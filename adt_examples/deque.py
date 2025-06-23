class Deque:
    def __init__(self, size):
        self.size  = size
        self.list = [None for _ in range(size)]
        self.right = 0
        self.left = 0
        self.counter = 0


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
            self.list[((self.left -1) % self.size)] = x
            self.left -= 1


    def popleft(self):
        value = self.list[(self.left % self.size)]
        self.list[(self.left % self.size)] = None
        self.left += 1
        return value

    def peekleft(self):
        return self.list[(self.left) % self.size]

    def __len__(self):
        return self.right - self.left

    def __iter__(self):
        self.counter = self.left
        return self

    def __next__(self):
        while self.counter != self.right:
            val = self.list[self.counter%self.size]
            self.counter += 1
            return val
        else:
            raise StopIteration


def base_data():
    Q = Deque(5)
    Q.append(5)
    Q.append(10)
    Q.append(15)
    Q.append(20)
    Q.append(25)
    Q.popleft()
    Q.popleft()
    Q.append(35)
    Q.append(40)

    T = Deque(4)
    T.append('n')
    T.append('n+1')
    T.appendleft('n+2')
    T.appendleft('n+3')
    T.pop()
    T.append('n+4')
    return Q, T