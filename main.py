import random
import colorise

class DictGame():
    def __init__(self) -> None:
      self.palabras = ["amable","bonito","correr","dorado","felino","grande","habito", "jovial","kilito","lugare", "maduro","morado","oceano", "planta",
        "quinto","rubato","sereno","tierra","unidad","viajar","yeguar","zumban","alamos","besito","ceniza"]
      

class Mapa():
  def __init__(self) -> None:
    self.guesses_grid = [['🌫️','🌫️','🌫️','🌫️','🌫️','🌫️'] for _ in range(12)]
    self.feedback_grid = [['🌫️','🌫️','🌫️','🌫️','🌫️','🌫️']for _ in range(12)]
    
  def add_arrays(self,player_input,attemp,coded_word):
    self.guesses_grid[attemp] = player_input
    self.feedback_grid[attemp] = coded_word
        
  
  def print_mapa(self):
    # for j in range(len(player_input)):
    # for element in player_input:
      # print(f'print de prueba{self.map[attemp]}')
      
      # self.guesses_grid[attemp] = player_input
      # for row in self.guesses_grid:
      #   print("".join(map(str,row)))
      for guesses_grid, feedback_grid in zip(self.guesses_grid, self.feedback_grid):
            # Convirtiendo cada elemento de ambas filas a string
            fila_tablero_str = "  ".join(map(str, guesses_grid))
            fila_ayuda_str = "  ".join(map(str, feedback_grid))
            # Imprimiendo la fila combinada
            print(f"|  {fila_tablero_str}  |  {fila_ayuda_str}  |")
    
      
 
    
class Decripting():
  def __init__(self, player_input: list, cpu_input: list, word_guess: list, attemp: int, map_instance) -> None:
    coded_word = []
    
    
    for letter in range(len(word_guess)):
      if player_input[letter] == word_guess[letter]:
        coded_word.append(player_input[letter])
      elif player_input[letter] in word_guess:
        coded_word.append("?")
      elif player_input[letter] not in word_guess:
        coded_word.append("X")
    print(coded_word)
    map_instance.add_arrays(coded_word=coded_word,player_input=player_input, attemp=attemp)
    map_instance.print_mapa()
    
    
    
class PlayerElection():
    def __init__(self,player_input) -> None:
      self.player = player_input.split()
      
    
class CpuElection():
  def __init__(self,) -> None:
    self.cpu 
    pass
  

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
                          'Adivinar' para adivinar la palabra:
                          'Master' para proponer palabra a adivinar:""")
      if game_mode.lower() == "adivinar":
        instance_word_gues = WordToGuess(self.dict_game.palabras)
        word_guess = instance_word_gues.word_guess
        while self.attemp < 12:
          player_input = list(input("guess the word: "))
          Decripting(player_input=player_input,word_guess=word_guess, cpu_input=None,attemp = self.attemp,map_instance = self.map_instance)
          self.attemp += 1
          if self.attemp == 12:
            exit()
              
             
            
        
 
Game()       

    
   
   



    
  

# word_guess= list(input("word to decode"))
# word_guess= list(input("word to decode"))
# cpu_input = list("cacaos")


