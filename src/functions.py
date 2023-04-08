import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.messagebox import askokcancel, askyesno, showerror
from src.globals import fonts, view_colors
from src.interface import edit_menu, file_menu, Find, font_menu_sub, \
    main_menu, Replace, root, text, view_menu, view_menu_sub, find_box, \
    replace_box

# global variables for an open file and its path

FILE_PATH = ''
FILE_OPENED = False


def find():
    # Removing all previous selections from the text widget

    text.tag_remove('found', '1.0', tk.END)

    # Getting the desired text from the find_box widget

    get_text = find_box.get()

    # If the text is found, it is searched and highlighted in red

    if get_text:
        idx = '1.0'
        while True:

            # Search for text in the text widget

            idx = text.search(get_text, idx, nocase=True,
                              stopindex=tk.END)
            if not idx:
                break

            # Calculation of the last index of the found text

            last_idx = '% s+% dc' % (idx, len(get_text))

            # Highlighting the found text in red

            text.tag_add('found', idx, last_idx)
            idx = last_idx

        # Setting the selection color, in our case color is red

        text.tag_config('found', foreground='red')


def replace():
    # Removing all previous selections from the text widget

    text.tag_remove('found', '1.0', tk.END)

    # Getting the searched and replaced texts from the find_box and replace_box widgets

    get_text = find_box.get()
    get_text_2 = replace_box.get()

    # If the text is found, then the replaced text is replaced and highlighted in green on a yellow background

    if get_text and get_text_2:
        idx = '1.0'
        while True:

            # Search for text in the text widget

            idx = text.search(get_text, idx, nocase=True,
                              stopindex=tk.END)
            if not idx:
                break

            # Calculation of the last index of the found text

            last_idx = '% s+% dc' % (idx, len(get_text))

            # Deleting the found text

            text.delete(idx, last_idx)

            # Inserting new text

            text.insert(idx, get_text_2)

            # Highlighting the replaced text in green on a yellow background

            last_idx = '% s+% dc' % (idx, len(get_text_2))

            # Setting the highlight color

            text.tag_add('found', idx, last_idx)
            idx = last_idx

        # Setting color

        text.tag_config('found', foreground='green', background='yellow'
                        )


# Function for changing the background color of the text editor

def change_theme(theme):
    text['bg'] = view_colors[theme]['text_bg']
    text['fg'] = view_colors[theme]['text_fg']
    text['insertbackground'] = view_colors[theme]['cursor']
    text['selectbackground'] = view_colors[theme]['select_bg']


# Function for changing the font of the text of the text editor

def change_font(font):
    text['font'] = fonts[font]['font']


# Then there are functions related to edit_menu, *args needed so that we can bind them

def cut(*args):
    text.focus_get().event_generate('<<Cut>>')


def copy(*args):
    text.focus_get().event_generate('<<Copy>>')


def paste(*args):
    text.focus_get().event_generate('<<Paste>>')


def delete_t(*args):
    text.focus_get().event_generate('<<Clear>>')


def select_all(*args):
    text.focus_get().event_generate('<<SelectAll>>')


# Functions related to file_menu

# Create a new file or clear the text field

def new_file(*args):
    text.delete('1.0', tk.END)


def open_file(*args):
    # dialog box for selecting a file

    file_path = askopenfilename(title='File', filetypes=(('Text files',
                                                          '*.txt'), ('All files', '*.*')))

    # if the user has selected a file,
    # then we read its contents and display it in the text widget

    if file_path:
        text.delete('1.0', tk.END)
        with open(file_path) as o:
            text.insert('1.0', o.read())

        # setting global variables for the open file and its path

        global FILE_OPENED
        FILE_OPENED = True
        global FILE_PATH
        FILE_PATH = file_path


def save_as(*args):
    # dialog box for choosing where to save the file

    file_path = asksaveasfilename(title='Save As',
                                  defaultextension='.txt')
    try:

        # writing the contents of the text widget to a file

        with open(file_path, 'w') as file:
            global FILE_OPENED
            FILE_OPENED = True
            global FILE_PATH
            FILE_PATH = file_path
            input_text = text.get('1.0', tk.END)
            file.write(input_text)
    except FileNotFoundError:

        # if an error has occurred, we output an error message

        showerror('Error', 'Save Error')


