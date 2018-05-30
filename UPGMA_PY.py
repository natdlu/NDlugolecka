#Tworzenie klasy laczacej nazwe i sekwencje
class sequence:

    def __init__(self, p, s):

        self.name = p

        self.seq = s

#Tworzenie klasy odpowiadajacej za dystans pomiedzy dwoma sekwencjami: funkcja wyliczajaca + konstrukcja klasy
class distance:

    def __init__(self, seq1, seq2):

        self.seq1 = seq1
        self.seq2 = seq2
        self.distance = 0.0

    #Funkcja wyliczajaca dystans
    def count_distance(self, s1, s2):
        d = 0
        dominant_seq = min(len(s1), len(s2))

        for i in range(0, dominant_seq):
            if s1[i] != s2[i]:
                self.distance += 1

    def count_average_distance(self, x, y):
        self.distance = (x + y) / 2

#Szukanie minimum w obliczonych dystansach
def min_distance(temp):
    dl = len(temp)
    if dl != 0:
        min = temp[0].distance
        whos = temp[0].seq1 + temp[0].seq2
        for i in range(1, dl):
            if temp[i].distance < min:
                min = temp[i].distance
                whos = temp[i].seq1 + temp[i].seq2
    return whos

def clustering(input_tab):

    while len(input_tab) > 1:
        min = min_distance(input_tab)
        deleting_min(input_tab, min)
        cluster_part1(input_tab, min)
        deleting_useless_distances(input_tab, min)

def deleting_min(input_tab, min):
    i = 0
    length = len(input_tab)
    while i < length and (input_tab[i].seq1 != [min[0]] or input_tab[i].seq2 != [min[1]]):

        i += 1
    if i < length:
        input_tab.pop(i)

def deleting_useless_distances(input_tab, min):
    length = len(input_tab)
    i = 0
    while i < length:
        if (input_tab[i].seq1 == [min[0]] or input_tab[i].seq2 == [min[1]]) or (input_tab[i].seq2 == [min[0]] or input_tab[i].seq1 == [min[1]]):
            input_tab.pop(i)
            length -= 1
        else:
            i += 1

def cluster_part2(input_tab, value1, value2): #[[], [B]]
    i = 0
    length = len(input_tab)
    while i < length and ((input_tab[i].seq1 != value1 or input_tab[i].seq2 != value2) and (input_tab[i].seq2 != value1 or input_tab[i].seq1 != value2)):
        #Warunek uwzglednia przemiennosc, tzn. dystans pomiedzy A-B jest identyczny co dystans B-A
        i += 1
    if i < length:
        return input_tab[i].distance
    return -1


def cluster_part1(input_tab, min): # [[A], []]
    length = len(input_tab)

    for i in range(0, length):
        if input_tab[i].seq1 == [min[0]]:
            war = cluster_part2(input_tab, [min[1]], input_tab[i].seq2)
            if war != -1:
                input_tab += [distance([[min[0]] + [min[1]]], input_tab[i].seq2)] #Tworzenie "klastera"
                input_tab[len(input_tab) - 1].count_average_distance(input_tab[i].distance, war) #Obliczanie sredniego dystansu
        elif input_tab[i].seq2 == [min[0]]:
            war = cluster_part2(input_tab, [min[1]], input_tab[i].seq1)
            if war != -1:
                input_tab += [distance(input_tab[i].seq1, [[min[0]] + [min[1]]])]  # Tworzenie "klastera"
                input_tab[len(input_tab) - 1].count_average_distance(input_tab[i].distance, war)  # Obliczanie sredniego dystansu


base = []
fasta_file = "fastaseq_2.fasta"
temp_string = ''
id = ''
benek = []

with open(fasta_file, 'r') as  file:
    for line in file:
        if line.startswith('>'):
            i = 0 #Pobieranie nazwy sekwencji z pliku - id
            while line[i] != ':':
                i += 1
            i += 1
            while line[i] != '|':
                id += line[i]
                i += 1
            benek += [id] #Dodawanie kolejnej nazwy
            id = ''

            base += [temp_string]
            temp_string = ''

        else:
            line = line.strip('\n')
            temp_string += line

base.pop(0)
base += [temp_string]
#temp_string = ''

print(base)
print(benek)

length = len(base)
seq = []
dupa = []
n = 0

for i in range(0, length):
    seq += [sequence(benek[i], base[i])]

for i in range(0, length):
    for j in range(i+1, length):
        dupa += [distance([seq[i].name], [seq[j].name])]
        dupa[n].count_distance(seq[i].seq, seq[j].seq)
        print(str(dupa[n].seq1) + " " + str(dupa[n].seq2) + " " + str(dupa[n].distance))
        n += 1


clustering(dupa)

print("----------------")

for n in range(0, len(dupa)):
    print(str(dupa[n].seq1) + " " + str(dupa[n].seq2) + " " + str(dupa[n].distance))
