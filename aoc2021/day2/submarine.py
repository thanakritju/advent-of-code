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
