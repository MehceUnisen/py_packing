import turtle
from random import randint, shuffle

left_most = 0
bottom_most = 0
current_height = 0
filled_coordinates = []

wn = turtle.Screen()
rect_turtle = turtle.Turtle()
rect_turtle.speed(0)
wn.colormode(255)
def draw_rectangle(width, height):
    rect_turtle.fillcolor(randint(0, 255),randint(0, 255),randint(0, 255))
    rect_turtle.begin_fill()
    for _ in range(2):
        rect_turtle.forward(width)
        rect_turtle.left(90)
        rect_turtle.forward(height)
        rect_turtle.left(90)
    rect_turtle.end_fill()

def read_data(path):
    str_data = []
    box_count = 0
    file_path = path

    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            str_data.append(line.split(' '))
        box_count = str_data[0][0]
        str_data.pop(0)
        str_data.pop(0)
        for data in str_data:
            data[0] = int(data[0])
            data[1] = data[1].replace('\n', '')
            data[1] = int(data[1])
    return int(box_count), str_data

def draw(x, y, w, h):
    rect_turtle.penup()
    rect_turtle.goto(x * 10, y * 10)
    rect_turtle.pendown()
    draw_rectangle(w * 10, h * 10)

def draw_outline():
    draw(0, 0, 20, 20)

def choose_box(boxes):
    global current_height
    global left_most
    global bottom_most
    score = []
    for box in boxes:
        pre_score = []
        for j in range(2):
            pre_score.append(0)
            if left_most + box[0] < 20:
                pre_score[j] += 5
            if left_most + box[0] == 20:
                pre_score[j] += 10
            if left_most + box[0] > 20:
                pre_score[j] -= 10
            box[0], box[1] = box[1], box[0]

        if pre_score[0] > pre_score[1]:
            box[0], box[1] = box[1], box[0]
            score.append(pre_score[0]) 
        else:
            score.append(pre_score[1])
         
    l_idx = 0
    l_item = score[l_idx]
    for index, element in enumerate(score):
        if element > l_item:
            l_item = element
            l_idx = index
    return boxes[l_idx]   

def choose_coordinate(box):
    global current_height 
    global left_most
    global bottom_most
    global filled_coordinates

    bx = box[0]
    by = box[1]
 
def place(box, x, y):
    draw(x, y , box[0], box[1])
    
def pack():
    global current_height
    global left_most
    global bottom_most

    draw_outline()
    cnt, data = read_data("data_set/C1_1")
    current_height = 0
    left_most = 0
    bottom_most = 0
    i = 0
    shuffle(data)
    for i in range(cnt):
        for boxes in data: 
            box = choose_box(data)
            data.remove(box)
            x, y = choose_coordinate(box)
            place(box, x, y)
    print(data)

pack()
wn.exitonclick()