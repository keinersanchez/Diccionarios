#1.Crea un diccionario vacío llamado perro
perro = {}

#2.Añade nombre, color, raza, patas y edad al diccionario perro.
perro['nombre'] = 'Balto'
perro['color'] = 'Blanco'
perro['raza'] =  'pitbul'
perro['patas'] =  4
perro['edad'] =   5

#3.Crea un diccionario de estudiante y añade nombre, apellido, sexo, edad, estado civil, habilidades, país, ciudad y dirección como claves del diccionario

estudiante = {
    'nombre': 'Keiner',
    'apellido': 'Sanchez',
    'sexo': 'Masculino',
    'edad': 23,
    'estado civil': 'Soltero',
    'habilidades':  ['Base de datos','natacion'],
    'pais': 'colombia',
    'ciudad': 'Cartagena',
    'dirección': 'zaragocilla'
}
#4.Obtén la longitud del diccionar
print("la longitud del diccionario",estudiante.__len__())

#5.Obtenga el valor de las habilidades y compruebe el tipo de datos, debe ser una lista
print('habilidades:', estudiante['habilidades'][0],'y',estudiante['habilidades'][1])
print(type(estudiante['habilidades']))

#6.Modifique los valores de las aptitudes añadiendo una o dos aptitudes

estudiante['habilidades'].append('guitarra')
estudiante['habilidades'].append('piano')

#7.Obtener las claves del diccionario como una lista
claves = list(estudiante.keys())
print("las claves del diccionario de estudiante:", claves)

#8.Obtener los valores del diccionario como una lista
valores=estudiante.values()
print(valores)

#9.Cambie el diccionario a una lista de tuplas utilizando el método items()
print(estudiante.items())

#10.Eliminar uno de los elementos del diccionario

del estudiante['pais']
print(" eliminar 'pais':", estudiante)


#11.Borrar uno de los diccionarios
del perro
