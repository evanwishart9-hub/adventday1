class Lock:
    def __init__(self):
        self.nums = []
        for i in range(100):
            self.nums.append(i)
        self.direction = ["L", "R"]
        self.current = 50
        self.zeros = 0

    def turn(self, order):
        number = int(order[1:])
        if order[0] == "L":
            for i in range(number, 0, -1):
                self.current = self.nums[(self.current - 1) % len(self.nums)]
                self.count_zeros(self.current)
        elif order[0] == "R":
             for i in range(number, 0, -1):
                self.current = self.nums[(self.current + 1) % len(self.nums)]
                self.count_zeros(self.current)
    def count_zeros(self, current):
        if current == 0:
            self.zeros += 1
