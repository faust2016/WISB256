
def lees(s):
    file = open(s)
    lijst=[]
    for line in file:
        gesplitst = line.strip().split(' ')
        lijst+= gesplitst
    print(lijst)
        
lees('words.txt')