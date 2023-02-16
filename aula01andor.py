x = int(input("Digite o  número x: "))
y = int(input("Digite o número y: "))
z = int(input("Digite o número z: "))
if x > y and x > z:
    result = "x é o maior número"
    
elif y > x and y > z:
    result = "y é o maior número"
    
elif z > x and z > y:
    result = "z é o maior número"
    
else:
    result = "há números iguais"
print (result)