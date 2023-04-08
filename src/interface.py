import tkinter as tk

# Creating the main application window with title 'Text Editor' and size '600x800'

root = tk.Tk()
root.title('Text Editor')


# getting the screen dimensions

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculating the coordinates for centering the window

x = (screen_width // 2) - (600 // 2)
y = (screen_height // 2) - (800 // 2)

# Setting the window position

root.geometry(f"600x800+{x}+{y}")

# minimum size of the text editor window

root.minsize(525, 650)

# creating a frame in the main window

frame = tk.Frame(root)
frame.pack(fill=tk.BOTH, expand=1)

# creating a text widget

text = tk.Text(
    frame,
    background='black',
    fg='lime',
    padx=10,
    pady=10,
    wrap=tk.WORD,
    insertbackground='red',
    selectbackground='#ADD8E6',
    spacing3=10,
    )
text.focus_set()
text.pack(fill=tk.BOTH, expand=1, side=tk.BOTTOM)

# creating the main menu in the main window

main_menu = tk.Menu(root)

# creating the "File" submenu in the main menu

file_menu = tk.Menu(main_menu, tearoff=0)

# creating a "View" submenu in the main menu

view_menu = tk.Menu(main_menu, tearoff=0)
view_menu_sub = tk.Menu(view_menu, tearoff=0)
font_menu_sub = tk.Menu(view_menu, tearoff=0)

# creating the "Edit" submenu in the main menu

edit_menu = tk.Menu(main_menu, tearoff=0)

# creating an input field for text search

find_box = tk.Entry(frame)
find_box.pack(side=tk.LEFT, fill=tk.BOTH)

# creating a button "Find"

Find = tk.Button(frame, text='Find')
Find.pack(side=tk.LEFT, fill=tk.BOTH)

# creating an input field for text replace

replace_box = tk.Entry(frame)
replace_box.pack(side=tk.RIGHT, fill=tk.BOTH)

# creating a button "Replace"

Replace = tk.Button(frame, text='Replace')
Replace.pack(side=tk.RIGHT)
frame.pack(side=tk.TOP)
