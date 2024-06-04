#Tipos de Dados em python
"""
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType"""

#Texto : str (String)
#Exemplos válidos
str1= "Texto1"
str2= 'Texto2'
str3= """Texto3"""
str4= '''Texto4'''
str5= "p"
print(type(str1))
print(type(str2))
print(type(str3))
print(type(str4))
print(type(str5))

#Tipos Numéricos
#Numérico: int (Inteiro)
inteiro = 2024
print(type(inteiro))
#Numérico: float (Flutuante)
flutuante = 2024.02
print(type(flutuante))
#Numérico: complex (Complexo)
complexo = 2024.02j
print(type(complexo))

#Tipos Sequências
#Sequências : list (Lista)
lista = ["banana","goiaba","laranja"]
print(type(lista))
#Sequências : tuple (Tupla)
tupla = ("banana","goiaba","laranja")
print(type(tupla))
#Sequências : range (Faixa)
faixa = range(5)
print(type(faixa))

#Tipos de Mapas
#Mapas: dict (dicionário)
dicionario = {"nome":"guedes","age":25}
print(type(dicionario))

#Tipos de Definição
#Definição: set (definir)
definir = {"cachorro","gato","pássaro"}
print(type(definir))
#Definição: frozenset (conjunto congelado)
definir = frozenset({"dog","cat","bird"})
print(type(definir))

#Tipos Booleanos
#Booleanos: bool (booleano)
booleano = True
print(type(booleano))

#Tipos Binários
#Binários: bytes (binario)
binario = b"gato"
print(type(binario))
#Binários: bytearray (binario)
binario = bytearray(5)
print(type(binario))
#Binários: memoryview (binario)
binario = memoryview(bytes(5))
print(type(binario))

#Tipo None
#None: NoneType (tipo none)
tipo_none= None
print(type(tipo_none))