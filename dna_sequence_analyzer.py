# DNA Sequence Analyzer
# Project 1 - Computational Biology Portfolio

dna = input("Enter a DNA sequence: ").upper()

valid = True

for base in dna:
    if base not in "ATGC":
        valid = False
        break

if valid:
    print("\n===== DNA SEQUENCE ANALYSIS =====")

    print("Sequence Length :", len(dna))
    print("Adenine (A)     :", dna.count("A"))
    print("Thymine (T)     :", dna.count("T"))
    print("Guanine (G)     :", dna.count("G"))
    print("Cytosine (C)    :", dna.count("C"))

    gc_content = ((dna.count("G") + dna.count("C")) / len(dna)) * 100
    print("GC Content      :", round(gc_content, 2), "%")

    complement = {
        "A": "T",
        "T": "A",
        "G": "C",
        "C": "G"
    }

    reverse_complement = ""

    for base in dna:
        reverse_complement += complement[base]

    reverse_complement = reverse_complement[::-1]

    print("Reverse Complement :", reverse_complement)

    print("===============================")

else:
    print("\n❌ Invalid DNA Sequence")
    print("Please enter a sequence containing only A, T, G, and C.")