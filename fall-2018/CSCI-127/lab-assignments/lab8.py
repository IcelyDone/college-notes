#Name: Soren Soroush
#Date: September 8, 2018
#This program shifts ASCII code of strings by -1

reqWord = input('Please type a string: ')
pWord = ""
for ch in reqWord:
    offset = ord(ch) - ord('a') - 1 #how many letters past 'a'
    wrap = offset % 26  #if larger than 26, wrap back to 0
    newChar = chr(ord('a') + wrap)  #compute the new letter
#   print(wrap, chr(ord('a') + wrap))    #print the wrap & new letter
    pWord += newChar #add the newChar to the coded word
print(pWord)
