import benchmarking
import functions
import test_gens




#########################
# Specific Input Testing via CSV files
#########################

nucleotide_library = dict()
amino_acid_chain_library = dict()

filename = "test1_validcodons"
nucleotide_library.update(functions.read_sequences_from_csv(filename))
for entry in nucleotide_library:
    if (entry in amino_acid_chain_library.keys()):
        continue
    amino_acid_chain_library[entry] = functions.translate_dna_to_protein(nucleotide_library[entry])



