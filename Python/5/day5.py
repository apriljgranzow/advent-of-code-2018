with open("input5.txt") as file:
    chain = file.read()

def pairs(string):
    return list(zip(string[:len(string)],string[1:]))

def react(pairs):
    return [x for x in pairs if x[0] != x[1].swapcase()]

def part_one(string): # this one doesn't work lol - it's inefficient to generate so many new lists
    reaction = react(pairs(string))
    newList = [i for sub in reaction for i in sub]
    while len(newList) != len(reaction):
        reaction = react(pairs(newList))
        newList = [i for sub in newList for i in sub]
    return [i for sub in newList for i in sub]

def part_one_stack(string):
    string = list(string)
    stack = [string.pop()]
    while string:
        if not stack:
            stack.append(string.pop())
        if stack[len(stack)-1] == string[len(string)-1].swapcase():
            stack.pop()
            string.pop()
        else:
            stack.append(string.pop())
    return len(stack)
        
def part_two():
    pass