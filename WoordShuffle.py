import random

loop = 3
wordToShuffle = input("Kies een woord: ")

def shuffleWord(word):
        original = word
        randomised = ''.join(random.sample(original, len(original)))
        return randomised


for E in range(loop):
        RandomWoorden = shuffleWord(wordToShuffle)
        print (RandomWoorden)
