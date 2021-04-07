class Snake:
    def __init__(self, color):
        self.list = []  # store tuples with (col, row)
        self.direction = 'LEFT'  # right
        self.speed = 1
        self.color = color
        self.length = 1

    def move(self, direction):
        # print(self.list)
        if direction == 'UP':
            self.list = [(self.list[0][0], self.list[0][1] - 1)] + self.list
        if direction == 'DOWN':
            self.list = [(self.list[0][0], self.list[0][1] + 1)] + self.list
        if direction == 'LEFT':
            self.list = [(self.list[0][0] - 1, self.list[0][1])] + self.list
        if direction == 'RIGHT':
            self.list = [(self.list[0][0] + 1, self.list[0][1])] + self.list
        self.list = self.list[:self.length]
        self.direction = direction
        # print(self.list)

