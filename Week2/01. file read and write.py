with open('firstpro.txt', 'w') as fwrite:
    fwrite.write('Hello,World!')

with open('firstpro.txt', 'r') as freader:
    p1 = freader.read(5)
    p2 = freader.read()
print(p1)    
print(p2)