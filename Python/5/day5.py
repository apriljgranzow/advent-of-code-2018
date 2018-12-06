with open("input5.txt") as file:
    chain = file.read()

def part_one(string):
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
        
def filter_letter(letter,string):
    newList = []
    for char in string:
        if char != letter and char != letter.swapcase():
            newList.append(char)
    return newList       

def part_two(string):
    letters = {chr(i) : part_one(filter_letter(chr(i),string)) for i in range(97,123)}
    return min(letters.values())

if __name__ == "__main__":
    print(part_two(chain))