def save_opened_file():
    with open(FILE_PATH, 'w') as file:
        input_text = text.get('1.0', tk.END)
        file.write(input_text)


# Depending on whether the file is open, we call the functions

def save(*args):
    if not FILE_OPENED:
        save_as()
    else:
        save_opened_file()


def close_file(*args):
    # ask a question about saving a file before closing the program

    answer_for_save = askyesno('Save File', 'Save file?')

    # if the file has already been opened,
    # then call the save_opened_file() function, otherwise save_as()

    if answer_for_save:
        if FILE_OPENED:
            save_opened_file()
        else:
            save_as()

        # asking a question about exiting the program

        answer_for_exit = askokcancel('Exit',
                                      'Are you sure you want to get out?')

        # if the answer is positive, then close the program

        if answer_for_exit:
            root.destroy()
            exit()
    elif not answer_for_save:

        # if the user refuses to save the file, then we ask a question about exiting the program

        answer_for_exit = askokcancel('Exit',
                                      'Are you sure you want to get out?')

        # if the answer is positive, then close the program

        if answer_for_exit:
            root.destroy()
            exit()


# functions for moving the cursor

def move_left(event):
    # get the current cursor index
    # and set the new index one character to the left

    current_index = text.index(tk.INSERT)
    new_index = text.index(current_index + '-1c')

    # remove the selection and set a new cursor index

    text.tag_remove('sel', '1.0', 'end')
    text.mark_set(tk.INSERT, new_index)

    # scroll the text to the new index

    text.see(new_index)
    return 'break'


def move_right(event):
    # get the current cursor index
    # and set the new index one character to the right

    current_index = text.index(tk.INSERT)
    new_index = text.index(current_index + '+1c')

    # remove the selection and set a new cursor index

    text.tag_remove('sel', '1.0', 'end')
    text.mark_set(tk.INSERT, new_index)

    # scroll the text to the new index

    text.see(new_index)
    return 'break'


def move_up(event):
    # get the current cursor index
    # and set the new index one line higher

    current_index = text.index(tk.INSERT)
    (line, col) = map(int, current_index.split('.'))
    new_index = '{}.{}'.format(line - 1, col)

    # remove the selection and set a new cursor index

    text.tag_remove('sel', '1.0', 'end')
    text.mark_set(tk.INSERT, new_index)

    # scroll the text to the new index

    text.see(new_index)
    return 'break'


def move_down(event):
    # get the current cursor index
    # and set the new index one line below

    current_index = text.index(tk.INSERT)
    (line, col) = map(int, current_index.split('.'))
    new_index = '{}.{}'.format(line + 1, col)

    # remove the selection and set a new cursor index

    text.tag_remove('sel', '1.0', 'end')
    text.mark_set(tk.INSERT, new_index)

    # scroll the text to the new index

    text.see(new_index)
    return 'break'


def move_to_start(event):
    # remove the selection
    # and set the new cursor index to the beginning of the text

    text.tag_remove('sel', '1.0', 'end')
    text.mark_set(tk.INSERT, '1.0')
    text.see('1.0')
    return 'break'


def move_to_end(event):
    # remove the selection
    # and set the new cursor index to the end of the text

    text.tag_remove('sel', '1.0', 'end')
    text.mark_set(tk.INSERT, 'end')
    text.see('end')
    return 'break'


def move_cursor_forward(event):
    # remove the selection
    # and set the new cursor index to the next word

    text.tag_remove(tk.SEL, '1.0', tk.END)
    text.mark_set('insert', 'insert+1c wordend')
    return 'break'


def move_cursor_backward(event):
    # remove the selection
    # and set the new cursor index to the previous word

    text.tag_remove(tk.SEL, '1.0', tk.END)
    text.mark_set('insert', 'insert-1c wordstart')
    return 'break'


