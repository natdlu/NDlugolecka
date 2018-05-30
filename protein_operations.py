"""
08.11.2017
Natalia Dlugolecka 
Techniki bioinformatyczne

361

"""

#source = '/home/student/ndlugolecka/l2'

#def open_file(source, file):
 #   with open(source, 'r') as  file:
#for line in file:

 #   if line.startswith('>'):
  #      pass

   # else:

    #    for i in line:
     #       if i == 'A':
      #          a += 1
       #     elif i == 'T':
        #        t += 1
         #   elif i == 'C':
          #      c += 1
           # else:
            #    g += 1



"""

#------------------------------------------------------------------------------------------------------------------------------- procent par CG
a = 0
g = 0
t = 0
c = 0

pary = 0
seq = 0



with open(DNA, 'r') as  file:
    for line in file:

        if line.startswith('>'):
            pass

        else:
            pary += line.count('G')
            pary += line.count('C')
            seq += len(line)

procent = (pary/seq)*100

print('\nDlugosc sekwencji: ', seq, '\nPar GC: ', pary, '\nProcent par GC: ', procent)

print(a, t, c, g, sep=' | ')

#------------------------------------------------------------------------------------------------------------------------------- slowniki tworzenie

with open(DNA, 'r') as  file:
    for line in file:
        line = line.strip('\n')

        if line.startswith('>'):
            pass

        else:
            for i in line:
                if i not in pep:
                    pep[i] = 1 #dodanie do slownika i przypisanie wartosci klucza

                else:
                    pep[i] += 1

for key in pep.keys():
    print(key, pep[key])
"""

#------------------------------------------------------------------------------------------------------------------------------ obliczanie masy bialka
"""
DNA = 'dnak.fasta' #plik z bialkiem

masa = 0
pep = {}
mass = { #wagi aminokwasow
    'A': 71.07, 'R': 156.18, 'N': 114.10, 'D': 115.08, 'C': 103.13, 'E': 129.11, 'Q': 128.12, 'G': 57.05, 'H': 137.12, 'I': 113.15,
    'L': 113.15, 'K': 128.17, 'M': 131.19, 'F': 147.17, 'P': 97.11, 'S': 87.11, 'T': 101.10, 'W': 186.21, 'Y': 163.17, 'V': 99.13
        }

#for key in mass.keys():
 #   print(key, mass[key])


with open(DNA, 'r') as  file:
    for line in file:
        line = line.strip('\n')

        if line.startswith('>'):
            pass

        else:
            for i in line:
                if i not in pep:
                    pep[i] = 1 #dodanie do slownika i przypisanie wartosci klucza


                else:
                    pep[i] += 1

#for key in pep.keys():
 #   print(key, pep[key])

print(".................")

masa = 0
aminokwasy = 0

for key in pep.keys():
    aminokwasy += pep[key]

for key in pep.keys():
    waga = pep[key]*mass[key]
    masa += waga

print('Waga bialka "z woda":', masa)
print('Bez wody:', masa-aminokwasy*18)

print(".................")

#------------------------------------------------------------------------------------------------------------------------------ odleglosc Hamminga

dna1 = 'MVGVLSHTPMRVTSALTRYCATGTCAVWQNRS'
dna2 = 'MVGVLSHTPMRVTSALTRYCATGTCAVWQNRS'

h = 0

for i in range(0, len(dna1)):

    if dna1[i] != dna2[i]:
        h += 1

print('Dlugosc sekwencji: ', len(dna1), '\nOdleglosc Hamminga: ', h, '\n..............\n')

#------------------------------------------------------------------------------------------------------------------------------ genebank na fasta

f_header = ">"
ori_flag = False
seq = "genbankseq.gb"
nazwa = "genbankseq.gb"

with open(seq, 'r') as  file:
    for line in file:
        if line.startswith('LOCUS'):
            header = line.split()
            f_header += ' '.join(header[1:])

        if line.startswith('ORIGIN'):
            ori_flag = True

            continue

        if ori_flag:
            seq_line = line.split()
            seq += ''.join(seq_line[1:]).upper()
            seq += '\n'


print(f_header)
print(seq)

fasta1 = "FASTA_"
fasta = fasta1 + nazwa

with open(fasta, 'a') as f:
    f.write(f_header)
    f.write(seq)
    """
#------------------------------------------------------------------------------------------------ <3 DNA DO BIALKA <3


mass = { #wagi aminokwasow
    'A': 71.07, 'R': 156.18, 'N': 114.10, 'D': 115.08, 'C': 103.13, 'E': 129.11, 'Q': 128.12, 'G': 57.05, 'H': 137.12, 'I': 113.15,
    'L': 113.15, 'K': 128.17, 'M': 131.19, 'F': 147.17, 'P': 97.11, 'S': 87.11, 'T': 101.10, 'W': 186.21, 'Y': 163.17, 'V': 99.13
        }

