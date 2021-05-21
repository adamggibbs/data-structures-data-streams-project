# https://www.youtube.com/watch?v=zURFD55lGBI
# usage: 
# import polyhash
# polyhash.generatePolyhash(string,length of array)

import string
import random

# this will enable us to get different mappings for different seeds hence independence
def randomMap(seed):
    mapping = {}
    characters =  string.ascii_lowercase + '0123456789'
    characters = list(characters)
    random.Random(seed).shuffle(characters)

    for i,char in enumerate(characters):
        mapping[char] = i + 1

    return mapping

#will return integer value
def generateAsciiMapping(item,seed):
    mapping = randomMap(seed)

    if not item.isalnum():
        raise Exception("Not alphanumeric")
        
    l = list(item)
    n = []
    
    for char in l:
        char = char.lower()
        n.append(mapping[char])
    
    return n

# will return a hash generated that maps an item between [0,(mod-1)]
def generatePolyhash(string,mod,seed):
    p_power = 1
    prime = 41
    mapToInteger = generateAsciiMapping(string,seed)
    value = 0
    
    for no in mapToInteger:
        value = (value + (no * p_power)) % mod
        p_power = (p_power * prime) % mod 
    
    return value