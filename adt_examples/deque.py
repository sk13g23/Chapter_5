class Deque:
    def __init__(self, size):
        self.size  = size
        self.list = [None for _ in range(size)]
        self.left = 0
        self.right = size-1

    def append(self , x):
        if self.list[self.right] is None:
            self.list[self.right] = x
            self.right -= 1
        else:
            pass

    def appendleft(self , x):
        if self.list[self.left] is None:
            self.list[self.left] = x
            self.left += 1
        else:
            pass


    def pop(self):
        return self.list.pop()

    def popleft(self):
        return self.list.pop(0)

    def peek(self):
        return self.list[-1]

    def peekleft(self):
        return self.list[0]


    def __len__(self):
        return len(self.list)