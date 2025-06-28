
import random

num_prisoners=10

num_turns=10

prisoners=[]


def get_prisoner_index(i):
    return i-1
def get_prisoner_id(i):
    return i+1
def get_prisoner(i):
    return prisoners[get_prisoner_index(i)]




for i in range(0,num_prisoners):
    prisoner_id=get_prisoner_id(i)
    prisoners.append(prisoner_id)

# print(prisoners)

boxes=prisoners.copy()
random.shuffle(boxes)

# print(boxes)

num_founded=0

for prisoner_id in prisoners:
    # print(prisoner_id)

    current_box=get_prisoner_index(prisoner_id)
    found=False
    print(f"-----------{prisoner_id} Turn-----------")

    for i in range(0,num_turns):

        box_id=get_prisoner_id(current_box)

        box_value=boxes[current_box]
        print(f"{i+1}: Finding {prisoner_id} in box {box_id} found {box_value}")
        if prisoner_id == box_value:
            print(f"{i+1}: Found {prisoner_id} in box {box_id}")
            found=True
            num_founded=num_founded+1
            break

        current_box=get_prisoner_index(box_value)
        

    if not found:
        print(f"{num_turns}: Not Found {prisoner_id}")

print(f"Founded: {num_founded}")




