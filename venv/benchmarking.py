import time
import timeit
import cProfile
import pstats
import io
import statistics
import os
from memory_profiler import memory_usage

def benchmark_time_function(func, *args, **kwargs):
    """
    Benchmark execution time
    return: time elapsed (s)
    """
    start = time.perf_counter()
    func(*args, **kwargs)
    end = time.perf_counter()
    return end - start

def benchmark_timeit_function(func, *args, repeats=3, number=100, **kwargs):
    """
    Benchmark execution time
    - repeats: number of times to repeat the timing test
    - number: number of executions per repeat
    return: best time from repeats.
    """
    def wrapper():
        return func(*args, **kwargs)

    times = timeit.repeat(wrapper, repeat=repeats, number=number)
    return min(times) / number

def benchmark_memory_function(func, *args, **kwargs):
    """
    Benchmark memory usage
    return: max memory usage (MiB) during function execution.
    """
    mem_usage = memory_usage((func, args, kwargs), max_iterations=1) # memory usage samples
    return max(mem_usage) # peak memory usage in MiB

def profile_function(func, *args, **kwargs):
    """
    Profile a function and return stats as a string.
    """
    pr = cProfile.Profile()
    pr.enable()
    func(*args, **kwargs)
    pr.disable()

    s = io.StringIO()
    sortby = "cumulative"
    ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
    ps.print_stats()
    return s.getvalue()

def benchmark_input_size_scaling(func, input_generator, sizes, repeats=3):
    """
    Measures execution time as input size changes

    params:
        func (callable): The function to benchmark.
        input_generator (callable): A function that takes an integer (size) and returns an input of that size.
        sizes (list of int): A list of input sizes to test.
        repeats (int): How many times to run each size test.

    return:
        dict: {size: [run_times]} where run_times is a list of execution times for that size.
    """
    results = {}
    for size in sizes:
        run_times = []
        for _ in range(repeats):
            test_input = input_generator(size)
            test_input2 = input_generator(size)
            start = time.perf_counter()
            func(test_input, test_input2)
            end = time.perf_counter()
            run_times.append(end - start)
        results[size] = run_times
    return results


def benchmark_io_performance(func, file_generator, files, cleanup=True):
    """
    Measures execution time for when func performs I/O on given files.

    params:
        func (callable): The function to benchmark (should accept a filename as input).
        file_generator (callable): A function that takes a filename and size, and generates a test file.
        files (list of (filename, size)): A list of tuples specifying the filename and the size/content type.
        cleanup (bool): If True, delete test files after benchmarking.

    return:
        dict: {filename: execution_time} for each file tested.
    """
    results = {}
    for filename, size, line_length in files:
        # Generate test file
        file_generator(filename, size, line_length)

        start = time.perf_counter()
        func(filename)
        end = time.perf_counter()

        results[filename] = end - start

        if cleanup and os.path.exists(filename):
            os.remove(filename)
    return results

def benchmark_stability_variance(func, args=(), kwargs=None, runs=30):
    """
    Measures the stability and variance of execution time by running function multiple times.

    params:
        func (callable): function to benchmark.
        args (tuple): Positional arguments to pass to the function.
        kwargs (dict): Keyword arguments to pass to the function.
        runs (int): Number of times to run the function.

    return:
        dict: Contains mean, median, std, and all run times.
    """

    if kwargs is None:
        kwargs = {}
    run_times = []
    for _ in range(runs):
        start = time.perf_counter()
        func(*args, **kwargs)
        end = time.perf_counter()
        run_times.append(end - start)

    return {
        "mean": statistics.mean(run_times),
        "median": statistics.median(run_times),
        "std_dev": statistics.pstdev(run_times),
        "runs": run_times
    }