import pandas as pd
import numpy


def translate_dna_to_protein(dna_seq):

    dna_seq = dna_seq.upper().replace(" ", "")

    codon_table = {
        # Phenylalanine (F)
        "TTT": "F", "TTC": "F",
        # Leucine (L)
        "TTA": "L", "TTG": "L", "CTT": "L", "CTC": "L", "CTA": "L", "CTG": "L",
        # Isoleucine (I)
        "ATT": "I", "ATC": "I", "ATA": "I",
        # Methionine (M) - Start codon
        "ATG": "M",
        # Valine (V)
        "GTT": "V", "GTC": "V", "GTA": "V", "GTG": "V",
        # Serine (S)
        "TCT": "S", "TCC": "S", "TCA": "S", "TCG": "S", "AGT": "S", "AGC": "S",
        # Proline (P)
        "CCT": "P", "CCC": "P", "CCA": "P", "CCG": "P",
        # Threonine (T)
        "ACT": "T", "ACC": "T", "ACA": "T", "ACG": "T",
        # Alanine (A)
        "GCT": "A", "GCC": "A", "GCA": "A", "GCG": "A",
        # Tyrosine (Y)
        "TAT": "Y", "TAC": "Y",
        # Histidine (H)
        "CAT": "H", "CAC": "H",
        # Glutamine (Q)
        "CAA": "Q", "CAG": "Q",
        # Asparagine (N)
        "AAT": "N", "AAC": "N",
        # Lysine (K)
        "AAA": "K", "AAG": "K",
        # Aspartic Acid (D)
        "GAT": "D", "GAC": "D",
        # Glutamic Acid (E)
        "GAA": "E", "GAG": "E",
        # Cysteine (C)
        "TGT": "C", "TGC": "C",
        # Tryptophan (W)
        "TGG": "W",
        # Arginine (R)
        "CGT": "R", "CGC": "R", "CGA": "R", "CGG": "R", "AGA": "R", "AGG": "R",
        # Glycine (G)
        "GGT": "G", "GGC": "G", "GGA": "G", "GGG": "G",
        # Stop codons represented by X
        "TAA": "X", "TAG": "X", "TGA": "X"
    }

    # Ensure sequence length is a multiple of 3
    if len(dna_seq) % 3 != 0:
        dna_seq = dna_seq[:(len(dna_seq )//3 ) *3]

    protein = []

    for i in range(0, len(dna_seq), 3):
        codon = dna_seq[i: i +3]
        amino_acid = codon_table.get(codon, "")

        if amino_acid:
            protein.append(amino_acid)
        else:
            # Codon not found in table
            pass

    return "".join(protein)


def local_alignment(seq1, seq2, match=1, mismatch=-1, gap=-1):
    """
    Local alignment via smith-waterman algorithm

    params:
        seq1 (str): First amino acid sequence as a string.
        seq2 (str): Second amino acid sequence as a string.
        match (int): Score for a match
        mismatch (int): Score for a mismatch
        gap (int): Score for a gap

    returns:
        tuple: (max_score, aligned_seq1, aligned_seq2)
            max_score (int): The highest local alignment score
            aligned_seq1 (list of str): Locally aligned subsequence of seq1
            aligned_seq2 (list of str): Locally aligned subsequence of seq2
    """
    n = len(seq1)
    m = len(seq2)

    H = [[0] * (m + 1) for _ in range(n + 1)]

    max_score = 0
    max_pos = (0, 0)


    for i in range(1, n + 1):
        for j in range(1, m + 1):

            if seq1[i - 1] == seq2[j - 1]:
                diag_score = H[i - 1][j - 1] + match
            else:
                diag_score = H[i - 1][j - 1] + mismatch

            up_score = H[i - 1][j] + gap
            left_score = H[i][j - 1] + gap

            best_score = max(0, diag_score, up_score, left_score)
            H[i][j] = best_score

            if best_score > max_score:
                max_score = best_score
                max_pos = (i, j)

    aligned_seq1 = []
    aligned_seq2 = []

    i, j = max_pos
    while i > 0 and j > 0 and H[i][j] > 0:
        score_current = H[i][j]
        score_diag = H[i - 1][j - 1]
        score_up = H[i - 1][j]
        score_left = H[i][j - 1]

        if seq1[i - 1] == seq2[j - 1]:
            step_score = match
        else:
            step_score = mismatch

        if score_current == score_diag + step_score:
            aligned_seq1.append(seq1[i - 1])
            aligned_seq2.append(seq2[j - 1])
            i -= 1
            j -= 1
        elif score_current == score_up + gap:
            aligned_seq1.append(seq1[i - 1])
            aligned_seq2.append("-")
            i -= 1
        elif score_current == score_left + gap:
            aligned_seq1.append("-")
            aligned_seq2.append(seq2[j - 1])
            j -= 1

    aligned_seq1.reverse()
    aligned_seq2.reverse()

    return max_score, aligned_seq1, aligned_seq2


def global_alignment(seq1, seq2, match=1, mismatch=-1, gap=-1):
    """
    Global alignment via needleman-wunsch algorithm

    params:
        seq1 (str): First amino acid sequence.
        seq2 (str): Second amino acid sequence.
        match (int): Score for a match.
        mismatch (int): Score for a mismatch.
        gap (int): Score for a gap.

    returns:
        tuple: (final_score, aligned_seq1, aligned_seq2)
            final_score (int): The score of the optimal global alignment
            aligned_seq1 (list of str): Globally aligned version of seq1
            aligned_seq2 (list of str): Globally aligned version of seq2
    """

    n = len(seq1)
    m = len(seq2)


    H = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        H[i][0] = H[i - 1][0] + gap
    for j in range(1, m + 1):
        H[0][j] = H[0][j - 1] + gap

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if seq1[i - 1] == seq2[j - 1]:
                diag_score = H[i - 1][j - 1] + match
            else:
                diag_score = H[i - 1][j - 1] + mismatch

            up_score = H[i - 1][j] + gap
            left_score = H[i][j - 1] + gap

            H[i][j] = max(diag_score, up_score, left_score)

    aligned_seq1 = []
    aligned_seq2 = []

    i, j = n, m
    while i > 0 or j > 0:
        if i > 0 and j > 0 and (H[i][j] == H[i - 1][j - 1] + (match if seq1[i - 1] == seq2[j - 1] else mismatch)):
            aligned_seq1.append(seq1[i - 1])
            aligned_seq2.append(seq2[j - 1])
            i -= 1
            j -= 1
        elif i > 0 and H[i][j] == H[i - 1][j] + gap:
            aligned_seq1.append(seq1[i - 1])
            aligned_seq2.append('-')
            i -= 1
        else:
            aligned_seq1.append('-')
            aligned_seq2.append(seq2[j - 1])
            j -= 1

    aligned_seq1.reverse()
    aligned_seq2.reverse()

    final_score = H[n][m]
    return final_score, aligned_seq1, aligned_seq2


def read_sequences_from_csv(csv_path, name_col="Name", seq_col="Sequence"):
    """
    Reads a CSV file containing named nucleotide sequences into a dictionary.

    CSV format: Name, Sequence

    params:
        csv_path (str): Path to the CSV file.
        name_col (str): Column name for the sequence names (default "Name").
        seq_col (str): Column name for the nucleotide sequences (default "Sequence").

    returns:
        dict: A dictionary where keys are sequence names and values are sequences.
    """

    df = pd.read_csv(csv_path)

    if name_col not in df.columns or seq_col not in df.columns:
        raise ValueError(f"Your CSV must contain columns '{name_col}' and '{seq_col}'.")

    sequences = df.set_index(name_col)[seq_col].to_dict()

    return sequences