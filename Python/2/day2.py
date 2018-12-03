import collections
import numpy

with open("input.txt") as file:
    lines = str(file.read()).splitlines()

def part_one(lst):
    twos = []
    threes = []
    for item in lst:
        counts = collections.Counter(item)
        if 2 in counts.values():
            twos.append(item)
        if 3 in counts.values():
            threes.append(item)
    return len(twos)*len(threes)

def compare_differences(npArr1,npArr2):
    differences = npArr1 == npArr2
    return collections.Counter(differences)

def part_two(lst):
    numpyArrays = [numpy.array(list(x)) for x in lst]
    for i in range(len(numpyArrays)):
        for j in range(len(numpyArrays)):
            if i != j:
                differences = compare_differences(numpyArrays[i],numpyArrays[j])
                if differences[False] < 2:
                    print(''.join([x for x in numpyArrays[i] if x in numpyArrays[j]]))

if __name__ == "__main__":
    print(part_two(lines))
