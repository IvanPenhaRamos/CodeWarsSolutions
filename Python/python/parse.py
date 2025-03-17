def parse(data):

    n = 0

    result = []
    
    for letter in data:
        if letter == 'i': n += 1
        elif letter == 'd': n -= 1
        elif letter == 's': n **= 2
        elif letter == 'o': result.append(n)

    return result


# def parse(data):
#     n = 0
#     ops = {'i': lambda x: x + 1, 'd': lambda x: x - 1, 's': lambda x: x ** 2}  # ChatGPT propone usar un diccionario con funciones
    
#     result = []
#     for letter in data:
#         if letter in ops:
#             n = ops[letter](n)
#         elif letter == 'o':
#             result.append(n)

#     return result



print(parse("ooo")) # [0,0,0]
print(parse("ioioio")) # [1,2,3]
print(parse("idoiido")) # [0,1]
print(parse("isoisoiso")) # [1,4,25]
print(parse("codewars")) # [0]
print(parse("iiisdoso")) # [8,64]
print(parse("iiisdosodddddiso")) # [8,64,3600]


'''
Create a parser to interpret and execute the Deadfish language.

Deadfish operates on a single value in memory, which is initially set to 0.

It uses four single-character commands:

i: Increment the value
d: Decrement the value
s: Square the value
o: Output the value to a result array
All other instructions are no-ops and have no effect.

Examples
Program "iiisdoso" should return numbers [8, 64].
Program "iiisdosodddddiso" should return numbers [8, 64, 3600].
'''