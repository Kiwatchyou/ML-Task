import re
import numpy as np
import random


def readout():
    entername = str(input('Enter name '))
    book = open('{}'.format(entername))
    gen = ''
    for line in book.readlines():
        gen+=str(line)
    book.close()
    return gen

def formation(gen):
    gen = gen.lower()
    gen = gen.strip()
    gen = re.split("[^a-zа-яё]+",gen) 
    return gen

def maketoken(gen):
    text = {}
    for i in range(len(gen) - 1):
        if text.get(gen[i], 0):
            pointer = text.get(gen[i])
            pointer.append(gen[i + 1])
            text[gen[i]] = pointer
        else:
            text[gen[i]] = [gen[i + 1]]
    return text

def save(token):
    name_file = str(input('Enter new name '))
    return np.save('{}.npy' .format(name_file), token) 