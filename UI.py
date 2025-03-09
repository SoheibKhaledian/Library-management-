import PySimpleGUI as sg
from userClass import User
from bockClass import Bock


sg.theme('Purple')


def log_in_form():
    layout = [
        [sg.Text("Welcome to the Application", font=("Helvetica", 16), justification='center', pad=(0, 10))],
        [sg.Text("Please enter your information or create an account.", font=("Helvetica", 12), pad=(0, 20))],
        [sg.Text('ID:', size=(10, 1), justification='right'), sg.Input(key='id', size=(30, 1))],
        [sg.Text('Password:', size=(10, 1), justification='right'),
         sg.Input(key='pas', password_char='*', size=(30, 1))],
        [sg.Button('Log In', size=(10, 1), button_color=('white', 'green')),
         sg.Button('Sign Up', size=(10, 1), button_color=('white', 'blue')),
         sg.Button('Exit', size=(10, 1), button_color=('white', 'red'))]
    ]

    window = sg.Window('Log in', layout=layout)

    while True:
        event, values = window.read()

        if event in (sg.WIN_CLOSED, 'Exit'):
            break

        elif event == 'Log In':
            if values['id'] is None or values['pas'] is None:
                sg.popup('enter informtion then click log in')
            else:
                user = User.user_identification(int(values['id']), values['pas'])

                if user is None:
                    sg.popup("the password or id is wrong, please try agine litter \n   if you don't have account crate one")
                else:
                    if user.access == 0:
                        window.close()
                        user_panel(user)

                    if user.access == 1:
                        window.close()
                        admain_form(user)

        elif event == 'Sign Up':
            window.close()
            sign_up_form()


def sign_up_form():
    layout = [
        [sg.Text("Please Enter Your Information", font=("Helvetica", 16), justification='center', pad=(0, 10))],
        [sg.Text("Your Name:", size=(15, 1), justification='right'), sg.Input(size=(25, 1), key='name')],
        [sg.Text("Password:", size=(15, 1), justification='right'),
         sg.Input(size=(25, 1), password_char='*', key='pas')],
        [sg.Text("Confirm Password:", size=(15, 1), justification='right'),
         sg.Input(size=(25, 1), password_char='*', key='repas')],
        [sg.Button('Sign Up', size=(10, 1), button_color=('white', 'green')),
         sg.Button('Back', size=(10, 1), button_color=('white', 'blue')),
         sg.Button('Exit', size=(10, 1), button_color=('white', 'red'))]
    ]

    window = sg.Window('sign up', layout=layout)

    while True:
        event, values = window.read()

        if event in (sg.WIN_CLOSED, 'Exit'):
            window.close()
            break

        elif event == 'Sign Up':
            if len(values['pas']) < 8:
                sg.popup('the password must 8 digit or more')

            elif values['pas'] == values['repas'] and values['name'] is not None:
                result = User.add_user(values['name'], values['pas'])

                sg.popup(result[1])
                window.close()
                user_panel(result[0])

            else:
                sg.popup('enter informtion corctly')

        elif event == 'Back':
            window.close()
            log_in_form()


