import random

class Roll():
    def __init__(self, dice_size, dice_count, array_size):
        self.dice_size = dice_size
        self.dice_count = dice_count
        self.array_size = array_size
        self.arr = self.fill_array()
    
    def roll(self):
        return random.randint(1, self.dice_size)
    
    def fill_array(self):
        print('Started filling...')
        array = []
        for i in range(0, self.array_size):
            roll_result = 0
            for j in range(1, self.dice_count + 1):
                roll_result += self.roll()
            array.append(roll_result)
        print('Filling complete!')
        return array
    
    def draw_graph(self):
        for i in range(self.dice_count, (self.dice_size * self.dice_count) + 1):
            print(str(i) + ': ' + str(self.arr.count(i)))

        for i in range(self.dice_count, (self.dice_size * self.dice_count) + 1):
            print(('|' * int((self.arr.count(i) / self.array_size) * 1000)) + ' - ' + str(i))

    def graph_to_file(self, path):
        file = open(path, 'w')
        file.write('Dice size: ' + str(self.dice_size) + '\n')
        file.write('Dice count: ' + str(self.dice_count) + '\n')
        file.write('Roll count: ' + str(self.array_size) + '\n')

        for i in range(self.dice_count, (self.dice_size * self.dice_count) + 1):
            file.write(str(i) + ': ' + str(self.arr.count(i)) + '\n')

        for i in range(self.dice_count, (self.dice_size * self.dice_count) + 1):
            file.write(('|' * int((self.arr.count(i) / self.array_size) * 1000)) + ' - ' + str(i) + '\n')