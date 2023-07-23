from random import randint

draw_result = []

while len(draw_result)<4:
    drawed_number = randint(1,39)
    if not drawed_number in draw_result:
        draw_result.append(drawed_number)


result_sorted = sorted(draw_result)

print(result_sorted)