import PySimpleGUI as sg
import pyautogui as ag
sg.theme('Black')
layout = [
    [sg.Text('Welcome to autowriter')],
    [sg.Text('Text', size=(15, 1)), sg.InputText()],
    [sg.Text('Times', size=(15, 1)), sg.InputText()],
    [sg.Text('Delay after launch', size=(15, 1)), sg.InputText()],
    [sg.Submit(), sg.Cancel()]
]
window = sg.Window('AutoWriter', layout)
event, values = window.read()
import time
def files():
    l = open("x.txt","w")
    l.write(values[0])
    l.close()
def type():
    time.sleep(float(values[2]))
    for i in range(int(values[1])):
        ag.write(values[0])
        ag.press("enter")
files()
type()