map = {"UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L",
           "UCU": "S", "UCC": "s", "UCA": "S", "UCG": "S",
           "UAU": "Y", "UAC": "Y", "UAA": "STOP", "UAG": "STOP",
           "UGU": "C", "UGC": "C", "UGA": "STOP", "UGG": "W",
           "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
           "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
           "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
           "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
           "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M",
           "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
           "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K",
           "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",
           "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
           "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
           "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
           "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G", }



ori_flag = False
seq = "genbankseq.gb"
rna_seq = ''
dna_seq = ''
protein_seq = ''


with open(seq, 'r') as  file:
    for line in file:
        if line.startswith('ORIGIN'):
            ori_flag = True

            continue

        if ori_flag:
            seq_line = line.split()
            #dna_seq += ''.join(seq_line[1:]).upper()
            dna_seq += ''.join(seq_line[1:]).upper()

            #dna_seq += '\n'

    for i in dna_seq:
        if i == 'A':
            rna_seq += 'U'

        if i == 'C':
            rna_seq += 'G'

        if i == 'G':
            rna_seq += 'C'

        if i == 'T':
            rna_seq += 'A'


print('\nDNA: ')
print(dna_seq) #-------------------------------------------------------------------------------------- sekwencja DNA
print('\nRNA: ')
print(rna_seq) #----------------------------------------------------------------------------------- sekwencja RNA

start_flag = False


"""
#print(rna_seq[29:].find("UAA"))
print(rna_seq[29:].find("UGA"))
#print(rna_seq[29:].find("UAG"))

print('\n')
print((rna_seq[29:].find("UGA") - rna_seq.find("AUG"))/3)
"""


for i, j in enumerate(rna_seq): #-------------------------------------------------------- z lekcji gowno nie dzialajace

    start = i
    stop = i+3

    if stop > len(rna_seq):
        break

    else:
        codon = rna_seq[start:stop]
        acid = map[codon]
        #print(i, map[codon])

        if map[codon] == 'STOP' and start_flag:
            break

        if codon == 'AUG':
            start_flag = True

        if start_flag:
            protein_seq += map[codon]

"""
#ABSOLUTNIE TO SAMO TYLKO ZE BEZ FLAGI:

n = 3
for a in range(where_start, len(rna_seq)):

    if a+n > len(rna_seq):
        break

    else:
        codon = rna_seq[a:a+n]
        acid = map[codon]
        print(codon)

    if map[codon] == 'STOP':
        break

    protein_seq += map[codon]

"""
print('\nKodon START na pozycji: ')
print(rna_seq.find("AUG"))
where_start = rna_seq.find("AUG") #-------------------------------------------------------------- szukanie kodonu START


print("Kodon STOP na pozycji: ", rna_seq.find("UAA"))
where_stop2 = rna_seq.find("UGA")
where_stop3 = rna_seq.find("UAG")

#print("Kodon stop:\n", where_stop1, where_stop2, where_stop3)


rna_seq_start = rna_seq[where_start:]
print('\nRNA od kodonu START: ')
print(rna_seq_start) #----------------------------------------------------------------------- RNA od kodonu START

#------------------------------------------------------------------------------------------------------ @@@@ moj sposob

n = 3
nuc_table = ''
nuc_table = ([rna_seq[a:a + n] for a in range(where_start, len(rna_seq), n)]) #prawidlowe dzielenie na nukleotydy po znalezieniu AUG start

proteina = ''

print('\nWlasciwe dzielenie na kodony: ')
for k in range(0, len(nuc_table)-1):

   print(nuc_table[k]) #--------------------------------------------------------- od START do najblizszego kodonu STOP
   amino = nuc_table[k]

   if map[amino] == 'STOP':
       break

   proteina += map[amino]

proteina = proteina.upper()

weight = 0

for amino in proteina:
    weight += mass[amino]

print('\nMasa [Da]: ')
print(weight)
print('\nMasa zdehydrolizowana [Da]: ')
print(weight-32*18)

"""5'3' Frame 1 https://web.expasy.org/translate/ Trankrypcja rna_seq_start na bialko 
Met V G V L S H T P Met R V T S A L T R Y C A T G T C A V W Q N R S Stop"""
source_seq = 'MVGVLSHTPMRVTSALTRYCATGTCAVWQNRS'
result_seq = proteina

h = 0

for i in range(0, len(result_seq)):

    if source_seq[i] != result_seq[i]:
        h += 1

print('\nSekwencja zrodlowa: ')
print(source_seq)
print('\nSekwencja wynikowa: ')
print(result_seq)
print('\nDlugosc sekwencji: ')
print(len(result_seq))
print('\nOdleglosc Hamminga: ')
print(h)
