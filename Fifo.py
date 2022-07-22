class Circular_buffer:
    def __init__(self, size):
        self.size = size
        self.buf = []
        self.full = 0
    def put(self, value):
        if (len(self.buf) == self.size):
            self.buf = self.buf[1 :] + [value]
        else:
            self.buf.append(value)
        self.full += 1
        print(self.buf)
    def ret(self):
        return(self.buf)
class Circular_buffer_1:
    def __init__(self, size):
        self.size = size
        self.buf = []
        self.index = 0
    def put(self, value):

        if (len(self.buf) == self.size):
            self.buf[self.index] = value
        else:
            self.buf.append(value)
        print(self.buf)
        self.index = (self.index + 1) % self.size
    def ret(self):
        return(self.buf)
