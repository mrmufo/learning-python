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

# =======================MY SOLUTION====================================
# mW = tkinter.Tk()
# mW.title("Calculator")
# mW.geometry('340x400+500+400')
# mW.minsize(240, 320)
# mW['padx'] = 8
#
# mW.columnconfigure(0, weight=1)
# mW.columnconfigure(1, weight=1)
# mW.columnconfigure(2, weight=1)
# mW.columnconfigure(3, weight=1)
# mW.rowconfigure(0, weight=1)
# mW.rowconfigure(1, weight=1)
# mW.rowconfigure(2, weight=1)
# mW.rowconfigure(3, weight=1)
# mW.rowconfigure(4, weight=1)
# mW.rowconfigure(5, weight=1)
#
# result = tkinter.Entry(mW)
# result.grid(row=0, column=0, columnspan=4, sticky='nsew', padx=1, pady=10)
#
# buttonList = ["0", "=", "/", "1", "2", "3", "*", "4", "5", "6", "-", "7", "8", "9", "+", "C", "CE"]
# col_counter = 0
# row_counter = 5
# col_span = 1
# row_span = 1
# for each in buttonList:
#     new_button = tkinter.Button(mW, text=each, font=18)  # , command=result.insert(0, each))
#     if each == '=':
#         col_span = 2
#         new_button.grid(row=row_counter, column=col_counter, columnspan=col_span, rowspan=row_span, sticky='nsew',
#                         padx=2, pady=2)
#         col_counter += 2
#         continue
#     new_button.grid(row=row_counter, column=col_counter, columnspan=col_span, rowspan=row_span, sticky='nsew',
#                     padx=2, pady=2)
#     col_counter += 1
#     if col_counter > 3:
#         col_counter = 0
#         row_counter -= 1
#     col_span = 1
#     row_span = 1
# ========================================================================

keys = [[('C', 1), ('CE', 1)],
        [('7', 1), ('8', 1), ('9', 1), ('+', 1)],
        [('4', 1), ('5', 1), ('6', 1), ('-', 1)],
        [('1', 1), ('2', 1), ('3', 1), ('*', 1)],
        [('0', 1), ('=', 2), ('/', 1)]]

mW_padding = 8
mW = tkinter.Tk()
mW.title("Calculator")
mW.geometry('640x480+200+400')
mW['padx'] = mW_padding

result = tkinter.Entry(mW)
result.grid(row=0, column=0, sticky='nsew')

key_pad = tkinter.Frame(mW)
key_pad.grid(row=1, column=0, sticky='nsew')

row = 0

for key_row in keys:
    col = 0
    for key in key_row:
        tkinter.Button(key_pad, text=key[0]).grid(row=row, column=col, columnspan=key[1], sticky=tkinter.E + tkinter.W)
        col += key[1]
    row += 1
mW.update()
mW.minsize(key_pad.winfo_width() + mW_padding, result.winfo_height() + key_pad.winfo_height())
mW.maxsize(key_pad.winfo_width() + mW_padding + 100, result.winfo_height() + key_pad.winfo_height() + 100)

mW.mainloop()
