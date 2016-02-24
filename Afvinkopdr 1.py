codontable = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
    }

def main():
    bestand = openbestand()
    seqq = sequentie(bestand)
    seq = sfilter(seqq)
    print(seq)
    codons = create_codons(seq)
    print(" ".join(codons))
    amino_acid_seq = get_aminoacids(codons)
    print (amino_acid_seq)
    


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

def get_aminoacids(codons): # Add DNA-codon based aminoacid to a list 
    aminoacids = []
    for codon in codons:
        aminoacids.append (get_aminoacid(codon))
    return ''.join(aminoacids)

def get_aminoacid(codon): # Return Aminoacid
    return codontable[codon.upper()]

    
main()
