from roll import Roll

k = int(input("Enter size of the dice: ") or 6)
n = int(input("Enter number of dices: ") or 5)
size = int(input("Enter number of rolls: ") or 1000000)

dice = Roll(k, n, size)

dice.draw_graph()
dice.graph_to_file('result.txt')