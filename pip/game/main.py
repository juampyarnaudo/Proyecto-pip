import random

options = ('piedra', 'papel', 'tijera')

computer_wins = 0
user_wins = 0
rounds = 1

while True:
  print('*' * 15)
  print('ROUND: ', rounds)
  print('*' * 15)
  user_option = input('piedra, papel o tijera => ')
  #transformo el texto ingresado a minusculas
  user_option = user_option.lower()

  if not user_option in options:
    print('esa opción no es valida')
    #de esta forma ignora toda la logica de abajo
    continue

  #con el .choice le decimos que elija alguna de las opciones que ponemos en (options)
  computer_option = random.choice(options)

  print('User option => ', user_option)
  print('Computer option => ', computer_option)

  if (user_option == computer_option):
    print('Empate')
  elif user_option == 'piedra':
    if computer_option == 'tijera':
      print('Ganaste!')
      print('felicitaciones')
      user_wins += 1
    else:
      print('Computadora gana')
      print('vuelve a intentarlo')
      computer_wins += 1
  elif user_option == 'papel':
    if computer_option == 'piedra':
      print('Ganaste!')
      print('felicitaciones')
      user_wins += 1
    else:
      print('Computadora gana')
      print('vuelve a intentarlo')
      computer_wins += 1
  elif user_option == 'tijera':
    if computer_option == 'papel':
      print('Ganaste!')
      print('felicitaciones')
      user_wins += 1
    else:
      print('Computadora gana')
      print('vuelve a intentarlo')
      computer_wins += 1
    
  if computer_wins == 2:
      print('El ganardor es la computadora')
      break
  if user_wins == 2:
      print('El ganardor fuiste tu!')
      break
  rounds +=1
