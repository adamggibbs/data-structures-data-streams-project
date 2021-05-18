# https://www.youtube.com/watch?v=zURFD55lGBI
# usage: 
# import polyhash
# polyhash.generatePolyhash(string,length of array)

def generateAsciiMapping(string):
    if not string.isalnum():
        print(string)
        raise Exception("Not alphanumeric")
        
    l = list(string)
    n = []
    
    for char in l:
        char = char.lower()
        # a - z
        if ord(char) > 57:
            n.append(ord(char) - ord('a') + 11)
        # 0 - 9
        else: 
            n.append(ord(char) - 47)
    
    return n

def generatePolyhash(string,mod):
    p_power = 1
    prime = 37
    mapToInteger = generateAsciiMapping(string)
    value = 0
    
    for no in mapToInteger:
        value = (value + (no * p_power)) % mod
        p_power = (p_power * prime) % mod 
    
    return value