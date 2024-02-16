import PySimpleGUI as sg


def main_screen():
    # Define button layout with larger buttons and empty labels
    button_layout = [
        [sg.Button('Encrypt', size=(10, 2)), sg.Button('Decrypt', size=(10, 2))],
        [sg.Button('Edit', size=(10, 2)), sg.Button('Settings', size=(10, 2))]
    ]

    # Create layout with frame and vertical alignment
    layout = [
        [sg.Text('Welcome', font=('Arial', 14))],
        [sg.Stretch(), sg.Frame('', button_layout, pad=(0, 0), vertical_alignment='center'), sg.Stretch()]
    ]

    # Create window
    window = sg.Window('Password Manager', layout, size=(300, 200))

    # Event loop
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:
            break

def login():

    sg.theme('DarkGrey12')
    # Define the layout of your window
    layout = [
        [sg.Text('Enter Password:'), sg.InputText(password_char='*')],
        [sg.Button('Login'), sg.Button('Cancel')]
    ]

    # Create the window
    window = sg.Window('Password Login', layout)

    # Set a limit to the number of password attempts
    max_attempts = 3
    attempts = 0

    # Event loop
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == 'Cancel' or attempts >= max_attempts:
            break
        elif event == 'Login' and values[0] == 'mypassword':  # Replace 'mypassword' with your actual password
            window.close()
            main_screen()
            break
        else:
            attempts += 1
            remaining_attempts = max_attempts - attempts
            if remaining_attempts > 0:
                sg.popup(f'Incorrect password! {remaining_attempts} attempts remaining. Try again.')
            else:
                sg.popup('Maximum attempts reached. Login failed.')
                break

    # Close the window
    window.close()

login()