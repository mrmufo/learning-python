import math
try:
    import tkinter
except ImportError:  # python 2
    import Tkinter as tkinter


def parabola(c, size):
    for x in range(size):
        y = x * x / size
        plot(c, x, y)
        plot(c, -x, y)


# Modify the circle function that it allows the colour of the circle to be specified
# and defaults to red if a colour is not given. You may want to review the previous lectures
# about named parameters and default values.
#
def circle(c, radius, g, h, colour="red"):
    c.create_oval(g + radius, h + radius, g - radius, h - radius, outline=colour, width=2)
    # for x in range(g * 10, (g + radius) * 10):
    #     x /= 10
    #     y = h + (math.sqrt(radius ** 2 - ((x-g) ** 2)))
    #     plot(c, x, y)
    #     plot(c, x, 2 * h - y)
    #     plot(c, 2 * g - x, y)
    #     plot(c, 2 * g - x, 2 * h - y)


def draw_axes(c):
    c.update()
    x_origin = c.winfo_width() / 2
    y_origin = c.winfo_height() / 2
    c.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin))
    c.create_line(-x_origin, 0, x_origin, 0, fill="black")
    c.create_line(0, y_origin, 0, -y_origin, fill="black")
    print(locals())


def plot(c, x, y):
    c.create_line(x, -y, x + 1, -y + 1, fill="red")


mainWindow = tkinter.Tk()

mainWindow.title("Parabola")
mainWindow.geometry("640x480")

canvas = tkinter.Canvas(mainWindow, width=640, heigh=480)
canvas.grid(row=0, column=0)

# print(repr(canvas), repr(canvas2))
draw_axes(canvas)

# for x in range(-100, 100):
#     y = parabola(x)
#     plot(canvas, x, -y)
parabola(canvas, 100)
parabola(canvas, 200)
circle(canvas, 100, 100, 100, "yellow")
circle(canvas, 100, 100, -100)
circle(canvas, 100, -100, 100)
circle(canvas, 100, -100, -100, "blue")
circle(canvas, 10, 30, 30)
circle(canvas, 10, 30, -30)
circle(canvas, 10, -30, 30)
circle(canvas, 10, -30, -30)
circle(canvas, 30, 0, 0, "green")
mainWindow.mainloop()
