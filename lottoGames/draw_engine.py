from random import randint
import time

draw_result = []

def Draw_numbers():
    while len(draw_result)<4:
        drawed_number = randint(1,39)
        if not drawed_number in draw_result:
            draw_result.append(drawed_number)
    return draw_result.sort()

while True:
    Draw_numbers()
    print(draw_result)
    time.sleep(5)
    draw_result = []