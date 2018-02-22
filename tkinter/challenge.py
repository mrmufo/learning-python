# Write a GUI program to create a simple calculator
# layout that looks like the screenshot.
#
# Try to be as Pythonic as possible - it's ok if you
# end up writing repeated Button and Grid statements,
# but consider using lists and a for loop.
#
# There is no need to store the buttons in variables.
#
# As an optional extra, refer to the documentation to
# work out how to use minsize() to prevent your window
# from being shrunk so that the widgets vanish from view.
#
# Hint: You may want to use the widgets .winfo_height() and
# winfo_width() methods, in which case you should know that
# they will not return the correct results unless the window
# has been forced to draw the widgets by calling its .update()
# method first.
#
# If you are using Windows you will probably find that the
# width is already constrained and can't be resized too small.
# The height will still need to be constrained, though.

try:
    import tkinter
except ImportError:  # python 2
    import Tkinter as tkinter

mainWindow = tkinter.Tk()
mainWindow.title("Calculator")
mainWindow.geometry('340x400+500+400')
mainWindow.minsize(240, 320)
mainWindow['padx'] = 8

mainWindow.columnconfigure(0, weight=1)
mainWindow.columnconfigure(1, weight=1)
mainWindow.columnconfigure(2, weight=1)
mainWindow.columnconfigure(3, weight=1)
mainWindow.rowconfigure(0, weight=1)
mainWindow.rowconfigure(1, weight=1)
mainWindow.rowconfigure(2, weight=1)
mainWindow.rowconfigure(3, weight=1)
mainWindow.rowconfigure(4, weight=1)
mainWindow.rowconfigure(5, weight=1)

result = tkinter.Entry(mainWindow)
result.grid(row=0, column=0, columnspan=4, sticky='nsew', padx=1, pady=10)

# keyPad = tkinter.Frame(mainWindow)
# keyPad.grid(row=1, column=0, sticky='nsew')

buttonList = ["0", "=", "/", "1", "2", "3", "*", "4", "5", "6", "-", "7", "8", "9", "+", "C", "CE"]
col_counter = 0
row_counter = 5
col_span = 1
row_span = 1
for each in buttonList:
    new_button = tkinter.Button(mainWindow, text=each, font=18)  # , command=result.insert(0, each))
    if each == '=':
        col_span = 2
        new_button.grid(row=row_counter, column=col_counter, columnspan=col_span, rowspan=row_span, sticky='nsew',
                        padx=2, pady=2)
        col_counter += 2
        continue
    new_button.grid(row=row_counter, column=col_counter, columnspan=col_span, rowspan=row_span, sticky='nsew',
                    padx=2, pady=2)
    col_counter += 1
    if col_counter > 3:
        col_counter = 0
        row_counter -= 1
    col_span = 1
    row_span = 1

# c_Button = tkinter.Button(mainWindow, text="C")
# ce_Button = tkinter.Button(mainWindow, text="CE")
# sev_Button = tkinter.Button(mainWindow, text="7")
# eig_Button = tkinter.Button(mainWindow, text="8")
# nin_Button = tkinter.Button(mainWindow, text="9")
# plus_Button = tkinter.Button(mainWindow, text="+")
# fou_Button = tkinter.Button(mainWindow, text="4")
# fiv_Button = tkinter.Button(mainWindow, text="5")
# six_Button = tkinter.Button(mainWindow, text="6")
# minus_Button = tkinter.Button(mainWindow, text="-")
# one_Button = tkinter.Button(mainWindow, text="1")
# two_Button = tkinter.Button(mainWindow, text="2")
# thr_Button = tkinter.Button(mainWindow, text="3")
# times_Button = tkinter.Button(mainWindow, text="*")
# c_Button.grid(row=1, column=0, sticky='nsew')
# ce_Button.grid(row=1, column=1, sticky='nsew')
# sev_Button.grid(row=2, column=0, sticky='nsew')
# eig_Button.grid(row=2, column=1, sticky='nsew')
# nin_Button.grid(row=2, column=2, sticky='nsew')
# plus_Button.grid(row=2, column=3, sticky='nsew')
# fou_Button.grid(row=3, column=0, sticky='nsew')
# fiv_Button.grid(row=3, column=1, sticky='nsew')
# six_Button.grid(row=3, column=2, sticky='nsew')
# minus_Button.grid(row=3, column=3, sticky='nsew')
# one_Button.grid(row=4, column=0, sticky='nsew')
# two_Button.grid(row=4, column=1, sticky='nsew')
# thr_Button.grid(row=4, column=2, sticky='nsew')
# times_Button.grid(row=4, column=3, sticky='nsew')

mainWindow.mainloop()
