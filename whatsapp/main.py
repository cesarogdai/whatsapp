from time import sleep
import pyautogui as pt
import pyperclip as pc
from pynput.mouse import Button, Controller

normal = ['Ahhh no sabia', 'Oye', 'Claro que si', 'Lo que mejor te parezca', 'Si estas de acuerdo', 'Estoy de acuerdo', 'HAHAHAHHAHAHAHA']
common = ['Hola', 'Prueba', 'Tu lo sabes', 'Cuentame mas']
questions = ['Tu que dices?', 'Estas de acuerdo?']
pt.FAILSAFE = True
mouse = Controller()

#Nav to any image
def nav_to_image(image, clicks, off_x=0, off_y=0):
    position = pt.locateCenterOnScreen(image,confidence=.7)

    if position is None:
        print(f'{image} not found...')
        return 0
    else:
        pt.moveTo(position, duration=.5)
        pt.moveRel(off_x, off_y, duration=.2)
        pt.click(clicks=clicks, interval=.1)

#go from the code to whatsapp
#sleep(5)


def get_message():
    nav_to_image('python/whatsapp/images/paper.png', 0, off_y=-75)
    mouse.click(Button.left, 3)
    pt.rightClick()

    copy = nav_to_image('python/whatsapp/images/real.png', 1)
    return pc.paste() if copy != 0 else 0

def close_reply_box():
    nav_to_image('python/whatsapp/images/x.png', 2)


def send_message(msg):
    nav_to_image('python/whatsapp/images/paper.png', 2, off_x=100)
    pt.typewrite(msg, interval=.1)
    pt.typewrite('\n')

def process_message(msg):
   raw_msg = msg.lower()

   if raw_msg == 'hola':
       return 'Holaaaa'
   elif raw_msg in 'hay clases':
       return 'No gracias'
   elif raw_msg in 'tenems tarea':
       return 'No gracias'
   elif raw_msg in 'hagamos un meet':
       return 'Va'
   if raw_msg == 'Oye':
       return 'Si dime'
   elif raw_msg in 'Puedes hablar?':
       return 'Claro '
   elif raw_msg in common:
       if True in list(map(lambda ms: msg in ms, common)):
           return msg
       return 'No gracias'
   elif raw_msg in 'hagamos un meet':
       return 'Va'
   else:
       return 'Disculpa, no te entendi, podrias decirlo de otra forma??' 

#Ciclar
delay = 10
last_message = ''

sleep(3)

while True:
    nav_to_image('python/whatsapp/images/dot.png', 2, off_x=-100) #1
    close_reply_box() #2

    message = get_message() #3
    if message != 0  and message != last_message:
        last_message = message
        send_message(process_message(message))
    else:
        print("Todo igual")
    sleep(10)