
'''
En python se actualizan los elemmentos que se cambian en las listas, es una de las muy buenas funciones de oaython.
frutas.append('mangos') #mutuacion

lista coleccion de referencias no de datos como en otros lenguajes.
'''


# 5 Utilizando los pasos anteriores menos el 3. No verduras, quitar las verduras. Vaciar la lista de verduras

Verduras = ['tomate', 'paspas', 'cebollas', 'ajos']

frutas = ['piña', 'naranja', 'sandia']

carnes = ['mortadela', 'pollo', 'costilla de cerdo']

limpieza = ['jabon', 'cloro', 'shampoo']

lista_general = [Verduras, frutas, carnes, limpieza]

del Verduras

print(lista_general)

#Verduras = []

#print(lista_general)

pass

# Hay que probar las posibilidades siempre para es tar seguros
# a) Verduras.clear()
# b) del Verduras
# c) remove