import pyautogui as df
from time import sleep


df.doubleClick(632, 1073, duration=5)

sleep(5)

df.moveTo(187, 65, duration=5)
df.click(187, 65)
sleep(3)
df.typewrite("https://youtube.com")
df.typewrite(["enter"])
