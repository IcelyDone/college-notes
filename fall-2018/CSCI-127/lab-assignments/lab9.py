#Name: Soren Soroush
#Date: September 24, 2018
#This program calculates the length and GC-ratio of a DNA sequence

dna = input('Enter a DNA sequence: ')
l = len(dna)
gc = dna.count('G') + dna.count('C')
gcr = gc / l
print('Length is', l)
print('GC-content is ', gcr)

    