def user_panel(user):
    user_books = user.find_user_bock()
    user_exp = user.expiration()

    # print(f"{len(user_exp)}, {len(user_books)}")

    bock_data = []
    exp_data = []

    for i in user_books:
        bock_data.append([i[0].name, i[1], i[2]])

    for i in user_exp:
        exp_data.append([i[0].name, i[1]])

    layout = [
        [sg.Text(f"Welcome, {user.name}!", font=("Helvetica", 14), justification='left')],
        [sg.Button('Change Password or Name', size=(25, 1), button_color=('white', 'blue'))],
        [sg.Text('Search for a specific book:', font=("Helvetica", 12)), sg.Button('Search', size=(10, 1))],
        [sg.Button('Get a Book', size=(12, 1), button_color=('white', 'green')),
         sg.Button('Return Book', size=(12, 1), button_color=('white', 'orange'))],
        [sg.Text('Books currently borrowed:', font=("Helvetica", 12), pad=(0, 10))],
        [sg.Table(values=bock_data, headings=['Name', 'Borrowed Date', 'Return Date'],
                  auto_size_columns=False, justification='center',
                  col_widths=[20, 15, 15], num_rows=5, alternating_row_color='lightblue',
                  key='-bocks-', enable_events=True, tooltip="Books borrowed")],
        [sg.Text('Books overdue for return:', font=("Helvetica", 12), pad=(0, 10))],
        [sg.Table(values=exp_data, headings=['Name', 'Days Past Due'],
                  auto_size_columns=False, justification='center',
                  col_widths=[20, 10], num_rows=5, alternating_row_color='pink',
                  key='-expi-', enable_events=True, tooltip="Overdue books")],
        [sg.Button('Log Out', size=(10, 1), button_color=('white', 'red')),
         sg.Button('Exit', size=(10, 1), button_color=('white', 'gray'))]
    ]

    window = sg.Window('user panel', layout=layout)

    while True:
        event, values = window.read()

        if event in (sg.WIN_CLOSED, 'Exit'):
            break

        elif event == 'Search':
            search_form()

        elif event == 'Get a Book':
            deposit_form(user)

        elif event == 'Return Book':
            return_form(user)

        elif event == 'Change Password or Name':
            window.close()
            ch_form(user)

        elif event == 'Log Out':
            window.close()
            log_in_form()


def search_form():
    layout = [
        [sg.Text('Search for a Book:', font=("Helvetica", 12), justification='left')],
        [sg.Input(size=(30, 1), key='-INPUT-', tooltip="Enter your search term here"),
         sg.Button('By Name', size=(10, 1), button_color=('white', 'blue')),
         sg.Button('By Topic', size=(10, 1), button_color=('white', 'green')),
         sg.Button('By Author', size=(10, 1), button_color=('white', 'orange'))],
        [sg.Text('Search Results:', font=("Helvetica", 12), pad=(0, 10))],
        [sg.Table(values=[], headings=['Index', 'Name', 'Author', 'Topic'],
                  auto_size_columns=False, justification='center',
                  col_widths=[10, 20, 20, 20], num_rows=8, alternating_row_color='lightblue',
                  key='-TABLE-', tooltip="Results of your search will appear here")]
    ]

    window = sg.Window('search', layout=layout)

    while True:
        event, values = window.read()

        if event in (sg.WIN_CLOSED, 'Exit'):
            break

        elif event == 'By Name':
            bock = Bock.name_search(values['-INPUT-'].lower())

            if bock is None:
                sg.popup('no bock by this name was found')

            else:
                data = [[1, bock.name, bock.author, bock.topic]]

                window['-TABLE-'].update(values=data)

        elif event == 'By Topic':
            bocks = Bock.topic_search(values['-INPUT-'].lower())
            data = []

            if len(bocks) == 0:
                sg.popup('no bock was found in this topic')

            else:
                for i, bock in enumerate(bocks):
                    data.append([i+1, bock.name, bock.author, bock.topic])

                window['-TABLE-'].update(values=data)

        elif event == 'By Author':
            bocks = Bock.author_search(values['-INPUT-'].lower())
            data = []

            if len(bocks) == 0:
                sg.popup('no bock was found by this author')

            else:
                for i, bock in enumerate(bocks):
                    data.append([i, bock.name, bock.author, bock.topic])

                window['-TABLE-'].update(values=data)


def deposit_form(user):
    layout = [
        [sg.Text('Enter the Book Name:', font=("Helvetica", 12), pad=(10, 10))],
        [sg.Input(size=(30, 1), key='name', tooltip="Type the book name here")],
        [sg.Button('OK', size=(10, 1), button_color=('white', 'green')),
         sg.Button('Back', size=(10, 1), button_color=('white', 'blue'))]
    ]

    window = sg.Window('get', layout=layout)

    while True:
        event, values = window.read()

        if event in (sg.WIN_CLOSED, 'Back'):
            window.close()
            break

        elif event == 'OK':
            bock = Bock.name_search(values['name'].lower())

            if bock is None:
                sg.Popup('the bock is not found')

            else:
                sg.Popup(user.make_deposit(bock))


