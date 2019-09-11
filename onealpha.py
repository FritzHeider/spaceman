#qualifying tests
#stretch to check if the user input is just one character and also a guessed
#call the length function with the variable as an argument then call the
#.isalpha method on the variable



guessed = []
print(guessed)


guessed.append(input("put your inout here > "))


if len(guessed[0]) == 1 & guessed[0].isalpha():
    print("Good job picking one letter!")
else:
    print("you fucked up big time try again")

print('is the length of the guessed equal to 1? ')
print(len(guessed[0]) == 1)
print(len(guessed))


print("Is > " + guessed[0] + " < a letter?")
print(guessed[0].isalpha())

def split(word):
    return [char for char in word]
 
print (st)

print(split(word))
ts = (split(word))

print(len(ts))


#Prints iterations of charactes in my list!
for char in ts:
    i = 0
    print(char)
    i = i + 1
