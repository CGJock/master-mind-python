# master-mind-python
Creacion del juego WORDLE usando python ,(clases y composicion)
Nombre del creador:Jocksan Cardenas
**se usaron las bibliotecas, colored-termcolor, time, y random

-El juego incluye una clase game, que controla el flujo del juego, una clase mapa, que muestra las jugadas en consola, una clase para las plays de la maquina
y una clase para las plays del jugador, ademas de una clase que controla la logica para resolver los algoritmos

-se muestra al jugador en consola 2 arreglos, a la izquierda el arregllo con los inputs que el jugador haya escrito, a la derecha
esos inputs con un "hint de color"
verde = item posicion correcta
rojo = item posicion incorrecta
amarillo = item presente en palabra, posicion incorrecta

para el metodo random del bot se utilizo una manera manera sencilla que introduce letras aleatorias simplemente

para el metodo "brute" se hizo una impolementacion usando que utiliza una lista con un banco de palabras que ira emparejando en cada intento encontar la palabra con fuerza bruta

para el metodo "sofisticado" se intento basado en la posicon del ultimo elemento conocido del feedback revisar si el elemento cumplia las condiciones de los hints, pero solo se logro 
validar que los elementos verdes no puedan cambiar de posicion *SE NECESITA TRABAJAR EN ESO 

*SE NECESITA TRABAJAR TAMBIEN EN VALIDACIONES 