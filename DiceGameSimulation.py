import random 

def simulation():
    high = 0
    final = 0
    for i in range(0,10000):
        score = game()
        high = max(score, high)
        final += score
    average = final / 10000
    print ("Average amount won = " + "$%.2f" % average)
    print ("Max amount won = " + "$%.2f" % high)


def game():
    done = False
    total = 0
    while done != True:
        roll = random.randint(1, 6)
        if roll <=3:
            done = True
        else:
            total+=roll
    return total

simulation()







    