def return_form(user):
    layout = [
        [sg.Text('Enter Book Name:', font=("Helvetica", 14), justification='left', pad=(5, 10))],
        [sg.Input(size=(30, 1), key='name', tooltip="Type the book name here")],
        [sg.Button('OK', size=(12, 1), button_color=('white', 'green'), pad=(5, 10)),
         sg.Button('Back', size=(12, 1), button_color=('white', 'red'), pad=(5, 10))]
    ]

    window = sg.Window('return', layout=layout)

    while True:
        event, values = window.read()

        if event in (sg.WIN_CLOSED, 'Back'):
            window.close()
            break

        elif event == 'OK':
            bock = Bock.name_search(values['name'].lower())

            if bock is None:
                sg.Popup('the bock is not found')

            else:
                sg.Popup(user.make_return(bock))


def ch_form(user):
    layout = [
        [sg.Text("Please Enter Your Information", font=("Helvetica", 16), justification='center', pad=(0, 20))],
        [sg.Text("Your Name:", size=(15, 1)), sg.Input(size=(20, 1), key='name', tooltip="Enter your name"),
         sg.Button('Change Name', size=(12, 1), button_color=('white', 'blue'))],
        [sg.Text("Password:", size=(15, 1)),
         sg.Input(size=(20, 1), password_char='*', key='pas', tooltip="Enter your password")],
        [sg.Text("Confirm Password:", size=(15, 1)),
         sg.Input(size=(20, 1), password_char='*', key='repas', tooltip="Re-enter your password")],
        [sg.Button('Change Password', size=(15, 1), button_color=('white', 'green')),
         sg.Button('Back', size=(10, 1), button_color=('white', 'red'))]
    ]

    window = sg.Window('change informtion', layout=layout)

    while True:
        event, values = window.read()

        if event in (sg.WIN_CLOSED, 'Back'):
            window.close()
            user_panel(user)
            break

        elif event == 'Change Name':
            sg.Popup(User.change_name(user, values['name']))

        elif event == 'Change Password':
            if len(values['pas']) < 8:
                sg.popup('the password must 8 digit or more')

            elif values['pas'] == values['repas']:
                sg.Popup(User.change_pas(user, values['pas']))


def ach_form(user):
    layout = [
        [sg.Text("Please Enter Your Information", font=("Helvetica", 16), justification='center', pad=(0, 20))],
        [sg.Text("Your Name:", size=(15, 1)), sg.Input(size=(20, 1), key='name', tooltip="Enter your name"),
         sg.Button('Change Name', size=(12, 1), button_color=('white', 'blue'))],
        [sg.Text("Password:", size=(15, 1)),
         sg.Input(size=(20, 1), password_char='*', key='pas', tooltip="Enter your password")],
        [sg.Text("Confirm Password:", size=(15, 1)),
         sg.Input(size=(20, 1), password_char='*', key='repas', tooltip="Re-enter your password")],
        [sg.Button('Change Password', size=(15, 1), button_color=('white', 'green')),
         sg.Button('Back', size=(10, 1), button_color=('white', 'red'))]
    ]

    window = sg.Window('change informtion', layout=layout)

    while True:
        event, values = window.read()

        if event in (sg.WIN_CLOSED, 'Back'):
            window.close()
            admain_form(user)
            break

        elif event == 'Change Name':
            sg.Popup(User.change_name(user, values['name']))

        elif event == 'Change Password':
            if len(values['pas']) < 8:
                sg.popup('the password must 8 digit or more')

            elif values['pas'] == values['repas']:
                sg.Popup(User.change_pas(user, values['pas']))


