# Codon Alignment Tool

This script lets you feed in nucleotide sequences (either straight from a CSV or typed directly), translates those sequences into amino acids, and then does local or global alignments on them. It's a handy way to compare multiple protein sequences without having to juggle separate tools.

---

## What It Does
- Reads nucleotide sequences from a CSV or manual input.
- Translates each sequence into amino acids automatically.
- Performs both local alignments (Smith-Waterman) and global alignments (Needleman-Wunsch).
- Lets you tweak scoring options (match, mismatch, and gap) to see how they affect alignment results.
- Keeps a log of all your alignments in one place.

---

## Getting Started
1. Make sure you have Python 3, plus NumPy and pandas installed.  
2. Clone or download the repository, keeping `user_main.py` and `functions.py` in the same folder.  
3. Run the script:  
   ```bash
   python user_main.py
   ```
4. You’ll see a welcome message, then you can type in commands to control the tool.

---

## Basic Commands

- **csv**: Prompts you for a CSV file path. The file should have a "Name" and "Sequence" column. Each nucleotide sequence is translated into an amino acid sequence and stored.
- **direct**: Lets you type in a single nucleotide sequence and name it. The tool will translate it and store it.
- **amino_library**: Shows all amino acid sequences that have been generated so far.
- **alignment_library**: Shows a list of all alignments you’ve done in the current run.
- **align**: Asks whether you want a local or global alignment, then which two amino acid sequences to align.
- **modify_scoring**: Lets you change the values for match, mismatch, and gap.
- **help**: Displays info about all commands.
- **exit**: Closes out the script.

---

## Doing an Alignment
Say you have two sequences named "SeqA" and "SeqB" in your amino acid library. You can type:
```
align
```
Then choose `local` or `global` when asked. Enter "SeqA" and then "SeqB". The tool will show the alignment, score, and store it in the alignment library.

---

## Example Flow

1. **Load sequences**: Type `csv` and provide a path, like `my_sequences.csv`. The file should have lines like `SeqA,ATGCC...`.
2. **Check translations**: Type `amino_library` to see all amino acid sequences.
3. **Align**: Type `align`, pick local or global, then pick any two sequence names from the library.
4. **Review**: Type `alignment_library` to see a record of what you've aligned.

---

## Customizing Scoring
If you want to fine-tune the alignment, just type:
```
modify_scoring
```
You can change the current match reward, mismatch penalty, or gap penalty. Each alignment after that will use your new values.

---