def move_to_start_of_line(event):
    # remove the selection
    # and set the new cursor index to the beginning of the line

    current_index = text.index(tk.INSERT)
    new_index = '{}.0'.format(current_index.split('.')[0])
    text.tag_remove('sel', '1.0', 'end')
    text.mark_set(tk.INSERT, new_index)

    # scroll the text to the new index

    text.see(new_index)
    return 'break'


def move_to_end_of_line(event):
    # remove the selection
    # and set the new cursor index to the end of the line

    current_index = text.index(tk.INSERT)
    new_index = '{}.end'.format(current_index.split('.')[0])
    text.tag_remove('sel', '1.0', 'end')
    text.mark_set(tk.INSERT, new_index)

    # scroll the text to the new index

    text.see(new_index)
    return 'break'


# We add to the existing sections the names,
# the hint on the bind and the command that performs

file_menu.add_command(label='New File', accelerator='Ctrl+N',
                      command=new_file)
file_menu.add_command(label='Open', accelerator='Ctrl+O',
                      command=open_file)
file_menu.add_separator()
file_menu.add_command(label='Save', accelerator='Ctrl+S', command=save)
file_menu.add_command(label='Save as', accelerator='Ctrl+Shift+S',
                      command=save_as)
file_menu.add_separator()
file_menu.add_command(label='Close', accelerator='Ctrl+Q',
                      command=close_file)
root.config(menu=file_menu)

view_menu_sub.add_command(label='Dark', command=lambda: change_theme('dark'))
view_menu_sub.add_command(label='Light', command=lambda: change_theme('light'))
view_menu.add_cascade(label='Theme', menu=view_menu_sub)

font_menu_sub.add_command(label='Arial', command=lambda: change_font('Arial'))
font_menu_sub.add_command(label='Central Saint Martins', command=lambda: change_font('CSM'))
font_menu_sub.add_command(label='Times New Roman', command=lambda: change_font('TNR'))
view_menu.add_cascade(label='Font', menu=font_menu_sub)
root.config(menu=view_menu)

edit_menu.add_command(label='Cut', accelerator='Ctrl+X', command=cut)
edit_menu.add_command(label='Copy', accelerator='Ctrl+C', command=copy)
edit_menu.add_command(label='Paste', accelerator='Ctrl+V',
                      command=paste)
edit_menu.add_command(label='Delete', accelerator='Del',
                      command=delete_t)
edit_menu.add_command(label='Select All', accelerator='Ctrl+A',
                      command=select_all)
root.config(menu=edit_menu)

main_menu.add_cascade(label='File', menu=file_menu)
main_menu.add_cascade(label='View', menu=view_menu)
main_menu.add_cascade(label='Edit', menu=edit_menu)
root.config(menu=main_menu)

Find.config(command=find)
Replace.config(command=replace)

# binds used in TextEditor
# file_menu

root.bind('<Control-o>', open_file)
root.bind('<Control-s>', save)
root.bind('<Control-Shift-s>', save_as)
root.bind('<Control-q>', close_file)

# edit_menu

root.bind('<Control-x>', cut)
root.bind('<Control-c>', copy)
root.bind('<Control-v>', paste)
root.bind('<Control-d>', delete_t)
root.bind('<Control-a>', select_all)
root.bind('<Control-n>', new_file)

# binds with text

text.bind('<Left>', move_left)
text.bind('<Right>', move_right)
text.bind('<Up>', move_up)
text.bind('<Down>', move_down)
text.bind('<Control-Shift-Left>', move_to_start)
text.bind('<Control-Shift-Right>', move_to_end)
text.bind('<Control-w>', move_to_start_of_line)
text.bind('<Control-e>', move_to_end_of_line)

# may be problem with bind on mac_users

text.bind('<Control-Right>', move_cursor_forward)
text.bind('<Control-Left>', move_cursor_backward)

# Using the x button of the text editor interface will work similarly to closing from the file menu

root.protocol('WM_DELETE_WINDOW', close_file)