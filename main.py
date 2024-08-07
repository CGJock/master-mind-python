import random
import colorise
import string

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
  
      for guesses_grid, feedback_grid in zip(self.guesses_grid, self.feedback_grid):
            # Convirtiendo cada elemento de ambas filas a string
            row_map_str = "  ".join(map(str, guesses_grid))
            row_guess_str = "  ".join(map(str, feedback_grid))
            # Imprimiendo la fila combinada
            print(f"|  {row_map_str}  |  {row_guess_str}  |")
    
      
 
    
class Decripting():
  def __init__(self, player_input: list,  word_guess: list, attemp: int, map_instance) -> None:
    coded_word = []
    print(f"palabra a adivinar{word_guess}")
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
  def __init__(self) -> None:
    self.cpu = [None] *6 #se le da un valor predeterminado de 6 a la lista
    
  def cpu_brute(self, palabras: list):
    print("estoy usando metodo brute")
    index = random.randint(0,len(palabras) -1)
    self.cpu = list(palabras[index])
    return self.cpu
    
  def cpu_random(self):
    print("estoy usando meodo random")
    self.cpu = [chr(random.randint(ord('a'),ord('z'))) for _ in range(6)]
    return self.cpu
  
  # def cpu_algorithm(self,word_guess):
  #   self.cpu = "aceron"
    
  #   for i in range(6):
  #     if self.cpu[i] == word_guess[i]:
  #       self.cpu[i] = word_guess[i]
  #     elif self.cpu[i] in word_guess[i]:
  #       pass


  # def cpu_decide(self, palabras,attemp):
  #     num = random.randint(0,1)
  #     if num == 0:
  #         return self.cpu_brute(palabras)
      
  #     elif num == 1:
  #         return self.cpu_random()
      
  #     return self.cpu
      
     
    
  
    
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
        cpu_election = CpuElection()
        choosen_method = random.choice([lambda palabras: cpu_election.cpu_brute(self.dict_game.palabras),
                                        lambda palabras: cpu_election.cpu_random()])
        while self.attemp < 12:
          cpu_input = choosen_method(self.dict_game.palabras)
          Decripting(word_guess=player_input,attemp=self.attemp,map_instance = self.map_instance,player_input=cpu_input)
          self.attemp += 1
          if self.attemp == 12 or word_guess == player_input:
            print("juego terminado")
            exit()
              
             
            
        
 
Game()       

    
   
   



    
  

# word_guess= list(input("word to decode"))
# word_guess= list(input("word to decode"))
# cpu_input = list("cacaos")


