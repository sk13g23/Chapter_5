class Deque:
    def __init__(self, size):
        self.size  = size
        self.list = [None for _ in range(size)]
        self.right = 0
        self.left = 0


    def append(self,x):
        self.list[self.right % self.size] = x
        self.right += 1


    def pop(self):
        value = self.list[(self.right-1) % self.size]
        self.list[(self.right -1) % self.size] = None
        self.right -= 1
        return value


    def peek(self):
        return self.list[(self.right-1) % self.size]

    def appendleft(self , x):
        if self.list[(self.left) % self.size] == None:
            self.list [(self.left % self.size)]= x
            self.left -= 1
        else:
            self.left -= 1
            self.appendleft(x)


    def popleft(self):
        value = self.list[(self.left % self.size)]
        self.list[(self.left % self.size)] = None
        self.left += 1
        return value

    def peekleft(self):
        return self.list[(self.left) % self.size]

    def __len__(self):
        return self.right - self.left