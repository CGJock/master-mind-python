import random
import colorise

class DictGame():
    def __init__(self) -> None:
      self.palabras = ["amable","bonito","correr","dorado","felino","grande","habito", "jovial","kilito","lugare", "maduro","morado","oceano", "planta",
        "quinto","rubato","sereno","tierra","unidad","viajar","yeguar","zumban","alamos","besito","ceniza"]
      

class Mapa():
  def __init__(self) -> None:
    self.map = [
    ["🟦","🟦","🟦","🟦","🟦","🟦",],
    ["🟦","🟦","🟦","🟦","🟦","🟦",],
    ["🟦","🟦","🟦","🟦","🟦","🟦",],
    ["🟦","🟦","🟦","🟦","🟦","🟦",],
    ["🟦","🟦","🟦","🟦","🟦","🟦",],
    ["🟦","🟦","🟦","🟦","🟦","🟦",],
    ["🟦","🟦","🟦","🟦","🟦","🟦",],
    ["🟦","🟦","🟦","🟦","🟦","🟦",],
    ["🟦","🟦","🟦","🟦","🟦","🟦",],
    ["🟦","🟦","🟦","🟦","🟦","🟦",],
    ["🟦","🟦","🟦","🟦","🟦","🟦",],
    ["🟦","🟦","🟦","🟦","🟦","🟦",]
  ]
    
  def print_mapa(self,player_input):
    for j in range(len(player_input)):
      for i in range(len(player_input)):
        self.map[i] = player_input[i]
    print(self.map)
    
class Decripting():
  def __init__(self, player_input: list, cpu_input: list, word_guess: list) -> None:
    coded_word = []
    print(player_input)
    print(f"transformada{word_guess}")
    for letter in range(len(word_guess)):
      if player_input[letter] == word_guess[letter]:
        coded_word.append(player_input[letter])
      elif player_input[letter] in word_guess:
        coded_word.append("?")
      elif player_input[letter] not in word_guess:
        coded_word.append("X")
    print(coded_word)
    map_instance = Mapa()
    map_instance.print_mapa(player_input=player_input)
    
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
    def __init__(self,) -> None:
      self.run_game = True
      self.dict_game = DictGame()
      game_mode = input("""Seleccione el modo de juego: 
                          'Adivinar' para adivinar la palabra:
                          'Master' para proponer palabra a adivinar:""")
      if game_mode.lower() == "adivinar":
          instance_word_gues = WordToGuess(self.dict_game.palabras)
          word_guess = instance_word_gues.word_guess
          while self.run_game == True:
            player_input = list(input("guess the word: "))
            Decripting(player_input=player_input,word_guess=word_guess, cpu_input=None)
        
 
Game()       

    
   
   



    
  

# word_guess= list(input("word to decode"))
# word_guess= list(input("word to decode"))
# cpu_input = list("cacaos")


