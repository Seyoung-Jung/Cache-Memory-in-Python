class Memory:
    hit = 0
    total_hit = 0
    total_time = 0

    def __init__(self, name, size, time, lower_memory=None):
        self.name = name
        self.MEMORY_SIZE = size
        self.ACCESS_TIME = time
        self.memory = []
        self.lower_memory = lower_memory

    def get(self, data):
        if data in self.memory:
            Memory.total_hit += 1
            Memory.total_time += self.ACCESS_TIME
            if self.name == 'L1' or self.name == "L2" or self.name == 'L3':
                Memory.hit += 1
            return data, self.ACCESS_TIME
        else:
            if self.lower_memory is None:
                raise ValueError('There is not {} in {}.'.format(data, self.name))
            data, time = self.lower_memory.get(data)
            if len(self.memory) == self.MEMORY_SIZE:
                self.memory.pop(0)
            self.memory.append(data)
            return data, time + self.ACCESS_TIME

    def data_init(self):
        self.memory = list(range(self.MEMORY_SIZE))