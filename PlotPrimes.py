# Plot Primes
# Using a really fast algorithm 
# Found here: https://stackoverflow.com/questions/4114167/checking-if-a-number-is-a-prime-number-in-python

import math
from itertools import count, islice
import matplotlib.pyplot as plt
from random import choice, randint
import wave
import struct

def isPrime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(math.sqrt(n)-1)))

def generatePrimes(n, min=0, currentPrimes=[]):
    numFound = 0
    checkNum = min

    x = 0
    y = 1

    primePoints = currentPrimes

    while numFound < n:
        if isPrime(checkNum):
            numFound += 1
            primePoints.append(checkNum)

        checkNum += 1
    return primePoints

def linearize(points, start=0, end=1000000):
    # To make y = mx a straight line
    # transform => following slope m, f(x) = actualY - m(x)

    y1 = points[start]
    x1 = start

    y2 = points[end]
    x2 = end

    m = (y2 - y1)/(x2 - x1)


    audioArray = []

    index = 1
    for s in points:
                            # Mess with the math here for different tones
        audioArray.append((math.sin(index / (m*index - s)) * s)/1000)  # +/- 32769 is the max/min level for a wav file
        index += 1

    return audioArray

def writeToAudio(audioLevels, fname="output3.wav"):
    audioOutput = wave.open(fname, 'w')
    audioOutput.setparams((2, 2, 44100, 0, 'NONE', 'not compressed'))
    values = []

    for value in audioLevels:
        packedValue = struct.pack('h', int(value))
        audioOutput.writeframes(packedValue)  
        audioOutput.writeframes(packedValue)  # Twice because mono audio (for now)

    audioOutput.close()

def main():
    with open("primeNums.txt", "r") as f:
        primeStr = f.read()
    
    str_primes = primeStr.split('\n')
    
    primes = []
    for p in str_primes:
        primes.append(int(p))
    
#    Have first 1e7 prime numbers in db already, no need for more
#
#    print("Generating List of Primes...")
#    plotPoints = generatePrimes(380000, primes[-1] + 1, primes)
#
#    print("Adding to Prime DB")
#    with open("primeNums.txt", "w") as f:
#        first = True
#        for p in plotPoints:
#            if first == True:
#                f.write(str(p))
#                first = False
#            else:
#                f.write('\n' + str(p))

    transform = linearize(primes, randint(0, 620450/2), randint(620452/2, 620450))

    writeToAudio(transform[86000:])

    plt.plot(list(range(len(transform))), transform, '.')
    plt.show()

main()