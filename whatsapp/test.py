common = ['Hola', 'Prueba', 'Tu lo sabes', 'Cuentame mas']
questions = ['Tu que dices?', 'Estas de acuerdo?']
mess = input("Ingresa el mensaje")

def send(message):
    if True in list(map(lambda ms : mess in ms, common)):
        print(message)

send(mess)
