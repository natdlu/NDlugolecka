pdb_file="4r5j.pdb"
helix_value = 0
sheet_value = 0
helix_lengths = []
sheet_lengths = []
a = []
o = []
import string



with open(pdb_file, 'r') as  file:
    for line in file:
        if line.startswith('HELIX'):
            line = " ".join(line.split()).split(" ")
            a += line
            helix_lengths += [int(line[10])]

            helix_value += 1

        elif line.startswith('SHEET'):
            line = " ".join(line.split()).split(" ")
            a += line

            sheet_lengths += [int(line[3])]

            sheet_value += 1

print(helix_value)
print(helix_lengths)
print("Najdluzsza helisa: " + str(max(helix_lengths)))
print("Najkrotsza helisa: " + str(min(helix_lengths)))

print(sheet_value)
print(sheet_lengths)
print("Najdluzsza kartka: " + str(max(sheet_lengths)))
print("Najkrotsza kartka: " + str(min(sheet_lengths)))

#print(a)

#print(helix_value)
#print(helix_lengths)

#print(sheet_value)
#print(max(sheet_lengths))