def admain_form(user):
    layout = [
        [sg.Text(f"Welcome, {user.name}!", font=("Helvetica", 14), justification='left', pad=(5, 10)),
         sg.Button('Change Password or Name', size=(20, 1), button_color=('white', 'blue'))],

        [sg.Text("Search for Book Information:", size=(30, 1)),
         sg.Button('Search', size=(10, 1), button_color=('white', 'green'))],

        [sg.Text("Modify Book Collection:", size=(30, 1)),
         sg.Button('Add New Book', size=(15, 1), button_color=('white', 'orange'))],

        [sg.Text("Name of the Book to Delete:", size=(30, 1)),
         sg.Input(size=(20, 1), key='Dname', tooltip="Enter the book name"),
         sg.Button('Delete', size=(10, 1), button_color=('white', 'red'))],

        [sg.Text("Reports:", font=("Helvetica", 12), pad=(0, 10))],

        [sg.Button('User Favorite Book', size=(20, 1), button_color=('white', 'purple')),
         sg.Button('Book Report', size=(15, 1), button_color=('white', 'purple'))],

        [sg.Button('Log Out', size=(10, 1), button_color=('white', 'gray')),
         sg.Button('Exit', size=(10, 1), button_color=('white', 'gray'))]
    ]

    window = sg.Window('admin :)', layout=layout)

    while True:
        event, values = window.read()

        if event in (sg.WIN_CLOSED, 'Exit'):
            window.close()
            break

        elif event == 'Search':
            search_form()

        elif event == 'Add New Book':
            add_bock(user)

        elif event == 'Delete':
            if values['Dname'] is not None:
                sg.popup(Bock.delete_bock(values['Dname'].lower()))
            else:
                sg.popup('the name must be some thing')

        elif event == 'Log Out':
            window.close()
            log_in_form()

        elif event == 'User Favorite Book':
            favorite_report(user)

        elif event == 'Book Report':
            bock_report(user)

        elif event == 'Change Password or Name':
            window.close()
            sg.popup(ch_form(user))


def add_bock(user):
    layout = [
        [sg.Text('bock name:'), sg.Input(key='name')],
        [sg.Text('bock author:'), sg.Input(key='author')],
        [sg.Text('bock topic:'), sg.Input(key='topic')],
        [sg.Text('number of the bock:'), sg.Input(key='total')],
        [sg.Button('add'), sg.Button('Back')]
    ]

    window = sg.Window('add bock', layout=layout)

    while True:
        event, values = window.read()

        if event in (sg.WIN_CLOSED, 'Back'):
            window.close()
            admain_form(user)
            break

        elif event == 'add':
            sg.popup(Bock.add_bock(values['name'].lower(), values['author'].lower(), values['topic'].lower(), values['total']))


def favorite_report(user):
    layout = [
        [sg.Text('Enter User ID:', font=("Helvetica", 14), justification='left', pad=(5, 10))],
        [sg.Input(size=(30, 1), key='id', tooltip="Enter the user ID here")],
        [sg.Button('Search', size=(12, 1), button_color=('white', 'green')),
         sg.Button('Back', size=(12, 1), button_color=('white', 'red'))]
    ]

    window = sg.Window('user favorite', layout=layout)

    while True:
        event, values = window.read()

        if event in (sg.WIN_CLOSED, 'Back'):
            window.close()
            break

        if event == 'Search':
            if values['id'] is None:
                sg.popup("the id can't be None")

            else:
                sg.popup(User.favorite(int(values['id'])))


def bock_report(user):
    bocks = Bock.all_deposit_bock() or []

    layout = [
        [sg.Text('Book Information', font=("Helvetica", 16), justification='center', pad=(10, 10))],
        [sg.Table(values=bocks, headings=['Name', 'Get Data', 'Expiration Data', 'Return Data'],
                  auto_size_columns=False, justification='center',
                  col_widths=[15, 10, 15, 15], num_rows=10, alternating_row_color='lightblue',
                  key='-bocks-', row_height=30,
                  hide_vertical_scroll=True, vertical_scroll_only=False)],
    ]

    window = sg.Window('bock report', layout=layout)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            window.close()
            break

