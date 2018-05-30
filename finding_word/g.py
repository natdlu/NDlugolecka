#Natalia Dlugolecka - Projekt G
import re

def szukanie_slowa_binarnie(new_file_name, items, desired_item, start=0, end=None):
    file = open(new_file_name, "w")    
    if end == None:
        end = len(items)

    if start == end:
        raise ValueError("%s was not found in the list." % desired_item)

    pos = (end - start) // 2 + start

    if desired_item == items[pos]:
        #return (">> Slowo '" + desired_item + "' znaleziono w okolicy pozycji nr " + str(pos) + ".")
        file.write(">> Slowo '" + desired_item + "' znaleziono w okolicy pozycji nr " + str(pos) + ".")
        #return  pos
    
    elif desired_item > items[pos]:
    
        return szukanie_slowa_binarnie(new_file_name, items, desired_item, start=(pos + 1), end=end)
    else:
        return szukanie_slowa_binarnie(new_file_name, items, desired_item, start=start, end=pos)

                      
def szukanie_slowa_liniowo(lista, slowo, new_file_name):
    file = open(new_file_name, "w")    
    pozycje=[]
    ile=0
    for pozycja, element in enumerate(slowa):
        if element == slowo:
            pozycje.append(pozycja+1)
            ile=ile+1
        
    if(ile == 0):
        file.write("Nie znaleziono slowa '" + slowo + "'.")
    
    else:
        file.write("Wyniki szukania slowa '" + slowo + "':")
        file.write("\n> znaleziono w sumie: " + str(ile))
        file.write("\n> pozycje: " + str(pozycje))
        return pozycje
        
            

def into_text (nazwa_pliku):  
    try:
        with open (nazwa_pliku) as plik:
            plik = open(nazwa_pliku, 'r')
            print ("Plik otwarty. Wczytano jako tekst.")
            text = plik.read()
            #text = text.split()
            #print(text)

    except IOError:
            print ("Taki plik nie istnieje, blad otwarcia pliku.")
            text = {}
    return text
    
    
def into_array(input_file):
    try:
        with open (nazwa_pliku) as plik:
            plik = open(nazwa_pliku, 'r')
            print ("Plik otwarty. Wczytano jako lista.")
            text = plik.read()
            text = text.split()
            #print(text)

    except IOError:
            print ("Taki plik nie istnieje, blad otwarcia pliku.")
            text = {}
    return text
   
    
def clusters (slowa, new_file_name): #na podstawie algorytmu z naszej ksiazki
    file = open(new_file_name, "w")    
    counts = {}
    for baza_1 in ['A', 'T', 'G', 'C']:
        for baza_2 in ['A', 'T', 'G', 'C']:
            for baza_3 in ['A', 'T', 'G', 'C']:
                trinucleotide = baza_1 + baza_2 + baza_3
                count = slowa.count(trinucleotide)
                if count > 0:
                    counts[trinucleotide] = count
    file.write("Znaleziono nastepujace zlepki 3-literowe:\n" + str(counts))
    return counts
    
def all_upper(tekst, new_file_name):
    file = open(new_file_name, "w")    
    upper = tekst.upper()
    file.write(upper)
    return upper
    
def finding_symbol(input_file, letter, value, output):
   # array = []
    file = open(input_file, "r")
    file2 = open(output, "w")
    file.seek(0)  
    lines = file.readlines()
    
    file2.write("Linie, gdzie znak '"+ letter +"' wystapil wiecej niz "+ str(value) + " razy:\n")
    
 #   for line in lines:
  #      if line[len(line)-1] is '\n':
   #         line = line[:-1]
    #        array.append(line.split(' '))
            
    for line in lines:
        sum=0
        for word in line:
            for char in word:
                if letter == char:
                    sum=sum+1
    
        if sum > value:
            file2.write("\t" + str(sum) + " razy | " + str(line))
    file.close()
    
def delete_trashes(text, output_file):
    digits = "1234567890"
    file = open(output_file, "w")
    delete_symbols = re.sub(r'[^\w .]', '', text) #najpierw usuwam wszystko, co nie jest "normalnym" znakiem, poza kropka
    delete_numbers = str.maketrans('', '', digits) #usuwam liczby.
    without_trashes = delete_symbols.translate(delete_numbers)
    file.write(without_trashes)

#-------------------------------------------------------------------------
    
nazwa_pliku = "dane.txt"
szukane = "Duis" #---------------------------------------------- SZUKANE SLOWO

output1 = "zlepki.txt"
dna = into_text(nazwa_pliku)
zlepki = clusters(dna, output1)
print("> Wyszukano wszystkie wystepujace zlepki.")


output2 = "szukane_slowo_liniowo.txt"
slowa = into_array(nazwa_pliku)
print(slowa)
szukanie_slowa_liniowo(slowa, szukane, output2)
print("> Wyszukano slowo '" + szukane + "' liniowo.")


output6 = "szukanie_slowa_binarnie.txt"
sortowane = sorted(slowa)
s = szukanie_slowa_binarnie(output6, sortowane, szukane, start=0, end=None)
#print(s)
print("> Wyszukano slowo '" + szukane + "' binarnie.")


output3 = "all_upper.txt"
all_upper(dna, output3)
print("> Zamieniono wszystkie litery na wielkie.")


output4 = "finding_symbol.txt"
symbol = "a" #------------------------------------------------- SZUKANA LITERA
value = 10#----------------------------------------MIN. WYSTAPIEN LITERY W LINII
finding_symbol(nazwa_pliku, symbol, value, output4)
print("> Wypisano linie, w ktorych litera '" + symbol + "' wystepuje wiecej niz "
      + str(value) + " razy.")

output5 = "delete_trashes.txt"
delete_trashes(dna, output5)
print("> Usunieto wszystkie liczby i symbole poza kropka.")
