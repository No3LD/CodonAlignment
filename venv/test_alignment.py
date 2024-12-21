import unittest
from functions import global_alignment, local_alignment

class TestAlignmentFunctions(unittest.TestCase):
    def setUp(self):
        self.match = 1
        self.mismatch = -1
        self.gap = -1

    ############################
    # Global Alignment Tests
    ############################
    def test_global_identical_short_sequences(self):
        seq1 = list("ACGT")
        seq2 = list("ACGT")


        score, aligned_seq1, aligned_seq2 = global_alignment(
            seq1, seq2, match=self.match, mismatch=self.mismatch, gap=self.gap
        )

        self.assertEqual(score, 4, "Score should be 4 for identical sequences")

        self.assertEqual("".join(aligned_seq1), "ACGT")
        self.assertEqual("".join(aligned_seq2), "ACGT")

        print("[PASSED] test_global_identical_short_sequences")

    def test_global_one_sequence_shorter(self):
        seq1 = list("ACG")
        seq2 = list("ACGT")

        score, aligned_seq1, aligned_seq2 = global_alignment(
            seq1, seq2, match=self.match, mismatch=self.mismatch, gap=self.gap
        )

        self.assertEqual(score, 2, "Score should be 2 when one sequence is shorter by one base")
        print("[PASSED] test_global_one_sequence_shorter")

    def test_global_classic_gattaca_example(self):
        seq1 = list("GATTACA")
        seq2 = list("GCATGCU")

        score, aligned_seq1, aligned_seq2 = global_alignment(
            seq1, seq2, match=self.match, mismatch=self.mismatch, gap=self.gap
        )

        self.assertTrue(-5 <= score <= 0, f"Expected a score around -2, but got {score}")
        print("[PASSED] test_global_classic_gattaca_example")

    ############################
    # Local Alignment Tests
    ############################
    def test_local_partial_overlap(self):
        seq1 = list("ACGTC")
        seq2 = list("AACGTT")

        max_score, aligned_seq1, aligned_seq2 = local_alignment(
            seq1, seq2, match=self.match, mismatch=self.mismatch, gap=self.gap
        )
        self.assertGreaterEqual(max_score, 4, "Local alignment score should be >= 4 for the overlapping region")
        print("[PASSED] test_local_partial_overlap")

    def test_local_slightly_larger_example(self):
        seq1 = list("GGTTGACTA")
        seq2 = list("TGTTACGTA")

        max_score, aligned_seq1, aligned_seq2 = local_alignment(
            seq1, seq2, match=self.match, mismatch=self.mismatch, gap=self.gap
        )
        self.assertGreaterEqual(max_score, 4, "Expected a local alignment with score >= 4")
        print("[PASSED] test_local_slightly_larger_example")


if __name__ == '__main__':
    unittest.main()
