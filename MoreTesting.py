import PySimpleGUI as sg
from Encrypt import Operations

text_to_display = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
"""

def Password_length():
    layout = [
        [sg.Text('Length', size=(10, 1)), sg.InputText(key='length')],
        [sg.Button('Generate Password'), sg.Button('Cancel')]
    ]

    window = sg.Window('Login Information', layout, modal=True)  # Use modal=True for a modal window

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == 'Cancel':
            break
        elif event == 'Generate Password':
            password = Operations.Generate_Password(int(values['length']))
            Password_display(password)
    window.close()

def Password_display(password):
    layout = [
        [sg.Text(password, size=(60, 10), key='-TEXT-OUT-', enable_events=True)],
        [sg.Button('Exit'), sg.Button('Copy to clipboard')]
    ]

    window = sg.Window('Password Display', layout, modal=True)

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == 'Exit':
            break
        elif event == 'Copy to clipboard':
            sg.clipboard_set(password)
            sg.Popup("Copied to clipboard")

    window.close()

Password_length()