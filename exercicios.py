#exercicios

#tirar a raiz quadrada de um número

import math
num= int(input('Digite um número:'))
raiz=math.sqrt(num)
print('A raiz quadrada de {} é igual a {:.2f}.'.format(num,raiz))


#sortear um numero de 1 a 20

import random
num=random.randint(1,20)
print(num)


#Sortear um aluno da lista

import random
alunos=['Ana', 'Carlos', 'Roberto', 'Rogério']
for item in list (alunos):
     escolhido=random.choice(alunos)  
print(escolhido) 
     
     
#ver se a soma das duas dezenas é igual a raiz quadrada do numero de 4 digitos     
     
from math import sqrt

num=int(input('Digite um número de 4 digitos:'))
raiz=sqrt(num)
d1=num % 100
print (d1)
d2= num // 100
print(d2)
soma=(d1+d2)
print('A soma das duas dezenas de {} é igual a {}.'.format (num,d1+d2))

if raiz == soma:
    print('a raiz de {} é igual {}, que é a soma das suas duas dezenas.'.format(num,raiz))
else:
    print('a raiz de {} não é igual a soma das suas duas dezenas.'.format(num))
