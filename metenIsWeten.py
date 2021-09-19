a = int(input('vul het getal hier voor A: '))
b = int(input('vul het getal hier voor B: '))
print(type(a))

max = a
min = a

if a > b:
    print ('a is het grootste getal: ' ,max)
elif a < b:
    print('a is het kleinste getal" ' , min)
    max = a
else: 
    max = b
if a < b:
    min = a
else: 
    print('a en b zijn even groot')  
    min = b  
