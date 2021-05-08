import pyautogui as pt
from time import sleep
import pyperclip
import random

sleep(3)

position1 = pt.locateOnScreen("smiley.png ", confidence=.8)
x = position1[0]
y = position1[1]


# Gets message
def get_message():
    global x, y

    position = pt.locateOnScreen("smiley.png", confidence=.8)
    x = position1[0]
    y = position1[1]
    pt.moveTo(x, y, duration=.5)
    pt.moveTo(x + 120, y - 40, duration=.5)
    pt.tripleClick()
    pt.moveRel(12, 0)
    pt.rightClick()
    pt.moveRel(15, 15)
    pt.click()
    whatsapp_messages = pyperclip.paste()
    pt.click()
    print("Message received: " + whatsapp_messages)

    return whatsapp_messages


# Posts
def post_response(message):
    global x, y
    position = pt.locateOnScreen("smiley.png", confidence=.8)
    x = position1[0]
    y = position1[1]
    pt.moveTo(x, y, duration=.5)
    pt.moveTo(x + 200, y + 20, duration=.5)
    pt.click()
    pt.typewrite(message, interval=.01)

    pt.typewrite("\n", interval=.01)


# post_response(get_message())

# Process response
def process_response(message):
    random_no = random.randrange(3)

    if "vaccine" in str(message).lower():
        return "Please goto this site for more information www.cowin.gov.in"

    elif "test" in str(message).lower():
        return "Please goto this site for more information www.covid.icmr.org.in"

    elif "regist" in str(message).lower():
        return "Please goto this site for more information www.cowin.gov.in"

    elif "help" in str(message).lower():
        return "Please goto this site for more information www.mygov.in/covid-19/"

    elif "ambulance" in str(message).lower():
        return "Please goto this site for more information www.emri.in"

    elif "oxygen" in str(message).lower():
        return "Please goto this site for more information www.mohfw.gov.in"

    elif "hospital" in str(message).lower():
        return "Please goto this site for more information www.nhp.gov.in"

    else:
        return "Please enter the COVID related problems "


processed_message = process_response(get_message())
post_response(processed_message)





"""""
# Check for new messages
def check_for_new_messages():
    pt.moveTo(x + 125, y - 40, duration=.5)

    while True:
        # Continuously checks for green dot and new messages
        try:
            position = pt.locateOnScreen("green.png", confidence=.7)

            if position is not None:
                pt.moveTo(position)
                pt.moveRel(-100, 0)
                pt.click()
                sleep(.5)
        except(Exception):
            print("No new messages")
        if pt.pixelMatchesColor(int(x + 50), int(y - 35), (255, 255, 255), tolerance=10):
            print("is white")
            processed_message = process_response(get_message())
            post_response(processed_message)
        else:
            print("No new messages yet...")
        sleep(10)
        
check_for_new_messages()
"""""


