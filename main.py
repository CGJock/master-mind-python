import random
from termcolor import colored
import time

class DictGame():
  #banco de palabras para el brute y escoger la palabra a adivinar
    def __init__(self) -> None:
      self.palabras = ["amable","bonito","correr","dorado","felino","grande","habito", "jovial","kilito","lugare", "maduro","morado","oceano", "planta",
        "quinto","rubato","sereno","tierra","unidad","viajar","yeguar","zumban","alamos","besito","ceniza"]
      

class Mapa():
  def __init__(self) -> None:
    #instancias para hacer los prints en la consola
    self.guesses_grid = [['🌫️','🌫️','🌫️','🌫️','🌫️','🌫️'] for _ in range(12)]
    self.feedback_grid = [['🌫️','🌫️','🌫️','🌫️','🌫️','🌫️']for _ in range(12)]
    
  def add_arrays(self,player_input,attemp,coded_word):
    self.guesses_grid[attemp] = player_input
    self.feedback_grid[attemp] = coded_word
        
  
  def print_mapa(self):
  
      for guesses_grid, feedback_grid in zip(self.guesses_grid, self.feedback_grid):
            # Convirtiendo cada elemento de ambas filas a string
            row_map_str = "  ".join(map(str, guesses_grid))
            row_guess_str = "  ".join(map(str, feedback_grid))
            # Imprimiendo la fila combinada
            print(f"|  {row_map_str}  |  {row_guess_str}  |")
    
      
 
  #clase que controla la logica del juego y como seran mostrados los colores en consola 
class Decripting():
  def __init__(self, player_input: list,  word_guess: list, attemp: int, map_instance) -> None:
    coded_word = []#en este array se insertaran las letras con el color correspondiente
    print(f"palabra a adivinar{word_guess}")
    for letter in range(len(word_guess)):
      if player_input[letter] == word_guess[letter]:
        green = colored(player_input[letter],'green')
        coded_word.append(green) 
      elif player_input[letter] in word_guess:
        yellow = colored(player_input[letter],'yellow')
        coded_word.append(yellow) 
      elif player_input[letter] not in word_guess:
        red = colored(player_input[letter], 'red')
        coded_word.append(red)
    print(coded_word)
    map_instance.add_arrays(coded_word=coded_word,player_input=player_input, attemp=attemp)
    map_instance.print_mapa()
    
    
    
  #clase con la que el jugado escoge  
class PlayerElection():
    def __init__(self,player_input) -> None:
      self.player = player_input.split()
      
    
class CpuElection():
  def __init__(self,feedback_grid) -> None:
    self.cpu = [None] *6 #se le da un valor predeterminado de 6 a la lista
    self.correct_positions = [None] *6
    self.letters_in_word =  set()
    self.feedback_grid = feedback_grid 
    
  def cpu_brute(self, palabras: list):
    print("estoy usando metodo brute")
    index = random.randint(0,len(palabras) -1)
    self.cpu = list(palabras[index])
    palabras.pop(index)#se elimina la palabra que se uso en el indice
    return self.cpu
    
  def cpu_random(self):#metodo random 
    print("estoy usando meodo random")
    self.cpu = [chr(random.randint(ord('a'),ord('z'))) for _ in range(6)]
    return self.cpu
  
  def cpu_algorithm(self,word_guess,attemp,):
    print("usando el metodo algoritmo")
    #aperon seria la palabra llave 
    self.cpu  = ['a','p','e','r','o','n']
    
    
    if attemp == 0:
      print(f"esto es attemp {attemp}")
      self.cpu = ['a','p','e','r','o','n']
      return self.cpu
    
    if attemp > 0:
      #se le asigna el valor del ultimo elemento conocido del feedback
      previous_feedback = self.feedback_grid[attemp-1]
      for i in range(len(word_guess)):
        #se agregan o eliminan elementos a correct positions
        if previous_feedback[i] == colored(word_guess[i],'green'):
          self.correct_positions[i] = word_guess[i]
          self.letters_in_word.add(word_guess[i])
        elif previous_feedback[i] == colored(word_guess[i],'yellow'):
          self.letters_in_word.add(word_guess[i])
        elif previous_feedback[i] == colored(word_guess[i],'red'):
          self.letters_in_word.remove(word_guess[i])
    new_guess = self.cpu.copy()
   
      
    for i in range(len(word_guess)):
      if self.correct_positions[i] is not None:
        new_guess[i] = self.correct_positions[i]
      elif new_guess[i] in self.letters_in_word:
        for j in range(len(word_guess)):
          if new_guess[j] != word_guess[j]:
            new_guess[j] = new_guess[i]
            break
          
      else:
        new_guess[i] = chr(random.randint(ord('a'), ord('z')))
        
        
            
    self.cpu = new_guess
    return self.cpu
     
            
            
class WordToGuess():
  def __init__(self,palabras: list) -> None:
    index = random.randint(0,25)
    self.word_guess = list(palabras[index])
    print(self.word_guess)
    
  
  
class Game():
    def __init__(self) -> None:
      self.dict_game = DictGame()
      self.attemp = 0
      self.run = True
      self.map_instance = Mapa()
      game_mode = input("""Seleccione el modo de juego: 
                          '1' para adivinar la palabra:
                          '2' para proponer palabra a adivinar:""")
      if game_mode.lower() == "1":
        instance_word_gues = WordToGuess(self.dict_game.palabras)
        word_guess = instance_word_gues.word_guess
        while self.attemp < 12:
          player_input = list(input("guess the word: "))
          Decripting(player_input=player_input,word_guess=word_guess,attemp = self.attemp,map_instance = self.map_instance)
          self.attemp += 1
          if player_input == word_guess:
            print("Ganaste, palabra adivinada")
            exit()
          if self.attemp == 12:
            print("Llegaste al limite de turnos GAMEOVER")
            exit()
            
      elif game_mode.lower() == '2':
        player_input = list(input("Digite la palabra que quiere que se adivine: "))
        word_guess = player_input
        cpu_election = CpuElection(self.map_instance.feedback_grid)
        choosen_method = random.choice([lambda palabras: cpu_election.cpu_brute(self.dict_game.palabras),
                                        lambda palabras: cpu_election.cpu_random(),
                                        lambda palabras:  cpu_election.cpu_algorithm(word_guess,self.attemp)])
        while self.attemp < 12:
          print("Cpu thinking....")
          time.sleep(1.5)
          cpu_input = choosen_method(self.dict_game.palabras)
          Decripting(word_guess=player_input,attemp=self.attemp,map_instance = self.map_instance,player_input=cpu_input)
          self.attemp += 1
          if self.attemp == 12 or word_guess == cpu_input:
            print("juego terminado")
            exit()
              
             
 
Game()       

