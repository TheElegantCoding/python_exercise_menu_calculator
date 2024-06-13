import os
import math

option = 0

def clear():
  os.system('cls' if os.name == 'nt' else 'clear')

def continueMenu(option):
  continueResult = input('¿Desea hacer otro calculo? (Y/n): ')

  if(continueResult.lower() == 'y'):
    option = 0
    clear()
    return option

  option = 4
  return option

def calculateVolumenCube(longitude):
  volume = math.pow(longitude, 3)
  return volume

def calculateVolumenPyramid(area, height):
  volume = (area * height) / 3
  return volume

def calculateVolumenParallepiped(longitude, width, height):
  volume = longitude * height * width
  return volume

clear()

while option != 4:
  option = int(input('-- Calculadora de volumen -- \n\n 1.- Cubo \n 2.- Pirámide \n 3.- Paralelepípedo \n 4.- Salir \n\n Seleccione una opción: '))

  if option == 1:
    clear()
    longitude = int(input('\nIngrese el valor de la longitud de un lado del cubo: '))
    volume = calculateVolumenCube(longitude)
    clear()
    print('\n El volumen del cubo es: ' + str(volume) + '\n')
    option = continueMenu(option)

  if(option == 2):
    clear()
    area = int(input('\nIngrese el area de la pirámide: '))
    height = int(input('\nIngrese la altura de la pirámide: '))
    volume = calculateVolumenPyramid(area, height)
    clear()
    print('\n El volumen de la pirámide es: ' + str(volume) + '\n')
    option = continueMenu(option)

  if(option == 3):
    clear()
    longitude = int(input('\nIngrese el valor de la longitud del paralelepípedo: '))
    width = int(input('\nIngrese el ancho del paralelepípedo: '))
    height = int(input('\nIngrese la altura del paralelepípedo: '))
    volume = calculateVolumenParallepiped(longitude, width, height)
    clear()
    print('\n El volumen del paralelepípedo es: ' + str(volume) + '\n')
    option = continueMenu(option)