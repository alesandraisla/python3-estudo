# a é o identificador

a = 10
print(a)

#Operador aritmetico

print(2 + 5)
print(4 - 7)
print(9.4 / 3)
print(9.4 // 3)
print(10 % 3)

salario = 3450.45
despesas = 2456.2

percentual_comprometido = despesas / salario * 100

print(percentual_comprometido)

# Operador relacional 

print(3 > 4)
print( 3 != 2)
print(3 == 3)
print(3 == '3')

#Operadores de atribuicao

a = 3
a = a + 7
a += 5
a **= 7
a //= 256

#Operadores logicos

True or False
7 != 7 and 2 > 3

#Tabela verdade And
True and True
True and False
False and True
False and False

#Tabela verdade OR
True or True
True or False
False or True
False or False

#Tabela verdade Or exclusivo XOR
True != True
True != False
False != True
False != False

#Operador de negacao
not True
not False
not not -1 


saldo = 1000
salario = 4000
despesas = 3900

saldo_positivo = saldo > 0
despesas_controladas = salario - despesas >= 0.2 * salario
meta = saldo_positivo and despesas_controladas
print(meta)

#Desafio operadores logicos

trabalho_terca = True
trabalho_quinta = False

#Confirmando os 2: TV 5- + sorvete
#Confirmando apenas 1: Tv 32 + sorvete
#Nenhum confirmado : Fica em casa

tv_50 = trabalho_terca and trabalho_quinta
sorvete = trabalho_terca or trabalho_quinta
tv_32 = trabalho_terca != trabalho_quinta
mais_saudavel = not sorvete

print("tv50={} tv32={} Sorvete={} Saudavel={}".format(tv_50, tv_32, sorvete, mais_saudavel))


#Operadores ternarios

esta_chuvendo = True
'Hoje estou com as roupas ' + ('secas', 'molhadas')[esta_chuvendo]


frase = 'Hoje estou com as roupas ' + ('molhadas' if esta_chuvendo else 'secas')
print(frase)



lista = [ 1, 2, 3, 'Ana']
2 in lista
'Ana'not in lista

x = 3
y = x
z = 3
x is y
y is z
x is not z

lista_a = [ 1,2,3]
lista_b = lista_a
lista_c = [ 1,2,3]

#Builtins

# type
# print
# help

#Conversão de tipos

# 2 + 3
# '2' + '3'
# 2 + '3'
a = 2
b = '3'
c = '3.4'

print(type(a))
print(type(b))
print(a + int(b))
print(float(c))

# Coerção automática

d = 10 / 2
is_inteiro = d.is_integer()
print(is_inteiro)

from decimal import Decimal, getcontext

Decimal(1) / Decimal(7)

#Numero de casas decimais neste caso seria 4
getcontext().prec = 4
Decimal(1) / Decimal(7)
Decimal.max(Decimal(1), Decimal(7))

dir(Decimal)

#Tipos de String

dir(str)
nome = 'Lara Croft'
print(nome[0])
print(nome[-6:])
print(nome[::-1])


numeros = '123456789'
numeros
numeros[::]
numeros[::2]
numeros[1::2]
numeros[::-1] # inverter a string

frase = 'Python é uma linguagem excelente'
'py' not in frase
'ing'in frase
len(frase)
'py'in frase.lower()
frase.lower()
frase.split()
frase.split('E')

a = '123'
b = 'de Oliveira 4'
a.__add__(b)

#Lista
lista = []
type(lista)
dir(lista)
# help(list)
len(lista)
lista.append(5)
lista.append(3)

nova_lista = [1, 5, 'Ana']
nova_lista.remove(5)
nova_lista.reverse()

lista2 = [ 1, 2, 'Henrique', 'Isla']
# lista.index('Henrique')
# lista.index(1)
'Isla'in lista
'Quito'not in lista
lista[0]
lista[-1]
lista[1:3]
del lista[1]

# Tupla - nao pode ser modificada

# tupla = tuple()
# tupla = ()
# type(tupla)
# dir(tupla)
# tupla = ('um')
# tupla = ('um',)
# tupla[0]
# cores = ('verde', 'azul', 'rosa')
# cores[0]
# cores[-1]
# cores[1:]

# cores.index('amarelo')
# cores.count('Azul')
# len(cores)

#Dicionario - Indexada com string 

pessoa = {
  'nome': 'Isla',
  'idade': 34,
  'cursos': ['ingles', 'react']
}

type(pessoa)
dir(dict)
len(pessoa)
pessoa['nome']
pessoa['idade'][1]
pessoa['idade']= 30
pessoa['cursos'].append('Angular')
print(pessoa)
pessoa.pop('idade')
pessoa.update({'idade': 40, 'Sexo': 'F'})
del pessoa['cursos']
pessoa.clear()


#Conjunto - nao aceita repeticao Set

a = {1, 2, 3}
type(a)
a = set('coder')
print(a)
print('3' in a, 4 not in a)
{1, 2, 3} == { 3, 2, 1, 3}

c1 = { 1, 2}
c2 = { 2, 3}
c1.union(c2)
c1.intersection(c2)
c1.update(c2)
c1
c2 <= c1
c1 >= c2


#Interpolacao %f quebrada %string %d inteiro 

nome, idade = 'Ana', 30
 