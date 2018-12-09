import itertools as it

def part_one(players, finalMarble):
    # first 3 moves are special case
    circle = [0, 2, 1]
    currentIndex = 1
    turnOrder = it.cycle(range(players))
    scores = [0]*players
    removedMarbles = []
    for i in range(3, finalMarble+1):
        player = next(turnOrder)
        print(circle)
        #print("Current player:\t{}\nNext marble:\t{}\nCurrent Index:\t{}".format(player+1,i,currentIndex))
        if i % 23 == 0:
            scores[player] += i
            # the marble 7 marbles counter-clockwise from the ACTIVE marble is removed from the circle
            marbleToBeRemoved = (currentIndex - 7)
            # and also added to the current player's score.
            scores[player] += circle[marbleToBeRemoved]
            currentIndex = marbleToBeRemoved
            removedMarbles.append(marbleToBeRemoved)
            del circle[marbleToBeRemoved]
            i += 1
        else:
            insertPosition = (currentIndex + 2) % len(circle)
            circle.insert(insertPosition, i)
            currentIndex = insertPosition
            i += 1
    print(removedMarbles)
    return max(scores)

if __name__ == "__main__":
    print(part_one(9, 168))




