idRanges = []

def part1():
    isRange = True
    count = 0
    with open('day5/test2.txt', 'r') as file:
        for line in file:
            if (line.strip()==""):
                isRange = False  
                idRanges.sort(key=lambda t: (t[0], t[1]))                
            elif isRange:
                idRanges.append(parseRange(line.strip()))
            else:
                if(idInRanges(int(line.strip()), idRanges)):
                    count+=1
    print(count)


def parseRange(rangeStr):
    parts = rangeStr.split('-')
    start = int(parts[0])
    end = int(parts[1])
    return (start, end)

def inRange(id, rangeTuple):
    return rangeTuple[0] <= id <= rangeTuple[1]

def idInRanges(id, ranges):
    for rangeTuple in ranges:
        if inRange(id, rangeTuple):
            return True
    return False

part1()

def mergeRanges(ranges):
    if(len(ranges)<=1):
        return ranges
    res = []
    for i in range(len(ranges)-1):
        start = ranges[i][0]
        end = ranges[i][1]

        if (len(res)>0 and res[-1][0]<= start and res[-1][1]>=end):
            continue
    
        for j in range(i+1, len(ranges)):
            if (ranges[j][0]<= end):
                end = max(ranges[j][1], end)
        
        res.append((start,end))
    return res
    
def part2():
    if not idRanges:
        return 0
    sorted_ranges = sorted(idRanges, key=lambda t: (t[0], t[1]))
    merged = mergeRanges(sorted_ranges)
    total = 0
    for r in merged:
        total += r[1] - r[0] + 1
    return total

    
print(part2())