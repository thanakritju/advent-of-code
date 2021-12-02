def get_multiplication_of_coordinate(actions):
    x = 0
    y = 0

    for action in actions:
        command, value = action.split(" ")

        if command == "forward":
            x += int(value)
        if command == "down":
            y += int(value)
        if command == "up":
            y -= int(value)
        
    return x*y 

def get_multiplication_of_coordinate_with_aim(actions):
    x = 0
    y = 0
    aim = 0

    for action in actions:
        command, value = action.split(" ")

        if command == "forward":
            x += int(value)
            y += aim * int(value)
        if command == "down":
            aim += int(value)
        if command == "up":
            aim -= int(value)
        
    return x*y 
