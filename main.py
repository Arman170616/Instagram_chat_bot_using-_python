from time import sleep
from numpy import Infinity
import pyautogui as pt
import pyperclip as pc


sleep(2)


def move_to_text_input(message):
    position = pt.locateOnScreen('image/insta_image.png', confidence=.7)
    pt.moveTo(position[0:2], duration=0.5)
    pt.moveRel(-100, 20, duration=.5)
    pt.doubleClick(interval=0.3)
    pt.typewrite(message, interval=0.01)
    pt.typewrite('\n')

# handle message retrival
#move_to_text_input('hello, this is dammy message')


def get_message():
    position = pt.locateOnScreen('image/insta_smile.png', confidence=.9)
    pt.moveTo(position[0:2], duration=0.5)
    pt.moveRel(50, -50, duration=0.5)
    pt.click()

    # click on triple dots
    position = pt.locateOnScreen('image/triple_dot.png', confidence=.8)
    pt.moveTo(position[0:2], duration=0.5)
    pt.click()

    # click on copy message
    position = pt.locateOnScreen('image/insta_copy.png', confidence=.8)
    pt.moveTo(position[0] + 10, position[1] + 15,  duration=0.5)
    pt.click()

    user_text = pc.paste()
    return user_text


# process your response

def process_message(message):
    msg = str(message).lower()

    if msg == 'hello':
        return 'Go Away!'
    elif msg == 'sup':
        return 'Hello Iansta!'
    elif msg == 'how are you?':
        return 'How about you mind your own business?'
    else:
        return 'That is nonsense!'

# the programme......


last_massege, last_response = '', ''


def insta_chatbot():
    global last_massege, last_response

    # Checks whether the message copied is the same as the last one
    current_message = get_message()

    if current_message != last_massege:
        last_massege = current_message
        print(f'Last copied message: {current_message}')

        # Bot response

        if current_message != last_massege:
            response = process_message(current_message)
            last_response = response
            print(f'Bot: {response}')
            move_to_text_input(response)
    else:
        print('No New Messages.....')

# Infinite loop for the bot to run


while True:
    try:
        insta_chatbot()
        sleep(10)

    except Exception as e:
        print(f'Exception: {e}')
        sleep(10)
