"""
##########################
UPGMA
Natalia Dlugolecka
Bioinformatyka III
18/12/2017
##########################
"""

class sequence: #Tworzenie klasy laczacej nazwe i sekwencje

    def __init__(self, p, s):

        self.name = p

        self.seq = s

class distance: #Tworzenie klasy odpowiadajacej za dystans pomiedzy dwoma sekwencjami: funkcja wyliczajaca + konstrukcja klasy

    def __init__(self, seq1, seq2):

        self.seq1 = seq1
        self.seq2 = seq2
        self.seq1_elements = 1
        self.seq2_elements = 1
        self.distance = 0.0

    #Funkcja wyliczajaca dystans
    def count_distance(self, s1, s2):
        d = 0
        dominant_seq = min(len(s1), len(s2))

        for i in range(0, dominant_seq):
            if s1[i] != s2[i]:
                self.distance += 1

    def count_average_distance(self, x, y, seq1_elements, seq2_elements, add_elements): #Srednia pomiedzy kladem a sekwencja
        #seqX_elements - ilosc elementow przylaczonych w danym klastrze (tj. sekwencji)
        #add_elements - ilosc elementow dodawanego klastra (sekwencji porownywanej)

        self.distance = ((x * seq1_elements) + (y * seq2_elements)) / (seq1_elements + seq2_elements)
        self.seq1_elements = seq1_elements + seq2_elements #Zwiekszanie elementow o ilosc elementow w danym klastrze
        self.seq2_elements = add_elements

def load_file(fasta_file): #Wczytwanie zawartosci pliku fasta i edycja
    base = [] #sekwencje
    names = [] #nazwy sekwencji
    temp_string = ''
    id = ''

    with open(fasta_file, 'r') as file:
        for line in file:
            if line.startswith('>'):
                i = 0 #Pobieranie nazwy sekwencji z pliku - id
                while line[i] != ':':
                    i += 1
                i += 1
                while line[i] != '|':
                    id += line[i]
                    i += 1
                names += [id] #Dodawanie kolejnej nazwy
                id = ''

                base += [temp_string]
                temp_string = ''

            else:
                line = line.strip('\n')
                temp_string += line

    base.pop(0)
    base += [temp_string]

    return base, names

def min_distance(temp): #Szukanie minimum w obliczonych dystansach
    dl = len(temp)
    if dl != 0:
        min = temp[0].distance
        whos = temp[0].seq1 + temp[0].seq2 #Whos wskazuje na te nazwy sekwencji, ktore tworza ze soba minimalny dystans
        for i in range(1, dl):
            if temp[i].distance < min:
                min = temp[i].distance
                whos = temp[i].seq1 + temp[i].seq2
    return whos

def matrix_distances(base, names): #Wyliczanie dystansow pomiedzy wszystkimi sekwencjami (base - sekwencje, names - nazwy tych sekwencji)
    length = len(base)
    seq = []
    temp = []
    n = 0

    for i in range(0, length):
        seq += [sequence(names[i], base[i])]

    for i in range(0, length):
        for j in range(i+1, length):
            temp += [distance([seq[i].name], [seq[j].name])]
            temp[n].count_distance(seq[i].seq, seq[j].seq)
            n += 1

    return temp

def upgma_clustering(input_tab): #Skladanie w klastry

    while len(input_tab) > 1:
        min = min_distance(input_tab)
        elements = deleting_min(input_tab, min)

        if elements != -1:
            cluster_part1(input_tab, min, elements)
            deleting_useless_distances(input_tab, min)

def deleting_min(input_tab, min): #Usuwanie minimum po znalezieniu minimum
    i = 0
    elements = -1 #Zabezpieczenie
    length = len(input_tab)

    while i < length and (input_tab[i].seq1 != [min[0]] or input_tab[i].seq2 != [min[1]]): #Uwzglednienie przemiennosci
        i += 1

    if i < length:
        elements = [input_tab[i].seq1_elements, input_tab[i].seq2_elements]
        input_tab.pop(i) #Usuwanie

    return elements

def deleting_useless_distances(input_tab, min): #Usuwanie tego wiersza i tej kolumny po scaleniu ich w jeden klaster (A, B) -> usuwanie kolumny/wiersza A/B
    length = len(input_tab)
    i = 0

    while i < length:
        if (input_tab[i].seq1 == [min[0]] or input_tab[i].seq2 == [min[1]]) or (input_tab[i].seq2 == [min[0]] or input_tab[i].seq1 == [min[1]]): #Uwzglednienie przemiennosci
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

def cluster_part1(input_tab, min, elements): # [[A], []]
    length = len(input_tab)
    #Sekwencje oznaczaj tak naprawde klady wchodzace w sklad akutalnie rozpatrywanego kladu, ktory ma minimalny dystans, np. ((a,b), c) -> (a,b)
    for i in range(0, length):
        if input_tab[i].seq1 == [min[0]]: #Analizowanie pierwszej sekwencji kladu (seq1, X)
            war = cluster_part2(input_tab, [min[1]], input_tab[i].seq2)

            if war != -1:
                input_tab += [distance([[min[0]] + [min[1]]], input_tab[i].seq2)] #Tworzenie klastra
                input_tab[len(input_tab) - 1].count_average_distance(input_tab[i].distance, war, elements[0], elements[1], input_tab[i].seq2_elements) #Obliczanie sredniego dystansu

        elif input_tab[i].seq2 == [min[0]]: #Analizowanie drugiej sekwencji kladu (X, seq2)
            war = cluster_part2(input_tab, [min[1]], input_tab[i].seq1)
            if war != -1:
                input_tab += [distance(input_tab[i].seq1, [[min[0]] + [min[1]]])]  # Tworzenie klastra
                input_tab[len(input_tab) - 1].count_average_distance(input_tab[i].distance, war, elements[0], elements[1], input_tab[i].seq1_elements)  # Obliczanie sredniego dystansu

def newick(temp): #Rekurencyjna funkcja zapisujaca w postaci newick
    if type(temp).__name__ == 'list':
        length = len(temp)
        output = "("
        for i in range(0, length):
            if(i != length - 1):
                output += newick(temp[i]) + ", "
            else:
                output += newick(temp[i])
        output += ")"
    else:
        output = temp
    return output

######################################################################################################################

file = "fastaseq_2.fasta"
loaded_file = load_file(file)

matrix = matrix_distances(loaded_file[0], loaded_file[1])

upgma_clustering(matrix)

print(newick([matrix[0].seq1, matrix[0].seq2])+";") #Zapisanie w formacie Newick
