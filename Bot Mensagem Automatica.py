# Por: Akinori Koerich
# GitHub: https://github.com/AkinoriKoerich
# Programa elaborado para fins educacionais.


# importando as bibliotecas
import PySimpleGUI as sg
import pyautogui
import time

# criando o layout
layout = [[sg.Text('Navegador'), sg.InputText(size=(20, 1))],
          [sg.Text('Contato'), sg.InputText(size=(20, 1))],
          [sg.Text('Mensagem'), sg.InputText(size=(20, 1))],
          [sg.Button('Revisar'), sg.Button('Enviar')]]

# criando a janela
window = sg.Window('Bot Mensagem', layout)

# criando a leitura de eventos
while True:
    event, values = window.read()
    if event in (None, 'Enviar'):
        break
    elif event == 'Revisar':
        if values is not None:
            valor1 = values[0] # criando variaveis separadas e printando elas
            valor2 = values[1]
            valor3 = values[2]
            sg.popup(f'Navegador: {valor1}\nContato: {valor2}\nMensagem: {valor3}')

window.close()


# abrir a ferramenta/o sistema
pyautogui.press("win")
time.sleep(1.3)
pyautogui.write(valor1)
time.sleep(1.3)
pyautogui.press("enter")
time.sleep(4)

# localizar o alvo desejado
pyautogui.write("web.whatsapp.com")
pyautogui.press("Enter")
time.sleep(5)

# localizar o contato escolhido
pyautogui.press('Tab')
pyautogui.press('Tab')
pyautogui.press('Tab')
pyautogui.press('Tab')
pyautogui.press('Tab')
pyautogui.write(valor2)
time.sleep(1.3)
pyautogui.press('enter')

# digitar a mensagem
pyautogui.write(valor3)
pyautogui.press('enter')



