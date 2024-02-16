import PySimpleGUI as sg
import json

def save_settings(settings):
    with open('config.json', 'w') as file:
        json.dump(settings, file)

def load_settings():
    try:
        with open('config.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {'username': '', 'email': '', 'notifications': False}

def settings_window(settings):
    layout = [
        [sg.Text('Settings', font=('Helvetica', 16))],
        [sg.Text('Username'), sg.InputText(key='username', default_text=settings['username'])],
        [sg.Text('Email'), sg.InputText(key='email', default_text=settings['email'])],
        [sg.Checkbox('Enable Notifications', key='notifications', default=settings['notifications'])],
        [sg.Button('Save'), sg.Button('Cancel')]
    ]

    window = sg.Window('Settings', layout)

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == 'Cancel':
            break
        elif event == 'Save':
            settings['username'] = values['username']
            settings['email'] = values['email']
            settings['notifications'] = values['notifications']
            save_settings(settings)
            sg.popup('Settings saved!')

    window.close()

def main():
    sg.theme('LightGrey1')
    settings = load_settings()

    layout = [
        [sg.Text(f'Username: {settings["username"]}')],
        [sg.Text(f'Email: {settings["email"]}')],
        [sg.Text(f'Notifications: {"Enabled" if settings["notifications"] else "Disabled"}')],
        [sg.Button('Settings'), sg.Button('Exit')]
    ]

    window = sg.Window('PySimpleGUI Settings Menu', layout)

    while True:
        event, _ = window.read()

        if event == sg.WINDOW_CLOSED or event == 'Exit':
            break
        elif event == 'Settings':
            settings_window(settings)

    window.close()

if __name__ == '__main__':
    main()