#Name: Soren Soroush
#Date: September 8, 2018
#This program shifts ASCII code of strings by -1

reqString = input('Please type a string: ')
print(ord('`'))
for i in reqString:
    c = ord(i)
    print(chr(c-1))
