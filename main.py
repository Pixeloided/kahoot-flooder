from tkinter import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

idplc = '  Kahoot ID'
nameplc = '  Name of bots'
countplc = '  Number of bots'

def btn_clicked():
    a = 0
    botNumber = 0
    gamePin = str(kahootId.get())
    botNamed = str(botName.get())
    botAmount = int(botCount.get())

    while a < botAmount:
        browser = webdriver.Chrome(ChromeDriverManager().install())
        a += 1
        botNumber += 1
        botNamer = f"{botNamed}{botNumber}"
        browser.get("https://kahoot.it")
        browser.find_element_by_id("game-input").send_keys(gamePin)
        browser.find_element_by_id("game-input").send_keys(Keys.RETURN)

        time.sleep(1)
        try:
            browser.find_element_by_id("nickname").send_keys(botNamer)
            browser.find_element_by_id("nickname").send_keys(Keys.RETURN)

        except:
            browser.find_element_by_xpath('//*[@id="root"]/div[1]/div[2]/div/div[2]/button').click()
            time.sleep(3)
            browser.find_element_by_xpath('//*[@id="root"]/div[1]/div[2]/div/div[2]/button[2]').click()


def eraseId(event=None):
    if kahootId.get() == idplc:
        kahootId.delete(0,'end')
def addId(event=None):
    if kahootId.get() == '':
        kahootId.insert(0,idplc)

def eraseName(event=None):
    if botName.get() == nameplc:
        botName.delete(0,'end')
def addName(event=None):
    if botName.get() == '':
        botName.insert(0,nameplc)

def eraseCount(event=None):
    if botCount.get() == countplc:
        botCount.delete(0,'end')
def addCount(event=None):
    if botCount.get() == '':
        botCount.insert(0,countplc)


def addAll():
    addId()
    addName()
    addCount()

window = Tk()

window.geometry("720x512")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 512,
    width = 720,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    184.0, 303.0,
    image=background_img)

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    515.0, 168.5,
    image = entry0_img)

kahootId = Entry(
    bd = 0,
    bg = "#dddddd",
    highlightthickness = 0)

kahootId.place(
    x = 332, y = 152,
    width = 366,
    height = 31)

canvas.create_text(
    304.5, 90.0,
    text = "Kahoot flooder",
    fill = "#000000",
    font = ("Calibri", int(57.0)))

entry1_img = PhotoImage(file = f"img_textBox1.png")
entry1_bg = canvas.create_image(
    515.0, 227.0,
    image = entry1_img)

botName = Entry(
    bd = 0,
    bg = "#dddddd",
    highlightthickness = 0)

botName.place(
    x = 332, y = 211,
    width = 366,
    height = 30)

entry2_img = PhotoImage(file = f"img_textBox2.png")
entry2_bg = canvas.create_image(
    515.0, 291.5,
    image = entry2_img)

botCount = Entry(
    bd = 0,
    bg = "#dddddd",
    highlightthickness = 0)

botCount.place(
    x = 332, y = 275,
    width = 366,
    height = 31)

buttonsrc = PhotoImage(file = f"buttonsrc.png")
b0 = Button(
    image = buttonsrc,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 332, y = 372,
    width = 366,
    height = 32)

addAll()

kahootId.bind('<FocusIn>',eraseId)
kahootId.bind('<FocusOut>',addId)

botName.bind('<FocusIn>',eraseName)
botName.bind('<FocusOut>',addName)

botCount.bind('<FocusIn>',eraseCount)
botCount.bind('<FocusOut>',addCount)

window.title("Kahoot flooder")
window.iconbitmap("icon.ico")
window.resizable(False, False)
window.mainloop()