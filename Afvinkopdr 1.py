def main():
    bestand = openbestand()
    seqq = sequentie(bestand)
    seq = sfilter(seqq)
    print(seq)
    codons = create_codons(seq)
    print(" ".join(codons))


def openbestand():
    try:
        file = open("m_p53.gb", "r")
        bestand = file.read().upper()
        return bestand
    except IOError:
        print("Er is iets fout gegaan bij het openen van het bestand, probeer het opnieuw.")
    except:
        print("Er is iets fout gedaan.")


def sequentie(bestand):
    seq = bestand.split("ORIGIN")
    return seq[1]


def sfilter(seqq): #sequence filter, checks if sequence is DNA
    seq1 = []
    for i in seqq:
        if i in ["A","T","G","C"]:
            seq1.append(i)
    seq = "".join(seq1)
    return seq


def create_codons(seq):
    start = seq.find("ATG")
    done = 0
    codons = []
    print(start)
    if start != -1:
        while start + 2 < len(seq) and done != 1:
            codon = seq[start:start + 3]
            if codon == "TAG" or codon == "TAA" or codon == "TGA":
                done = 1
            if not codon == "TAG" or codon == "TAA" or codon == "TGA":
                codons.append(codon)
                start += 3
    return codons

main()
