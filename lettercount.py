""" this exercise analyzes a text file and tabulates a number for each letter in the alphabet, example a b c and so on"""

#first method finds the ID number for each letter using the ASCII key
#then converts the letters to numbers and tallies the frequency of each number

from sys import argv
script, txt = argv

f = open(txt)
captured_text = f.read()
f.close ()

counter = [0] * 26

for letter in captured_text.lower():
   letter_id = ord(letter) - 97
    print letter_id
    
   if letter_id >= 0 and letter_id < 25:
        
       counter[letter_id] += 1
        
for num in counter:  
   print num
    


"""second method uses a dictionary where each key is a letter with a value"""
"""the counter tracks the number of times each letter appears"""

from sys import argv
script, txt = argv

f = open(txt)
captured_text = f.read()
f.close()

#creates a dict called count    
count = {}

for character in captured_text.lower():

    if character in count:
        count[character] += 1
    else:        
        count[character] = 1

for character in count:
    print "%s: %d" % (character, count[character])


