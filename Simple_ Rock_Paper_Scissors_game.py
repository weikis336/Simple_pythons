import random
from getpass import getpass
import os
def clear_terminal():
  os.system('cls' if os.name == 'nt' else 'clear')
  #Borra terminal

def startgame():
  #Inicio del juego, consulta la cantidad de jugadores 
  human = 0
  print("Welcome to this game of Rock, Paper, Scissors!")
  print("Select one of the following options:")
  gameset = input("Twoplayers or Singleplayer mode\n")
  if gameset.lower() in ["twoplayers", "2player", "2 players", "two"]:
      human = 2
  elif gameset.lower() in ["singleplayer", "single", "1player", "1 player"]:
      human = 1
  else:
      print("Invalid input, please try again")
      startgame()
  return human

def rounds():
    #Consulta la cantidad de rondas a jugar
    rounds = 90
    while rounds not in range(0, 6):
      rounds = (input("Please set the number of rounds 1 to 5 games\n"))
      if rounds.isdigit() and int(rounds) in range(1,6):
        return rounds
      else:
        print("Insert a valid number in the range")

def match(numberofplayers, player, player1):
    #Funcion que ejecuta el juego
    playerselect = "something"
    playerselect1 = "something"
    game = 12
    #Se comprueba el numero de jugadores para asignar a player1 la CPU
    if numberofplayers == 1:
      #Se asigna valor aleatorio a la seleccion de la CPU
      cpu = random.randint(1,3)
      if cpu == 1:
        cpu = "rock"
      elif cpu == 2:
        cpu = "paper"
      else: 
        cpu = "scissors"
      playerselect1 = cpu
      #Se pregunta al jugador cual va ser su seleccion para la jugada
      playerselect = input("Select your option: Rock, Paper, or Scissors\n")
      while playerselect not in ["rock", "paper", "scissors"]: 
        #Se repite en bucle si lo escrito anteriormente por el jugador no es valido
        print("Invalid input, please try again")
        playerselect = input("Select your option: Rock, Paper or Scissors\n")
      #Se le transmite a la funcion battle los valores de todos los integrantes de la partida
      game = battle(playerselect, playerselect1, player, player1)
    if numberofplayers == 2:
      #Se pregunta al jugador cual va ser su seleccion para la jugada
      playerselect = getpass("Select your option: " + player + " Rock, Paper, or Scissors\n")
      while playerselect not in ["rock", "paper", "scissors"]:
        print("Invalid input, please try again")
        playerselect = getpass("Select your option: " + player + " : Rock, Paper or Scissors\n")
        #Se repite en bucle si lo escrito anteriormente por el jugador no es valido
      playerselect1 = getpass("Select your option: " + player1 + " Rock, Paper, or Scissors\n")
      while playerselect1 not in ["rock", "paper", "scissors"]:
        print("Invalid input, please try again")
        playerselect1 = getpass("Select your option: " + player1 + "  Rock, Paper or Scissors\n")
       #Se le transmite a la funcion battle los valores de todos los integrantes de la partida
      game = battle(playerselect, playerselect1, player, player1)
    return game

def battle(playerselect, playerselect1, player, player1):
  game = 12
  #Se comprueba el resultado de la jugada
  if playerselect == "rock" and playerselect1 == "paper":
    print("You lose, " + player + ", You win " + player1)
    game = "lose"
  elif playerselect == "rock" and playerselect1 == "scissors":
    print("You win " + player + ", You lose " + player1)
    game = "win"
  elif playerselect == "paper" and playerselect1 == "scissors":
    print("You lose, " + player + ", You win " + player1)
    game = "lose"
  elif playerselect == "paper" and playerselect1 == "rock":
    print("You win " + player + ", You lose " + player1)
    game = "win"
  elif playerselect == "scissors" and playerselect1 == "rock":
    print("You lose " + player + ", You win " + player1)
    game = "lose"
  elif playerselect == "scissors" and playerselect1 == "paper":
    print("You win " + player + ", You lose " + player1)
    game = "win"
  else:
    print("It's a tie")
    game = "tie"
  return game

numberofplayers = startgame()
loop = "y"

if numberofplayers == 2:
  player = input("What is your name player 1?\n")
  player1 = input("What is your player 2?\n")
else:
  player = input("Whats your name?\n")
  player1 = ("CPU")
  
while loop.lower()  in ["yes", "y"]:
  #Se restablecen los contadores a 0
  winsplayer = 0
  winsplayer1 = 0
  tie_count = 0
  totalrounds = int(rounds()) #Se recibe el numero total de rondas a jugar
  clear_terminal()
  for n in range(0, totalrounds): #bucle incremental que se repite el numero de rondas a jugar
    print("Round " + str(n + 1)) #imprime el numero de ronda
    results = match(numberofplayers, player, player1) #Se ejecuta la funcion match que dara lugar a la partida
  if results == "tie":
    print ("its a tie")
    tie_count += +1
  if results == "win":
    winsplayer += 1
  if results == "lose":
    winsplayer1 += 1

#Limpia el panel y muestra los contadores
  clear_terminal()
  print("Total tie rounds:", tie_count)
  print("Total wins rounds for:", player,winsplayer)
  print("Total wins rounds for:", player1, winsplayer1)
  if winsplayer > winsplayer1:
    print("The winner is:", player)
  elif winsplayer < winsplayer1:
    print("The winner is:", player1)
  loop = input("Do you want to play again? (yes/no)\n")
  if loop.lower() in ["yes", "y"]:
    loop = "yes"
    clear_terminal()
  else:
    clear_terminal()
    loop = "no"
    print("Great game, see you soon!")
