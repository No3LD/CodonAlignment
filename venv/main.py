import benchmarking
import functions
import test_gens

if __name__ == '__main__':
    #########################
    # Generic (randomly generated input) benchmark testing
    #########################

    # Benchmark Execution Time
    dna_seq1 = test_gens.generate_random_nucleotide_codon_sequence(10000)
    dna_seq2 = test_gens.generate_random_nucleotide_codon_sequence(10000)
    amino_seq1 = functions.translate_dna_to_protein(dna_seq1)
    amino_seq2 = functions.translate_dna_to_protein(dna_seq2)

    elapsed = benchmarking.benchmark_time_function(functions.global_alignment, amino_seq1, amino_seq2)
    print(f"Function took {elapsed:.6f} seconds")

    # Benchmark with timeit
    avg_time = benchmarking.benchmark_timeit_function(functions.global_alignment, amino_seq1, amino_seq2, repeats=3, number=10)
    print(f"Average execution time per call (best of 3 runs): {avg_time:.6f} seconds")

    # Benchmark Memory Usage
    mem_peak = benchmarking.benchmark_memory_function(functions.global_alignment,amino_seq1, amino_seq2)
    print(f"Peak memory usage: {mem_peak:.2f} MiB")

    # Profiling
    profile_results = benchmarking.profile_function(functions.global_alignment, amino_seq1, amino_seq2)
    print("Profiling function:")
    print(profile_results)

    # Stability and Variance
    stability_results = benchmarking.benchmark_stability_variance(functions.global_alignment, args=(amino_seq1, amino_seq2), runs=30)
    print("Stability and variance of exec time:", stability_results)

    # # Input Size Scaling
    # sizes = [10, 100, 1000, 10000]
    # scaling_results = benchmarking.benchmark_input_size_scaling(functions.global_alignment, test_gens.generate_amino_acid_sequence, sizes)
    # print("Input size scaling exec time results:", scaling_results)

    # # I/O Performance
    # test_files = [("test_ln10len10.txt", 10, 10), ("test_ln100len10.txt", 100, 10), ("test_ln10len100.txt", 10, 100),
    #               ("test_ln100len100.txt", 100, 100), ("test_ln1klen100.txt", 1000, 100), ("test_ln10klen100.txt", 10000, 100),
    #               ("test_ln100len1k.txt", 100, 1000), ("test_ln100len10k.txt", 100, 10000), ("test_ln1klen1k.txt", 1000, 1000),
    #               ("test_ln10klen1k.txt", 10000, 1000), ("test_ln1klen10k.txt", 1000, 10000), ("test_ln10klen10k.txt", 10000, 10000)]
    # io_results = benchmarking.benchmark_io_performance(functions.read_sequences_from_csv, test_gens.generate_test_file, test_files)
    # print("I/O performance results:", io_results)
