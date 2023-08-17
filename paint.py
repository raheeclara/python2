from tkinter import *

canvas_color = "white"
pen_color = "black"
pen_size = 2
shape_size = 10
my_tool = "pen"
fill_color = "white"

# 캔버스에 그림 그리는 함수
def paint(event):
    global pen_size, pen_color
    x1, y1 = event.x, event.y
    x2, y2 = event.x + pen_size, event.y + pen_size
    canvas.create_line(x1, y1, x2, y2, width = pen_size, fill = pen_color)

# 색깔 변경 함수
def change_color(color) :
    global pen_color,feel_color,my_tool
    if my_tool == "pen" :
        pen_color = color
        btn_pen['bg'] = color
        if color == "white" or pen_color == "yellow":
            btn_pen['fg'] = "black"
        if color == "black" :
            btn_pen['fg'] = "white"
    elif my_tool == "canvas":
        canvas['bg'] = color
        btn_canvas['bg'] = color
        if canvas_color == "white" or canvas_color == "yellow":
            btn_canvas['fg'] = "black"
        if canvas_color == "black" :
            btn_canvas['fg'] = "white"    
    else :
        fill_color = color
        btn_fill['bg'] = color
        if canvas_color == "white" or canvas_color == "yellow":
            btn_canvas['fg'] = "black"
        if canvas_color == "black" :
            btn_canvas['fg'] = "white"


# 도구 변경 함수
def change_tool(tool) :
    global my_tool
    my_tool = tool
    if my_tool == "oval":
        btn_oval['relief'] = "groove"
        btn_rect['relief'] = "raised"
        btn_tri['relief'] = "raised"
    elif my_tool == "rect":
        btn_oval['relief'] = "groove"
        btn_rect['relief'] = "raised"
        btn_tri['relief'] = "raised"
    elif my_tool == "tri":
        btn_oval['relief'] = "groove"
        btn_rect['relief'] = "raised"
        btn_tri['relief'] = "raised"
    else:
        btn_oval['relief'] = "groove"
        btn_rect['relief'] = "raised"
        btn_tri['relief'] = "raised"
    
# 펜 크기 변경 함수
def change_size(btn) :
    global shape_size,pen_size,my_tool
    if my_tool == "pen":
        if btn == "plus" :
            pen_size += 1
        elif btn == "minus" and pen_size > 2 :
                pen_size -= 1
        else :
            if btn == "plus" :
                pen_size += 10
            elif btn == "minus" and pen_size > 2 :
                pen_size -= 10


def draw_shape(event) :
    global shape_size,my_tool
    x1, y1 = event.x, event.y
    x2, y2 = event.x + shape_size, event.y + shape_size
    if my_tool == "oval":
        canvas.create_oval(x1 - (shape_size/2), y1,x2 - (shape_size/2),y2,fill = fill_color)
    elif my_tool == "rect": 
        canvas.create_rect(x1,y1,x2,y2,fill = fill_color)
    elif my_tool == "tri": 
        canvas.create_polygon(x1,y1,x2,y2,(x1 - (shape_size)),y2,fill = fill_color,outline = "black")

# 캔버스 초기화하는 함수
def clear_canvas() :
    canvas['bg'] = "white"
    btn_canvas['bg'] = "white"
    btn_canvas['fg'] = "black"
    canvas.delete("all")

w, h = 13, 2
win = Tk()
win.title("My paint")
win.geometry("510x600+200+200")
canvas = Canvas(win, width = 510, height = 470, bg = "white")
canvas.bind("<B1-Motion>", paint)
canvas.bind("<Double-Button-1>", draw_shape)
# 마우스 왼쪽 버튼을 누르면서 움직일 때

btn_white = Button(win, text = "white", bg = "white", width = w, height = h, command = lambda : change_color("white"))
btn_black = Button(win, text = "black", bg = "black", fg = "white", width = w, height = h, command = lambda : change_color("black"))
btn_blue = Button(win, text = "blue", bg = "blue",  fg = "white", width = w, height = h, command = lambda : change_color("blue"))
btn_green = Button(win, text = "green", bg = "green",  fg = "white", width = w, height = h, command = lambda : change_color("green"))
btn_yellow = Button(win, text = "yellow", bg = "yellow", width = w, height = h, command = lambda : change_color("yellow"))
btn_red = Button(win, text = "red", bg = "red",  fg = "white", width = w, height = h, command = lambda : change_color("red"))

btn_canvas = Button(win, text = "canvas\ncolor", bg = "white", fg = "black", width = w, height = h, command = lambda : change_tool("canvas"))
btn_pen = Button(win, text = "pen\ncolor", bg = "black", fg = "white", width = w, height = h, command = lambda : change_tool("pen"))
btn_fill = Button(win, text = "fill\ncolor", bg = "white", fg = "black", width = w, height = h, command = lambda : change_tool("shape"))

btn_oval = Button(win, text = "○", bg = "white", width = w, height = h, command = lambda : change_tool("oval"))
btn_rect = Button(win, text = "□", bg = "white", width = w, height = h, command = lambda : change_tool("rect"))
btn_tri = Button(win, text = "△", bg = "white", width = w, height = h, command = lambda : change_tool("tri"))


btn_plus = Button(win, text = "+", bg = "white", width = w, height = h, command = lambda : change_size("plus"))
btn_minus = Button(win, text = "-", bg = "white", width = w, height = h, command = lambda : change_size("minus"))
btn_clear = Button(win, text = "clear", bg = "white", width = w, height = h, command = clear_canvas)

canvas.grid(row = 0, column = 0, columnspan = 6)
btn_canvas.grid(row = 1, column = 0)
btn_black.grid(row = 1, column = 1)
btn_blue.grid(row = 1, column = 2)
btn_green.grid(row = 1, column = 3)
btn_plus.grid(row = 1, column = 4)
btn_pen.grid(row = 2, column = 0)
btn_white.grid(row = 2, column = 1)
btn_red.grid(row = 2, column = 2)
btn_yellow.grid(row = 2, column = 3)
btn_minus.grid(row = 2, column = 4)

btn_fill.grid(row = 3,column = 0)
btn_oval.grid(row = 3,column = 1)
btn_rect.grid(row = 3,column = 2)
btn_tri.grid(row = 3,column = 3)
btn_clear.grid(row = 3, column = 4)

win.mainloop()
