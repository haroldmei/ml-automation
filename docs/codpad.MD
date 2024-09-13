You are given a list of bombs. The range of a bomb is defined as the area where its effect can be felt. This area is in the shape of a circle with the center as the location of the bomb.

The bombs are represented by a 0-indexed 2D integer array bombs where bombs[i] = [xi, yi, ri]. xi and yi denote the X-coordinate and Y-coordinate of the location of the ith bomb, whereas ri denotes the radius of its range.

You may choose to detonate a single bomb. When a bomb is detonated, it will detonate all bombs that lie in its range. These bombs will further detonate the bombs that lie in their ranges.

Given the list of bombs, return the maximum number of bombs that can be detonated if you are allowed to detonate only one bomb.


bombs[i] = [xi, yi, ri]

Number of bombs: n

Brute force
1. for each bomb, find bombs within range: O(n^2)
2. for each bomb, detonate: O(nlogn)

def getWithinRange(b, bombs):
    withinSquare = []
    withinRange = []
    for i in bombs:
        if i[0] >= b[0] - b[2] and i[0] <= b[0] + b[2] and i[1] >= b[1] - b[2] and i[1] <= b[1] + b[2]:
            withinSquare.append(i)
    
    for i in withinSquare:
        if (i[0]-b[0])**2 + (i[1]-b[1])**2 <= b[2]**2:
            withinRange.append(i)
    return withinRange

def getDetonate(b, withinRanges, cached = {}):
    if b in cached:
        return cached[b]

    detonated = withinRanges[b]
    visited = set([])
    while detonated:
        cur = detonated.pop(0)
        if cur in visited:
            continue
        visited.add(cur)
        detonated += withinRanges[cur]

    cached[b] = detonated
    return detonated

def maximumDetonation(self, bombs: List[List[int]]) -> int:
    #preproc
    withinRanges = {}
    for b in bombs:
        cur = getWithinRange(b, bombs)
        withinRanges[b] = cur

    detonated = {}
    maxlen = 0
    for b in bombs:
        cur = getDetonate(b, withinRanges, detonated)
        if maxlen > len(cur):
            maxlen = len(cur)

    return maxlen
