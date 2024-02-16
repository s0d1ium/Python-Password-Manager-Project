import PySimpleGUI as sg
from Encrypt import Operations
from cryptography.fernet import Fernet
import json

# Theme
sg.theme('Black')


def keywarning():

    # User Interface Layout
    layout = [
        [sg.Text('This is a warning!', font=('Arial', 12))],
        [sg.Text(
            'Creating a new key removes the old key resulting in the current data being undecryptable, do you wish to continue?',
            font=('Arial', 10))],
        [sg.Button('Confirm'), sg.Button('Cancel')]
    ]

    # Initialise window
    window = sg.Window('Warning', layout, modal=True)

    # Event loop
    while True:

        # Listen and read events and values from the window
        event, _ = window.read()

        # Close window
        if event == sg.WINDOW_CLOSED or event == 'Cancel':
            break

        # "Confirm" button pressed
        if event == 'Confirm':

            # Write new key function/ Overwrite current key
            Operations.write_new_key()
            break

    window.close()


def credwarning():

    # User Interface Layout
    layout = [
        [sg.Text('This is a warning!', font=('Arial', 12))],
        [sg.Text('Clearning stored credentials cannot be undone, do you wish to continue?', font=('Arial', 10))],
        [sg.Button('Confirm'), sg.Button('Cancel')]
    ]

    # Initialise window
    window = sg.Window('Warning', layout, modal=True)

    # Event loop
    while True:

        # Listen and read events and values from the window
        event, _ = window.read()

        # Close window
        if event == sg.WINDOW_CLOSED or event == 'Cancel':
            break

        # "Confirm" button pressed
        if event == 'Confirm':

            # Overwrite current storage file
            Operations.write_new_storage()
            break

    window.close()


def Settings_screen():

    # User Interface Layout
    layout = [
        [sg.Button('Create new key', size=(10, 2))],
        [sg.Button('Clear stored credentials', size=(10, 2))],
        [sg.Text('Password', size=(10, 1)), sg.InputText(key='password')],
        [sg.Button('Submit')],
        [sg.Button('Close')]
    ]

    # Initialise window
    window = sg.Window('Settings', layout, element_justification='center', modal=True, size=(300, 200))

    # Event loop
    while True:

        # Listen and read events and values from the window
        event, values = window.read()

        # Close window
        if event == sg.WINDOW_CLOSED or event == 'Close':
            break

        # "Clear stored credentials" button pressed
        if event == 'Clear stored credentials':

            # Warning screen
            credwarning()

        # "Create new key" button pressed
        if event == 'Create new key':

            # Warning screen
            keywarning()

        # "Submit" button pressed
        if event == 'Submit':

            # Hash password and save result to file
            Operations.set_new_pass_hash(values['password'])

            # Confirmation popup
            sg.popup("New password set.")

    window.close()


def Decryption_screen(decrypted):

    # Removing characters for display purposes
    decryptedFormatted = [
        [str(item).replace('[', '').replace(']', '').replace('"', '').replace("b'", "").replace("'", '') for item in
         row] for row in decrypted]

    # Create a layout to display the 2D array in a window
    layout = [
        [sg.Table(values=decryptedFormatted, headings=['Platform', 'Username', 'Password'], auto_size_columns=True,
                  display_row_numbers=False, justification='center')],
        [sg.Button('Cancel')]
    ]

    # Create the window
    window = sg.Window('Decrypted data display', layout, modal=True)

    # Event loop
    while True:

        # Listen and read events and values from the window
        event, _ = window.read()

        # Close window
        if event == sg.WINDOW_CLOSED or event == 'Cancel':
            break
    window.close()


def Encryption_screen():
    layout = [
        [sg.Text('Platform', size=(10, 1)), sg.InputText(key='platform')],
        [sg.Text('Username', size=(10, 1)), sg.InputText(key='username')],
        [sg.Text('Password', size=(10, 1)), sg.InputText(key='password')],
        [sg.Button('Submit'), sg.Button('Cancel')]
    ]

    window = sg.Window('Login Information', layout, modal=True)  # Use modal=True for a modal window

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == 'Cancel':
            break

        # "Submit" button pressed
        elif event == 'Submit':
            platform = values['platform']
            username = values['username']
            password = values['password']

            # Debug
            print(f"Platform: {platform}, Username: {username}, Password: {password}")
            Operations(platform, username, password).encrypt()
            break

    # Close window
    window.close()

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

def main_screen():

    # User Interface Layout
    button_layout = [
        [sg.Button('Encrypt', size=(10, 1))],
        [sg.Button('Decrypt', size=(10, 1))],
        [sg.Button('Edit', size=(10, 1))],
        [sg.Button('Generate Password', size=(10, 1))],
        [sg.Button('Settings', size=(10, 1))]
    ]

    # User Interface Layout
    layout = [
        [sg.Stretch(), sg.Frame('', button_layout, pad=(0, 0), vertical_alignment='center'), sg.Stretch()],
        [sg.Button('Close')]
    ]

    # Initialisation fo window
    window = sg.Window('Password Manager', layout, size=(300, 200))

    # Event loop
    while True:

        # Listen and read events and values from the window
        event, values = window.read()

        # Close window
        if event == sg.WINDOW_CLOSED or event == 'Close':
            break

        # "Encrypt" button is pressed
        if event == 'Encrypt':

            # Open encryption window
            Encryption_screen()

        # "Decrypt" button is pressed
        if event == 'Decrypt':

            # Decryption function outputted to array
            data = Operations.Decrypt()

            # Open decryption screen with decrypted array as parameter
            Decryption_screen(data)

        # "Settings" button is pressed
        if event == 'Settings':

            # Open settings screen
            Settings_screen()

        if event == 'Generate Password':
            Password_length()


def login():

    # User Interface Layout
    layout = [
        [sg.Text('Enter Password:'), sg.InputText(password_char='*')],
        [sg.Button('Login'), sg.Button('Cancel')]
    ]

    # Initialisation of window
    window = sg.Window('Password Login', layout)

    # Max password attempts
    max_attempts = 3

    # Current attempts variable
    attempts = 0

    # Event loop
    while True:

        # Listen and read events and values from the window
        event, values = window.read()

        # Close window
        if event == sg.WINDOW_CLOSED or event == 'Cancel' or attempts >= max_attempts:
            break

        # Login button is pressed and password is hashed and compared to the hash stored in a file
        elif event == 'Login' and Operations.check_pass_hash(values[0]) == True:

            # Close current window
            window.close()

            # Initialise main window
            main_screen()
            break

        # If hash comparison outputted false
        elif Operations.check_pass_hash(values[0]) == False:

            # Increment attempts count
            attempts += 1

            # calculate remaining attempts
            remaining_attempts = max_attempts - attempts

            # loop while remaining attempts is larger than 0
            if remaining_attempts > 0:

                # remaining attempts popup
                sg.popup(f'Incorrect password! {remaining_attempts} attempts remaining. Try again.')
            else:

                # Popup before exiting program
                sg.popup('Maximum attempts reached. Login failed.')
                break

    window.close()


if Operations.check_count_is_0() == True:
    sg.popup("RECOMMENDED: Set a password in settings")
    main_screen()
else:
    login()
