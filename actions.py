class Action:
    pass

# Subclass of Action
class EscapeAction(Action):
    pass

# Subclass of Action
class MovementAction(Action):
    def __init__(self, dx: int, dy: int):
        super().__init__()

        self.dx = dx
        self.dy = dy