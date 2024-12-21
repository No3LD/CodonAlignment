import benchmarking
import functions
import random
import csv

nucleotides = ['A', 'T', 'C', 'G']

codon_table = {
    "TTT": "F", "TTC": "F",
    "TTA": "L", "TTG": "L", "CTT": "L", "CTC": "L", "CTA": "L", "CTG": "L",
    "ATT": "I", "ATC": "I", "ATA": "I",
    "ATG": "M",
    "GTT": "V", "GTC": "V", "GTA": "V", "GTG": "V",
    "TCT": "S", "TCC": "S", "TCA": "S", "TCG": "S", "AGT": "S", "AGC": "S",
    "CCT": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "ACT": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    "GCT": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    "TAT": "Y", "TAC": "Y",
    "CAT": "H", "CAC": "H",
    "CAA": "Q", "CAG": "Q",
    "AAT": "N", "AAC": "N",
    "AAA": "K", "AAG": "K",
    "GAT": "D", "GAC": "D",
    "GAA": "E", "GAG": "E",
    "TGT": "C", "TGC": "C",
    "TGG": "W",
    "CGT": "R", "CGC": "R", "CGA": "R", "CGG": "R", "AGA": "R", "AGG": "R",
    "GGT": "G", "GGC": "G", "GGA": "G", "GGG": "G",
    "TAA": "X", "TAG": "X", "TGA": "X"
}
valid_codons = [codon for codon, aa in codon_table.items()]


def generate_test_file(filename, size, line_length_codons):
    """
    Generate a CSV file with the format: Name,Sequence
    'size': Number of sequences (rows) to generate.
    'line_length_codons': Number of codons in each sequence.
    """
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Name", "Sequence"])

        for i in range(1, size + 1):
            sequence_codons = random.choices(valid_codons, k=line_length_codons)
            sequence = "".join(sequence_codons)

            seq_name = f"Seq{i}"

            writer.writerow([seq_name, sequence])


def generate_valid_codons_sequence(num_codons):
    """
    Generate a DNA sequence composed of codons that each translate into an amino acid.
    'num_codons' number of codons in sequence.
    """
    chosen_codons = random.choices(valid_codons, k=num_codons)
    return "".join(chosen_codons)


def generate_random_nucleotide_codon_sequence(size):
    """
    Generate a random DNA sequence of given length that is divisible by 3,
    ensuring it can be split into (valid or invalid) codons.

    If size is not a multiple of 3, it will be adjusted down to the nearest
    multiple of 3.
    """
    nucleotides = ['A', 'T', 'G', 'C']
    size = size * 3

    return "".join(random.choices(nucleotides, k=size))

def generate_amino_acid_sequence(size):
    """
    Generate a random amino acid sequence of given length.
    Uses the 20 standard amino acids single-letter codes and X for stop codons
    """
    amino_acids = ['A','R','N','D','C','E','Q','G','H','I',
                   'L','K','M','F','P','S','T','W','Y','V','X']
    return "".join(random.choices(amino_acids, k=size))