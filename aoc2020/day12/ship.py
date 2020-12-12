import math


class ShipAction:
    def __init__(self, action_type, value):
        self.type = action_type
        self.value = value


class ShipState:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.direction = 0

    def move(self, distance, direction=None):
        self._move(distance, direction=None)

    def _move(self, distance, direction=None):
        if direction == None:
            direction = self.direction
        self.x += int(distance * math.cos(math.radians(direction)))
        self.y += int(distance * math.sin(math.radians(direction)))

    def move_north(self, distance):
        self._move(distance, 90)

    def move_west(self, distance):
        self._move(distance, 180)

    def move_south(self, distance):
        self._move(distance, 270)

    def move_east(self, distance):
        self._move(distance, 0)

    def turn_left(self, degree):
        self.direction += degree

    def turn_right(self, degree):
        self.direction -= degree


class WaypointState(ShipState):
    def __init__(self, ship_state):
        self.x = 10
        self.y = 1
        self.direction = 0
        self.ship_state = ship_state

    def turn(self, degree):
        rad = math.radians(degree)
        old_x, old_y = self.x, self.y
        self.x = int(old_x * math.cos(rad)) + int(old_y * math.sin(rad))
        self.y = - int(old_x * math.sin(rad)) + int(old_y * math.cos(rad))

    def turn_left(self, degree):
        self.turn(-degree)

    def turn_right(self, degree):
        self.turn(degree)

    def move(self, times):
        self.ship_state.x += times * self.x
        self.ship_state.y += times * self.y


def get_distance(ship_movements):
    ship_state = ShipState()
    for movement in parse_movements(ship_movements):
        ship_state = dispatch(ship_state, movement)
    return abs(ship_state.x) + abs(ship_state.y)


def get_distance_with_waypoint(ship_movements):
    ship_state = ShipState()
    waypoint_state = WaypointState(ship_state)
    for movement in parse_movements(ship_movements):
        waypoint_state = dispatch(waypoint_state, movement)
    return abs(waypoint_state.ship_state.x) + abs(waypoint_state.ship_state.y)


def dispatch(state: ShipState, action: ShipAction):
    if (action.type == 'F'):
        state.move(action.value)
    if (action.type == 'L'):
        state.turn_left(action.value)
    if (action.type == 'R'):
        state.turn_right(action.value)
    if (action.type == 'N'):
        state.move_north(action.value)
    if (action.type == 'W'):
        state.move_west(action.value)
    if (action.type == 'S'):
        state.move_south(action.value)
    if (action.type == 'E'):
        state.move_east(action.value)
    return state


def parse_movements(ship_movements):
    for movement in ship_movements:
        yield ShipAction(movement[0], int(movement[1:]))
