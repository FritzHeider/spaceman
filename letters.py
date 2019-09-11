import random

guesses = []

def split(word):
    return [char for char in word]

alphabet = ("abcdefghijklmnopqrstuvwxyz")
print(alphabet)
print(split(alphabet))

letters = split(alphabet)
print(letters)
print(guesses)

print(len(letters))

guesses.append((letters.pop(5)))
print("these are popped over into new guesses list")
print(guesses)
print(letters)


print(len(letters))
