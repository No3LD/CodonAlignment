import functions
import numpy
import pandas as pd

nucleotide_library = dict() # Stores nucleotide sequences given via CSV or direct string input
amino_acid_chain_library = dict() # Stores translated amino acid sequences
alignment_library = []

m = 1 # match value
mm = -1 # mismatch value
g = -1 # gap penalty

print("Welcome to my codon alignment tool. \nThis tool allows you to input nucleotide sequences directly or using a CSV, then perform global and local alignments on the translated amino acid sequences.")


while(True):
    command = input(
        "\nPlease enter a command \n"
        "(commands: csv, direct, exit, align, modify_scoring, alignment_library, amino_library, help)\n"
        "For more information on all the commands, please enter 'help' \n")

    if (command.lower() == "amino_library"):
        print("Below is the library of amino acid sequences translated from inputted nucleotide sequences this session:")
        print(amino_acid_chain_library)

    if (command.lower() == "help"):
        print("commands:"
              "csv: Add a batch of nucleotide sequences to the sequence libraries using a CSV in the format (Name, Sequence)."
              "direct: Input a sequence name and a nucleotide sequence directly via string input"
              "exit: Stop the program"
              "align: Perform an alignment"
              "modify_scoring: Modify the scoring values used for alignments"
              "alignment_library: Display the alignments performed during this session")

    if (command.lower() == "alignment_library"):
        print("Below is the library of alignments you have done during this session.")
        print(alignment_library)

    if (command.lower() == "modify_scoring"):
        print(f"Current Scoring: Match: {m}  Mismatch: {mm}  Gap: {g} \n")
        command = input("Which scoring value would you like to modify? (commands: match, mismatch, gap) ")

        if (command == "match"):
            v = input("Enter the value you want to assign to matches: ")
            m = int(v)

        if (command == "mismatch"):
            v = input("Enter the value you want to assign to mismatches: ")
            m = int(v)

        if (command == "gap"):
            v = input("Enter the value you want to assign to gaps: ")
            m = int(v)

    if (command.lower() == "exit"):
        break

    if (command.lower() == "csv"):
        filepath = input("Please enter the filepath of your CSV: ")
        nucleotide_library.update(functions.read_sequences_from_csv(filepath))

        for entry in nucleotide_library:
            if (entry in amino_acid_chain_library.keys()):
                continue

            amino_acid_chain_library[entry] = functions.translate_dna_to_protein(nucleotide_library[entry])

    if (command.lower() == "direct"):
        seq = input("Please enter your nucleotide sequence: ")
        name = input("Please enter a name for your nucleotide sequence: ")

        nucleotide_library[name] = seq.upper()

        for entry in nucleotide_library:
            if (entry in amino_acid_chain_library.keys()):
                continue

            amino_acid_chain_library[entry] = functions.translate_dna_to_protein(nucleotide_library[entry])


    if (command.lower() == "align"):
        command = input("Perform local or global alignment? (commands: local, global) ")

        if (command == "local"):

            print("Amino Acid Sequence Library:")
            print(amino_acid_chain_library)
            s_name1 = input("Enter first sequence name: ")
            s_name2 = input("Enter second sequence name: ")

            score, aln1, aln2 = functions.local_alignment(amino_acid_chain_library[s_name1],
                                                          amino_acid_chain_library[s_name2],
                                                          match=m, mismatch=mm, gap=g)

            alignment_library.append(("local", s_name1, aln1, s_name2, aln2, score))

            print(f"{s_name1}: {aln1}")
            print(f"{s_name2}: {aln2}")
            print(f"Score: {score}")


        if (command == "global"):

            print("Amino Acid Sequence Library:")
            print(amino_acid_chain_library)
            s_name1 = input("Enter first sequence name: ")
            s_name2 = input("Enter second sequence name: ")

            score, aln1, aln2 = functions.global_alignment(amino_acid_chain_library[s_name1],
                                                          amino_acid_chain_library[s_name2],
                                                          match=m, mismatch=mm, gap=g)

            alignment_library.append(("global", s_name1, aln1, s_name2, aln2, score))

            print(f"Seq1: {aln1}")
            print(f"Seq2: {aln2}")
            print(f"Score: {score}")
