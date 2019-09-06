#stretch to check if the user input is just one character and also a letter
#call the length function with the variable as an argument then call the
#.isalpha method on the variable

letter = []
print(letter)


letter.append(input("put your inout here > "))


if len(letter[0]) == 1 & letter[0].isalpha():
    print("Good job picking one letter!")
else:
    print("you fucked up big time try again")

print(letter)


print(len(letter[0]))


print(letter[0].isalpha())

def split(word):
    return [char for char in word]

#print(letter[0])
word = 'love'
print(word)
print(split(word))
