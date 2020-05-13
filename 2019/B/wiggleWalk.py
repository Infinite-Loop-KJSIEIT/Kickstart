def cmdW(row, col):
    currRangeIdx = None
    for i in range(len(rows[row])):
        if col in rows[row][i]:
            currRangeIdx = i
            break
    
    dest = rows[row][currRangeIdx][0] - 1
    destIdx = None
    for i in range(len(rows[row])):
        if dest in rows[row][i]:
            destIdx = i
            break
    
    while destIdx is not None:
        currTemp = rows[row][currRangeIdx]
        currDest = rows[row][destIdx]
        newRange = [currDest[0], currTemp[1]]
        rows[row].pop(currRangeIdx)
        rows[row].pop(destIdx)
        rows[row].append(newRange)
        currRangeIdx = len(rows[row]) - 1
        dest = newRange[0] - 1
        destIdx = None
        for i in range(len(rows[row])):
            if dest in rows[row][i]:
                destIdx = i
                break
    
    rows[row][currRangeIdx][0] -= 1
    destCol = rows[row][currRangeIdx][0]
    
    cols[destCol].append([row, row])
    # print(x, destCol)
    return (x, destCol)

def cmdE(row, col):
    currRangeIdx = None
    for i in range(len(rows[row])):
        if col in rows[row][i]:
            currRangeIdx = i
            break
    
    dest = rows[row][currRangeIdx][1] + 1
    destIdx = None
    for i in range(len(rows[row])):
        if dest in rows[row][i]:
            destIdx = i
            break
    
    while destIdx is not None:
        currTemp = rows[row][currRangeIdx]
        currDest = rows[row][destIdx]
        newRange = [currTemp[0], currDest[1]]
        rows[row].pop(currRangeIdx)
        rows[row].pop(destIdx)
        rows[row].append(newRange)
        currRangeIdx = len(rows[row]) - 1
        dest = newRange[1] + 1
        destIdx = None
        for i in range(len(rows[row])):
            if dest in rows[row][i]:
                destIdx = i
                break
    
    rows[row][currRangeIdx][1] += 1
    destCol = rows[row][currRangeIdx][1]
    
    cols[destCol].append([row, row])
    # print(x, destCol)
    return (x, destCol)

def cmdN(row, col):
    currRangeIdx = None
    for i in range(len(cols[col])):
        if row in cols[col][i]:
            currRangeIdx = i
            break
    
    dest = cols[col][currRangeIdx][0] - 1
    destIdx = None
    for i in range(len(cols[col])):
        if dest in cols[col][i]:
            destIdx = i
            break
    
    while destIdx is not None:
        currTemp = cols[col][currRangeIdx]
        currDest = cols[col][destIdx]
        newRange = [currDest[0], currTemp[1]]
        cols[col].pop(currRangeIdx)
        cols[col].pop(destIdx)
        cols[col].append(newRange)
        currRangeIdx = len(cols[col]) - 1
        dest = newRange[0] - 1
        destIdx = None
        for i in range(len(cols[col])):
            if dest in cols[col][i]:
                destIdx = i
                break
    
    cols[col][currRangeIdx][0] -= 1
    destRow = cols[col][currRangeIdx][0]
    
    rows[destRow].append([col, col])
    # print(destRow, col)
    return (destRow, col)

def cmdS(row, col):
    currRangeIdx = None
    for i in range(len(cols[col])):
        if row in cols[col][i]:
            currRangeIdx = i
            break
    
    dest = cols[col][currRangeIdx][1] + 1
    destIdx = None
    for i in range(len(cols[col])):
        if dest in cols[col][i]:
            destIdx = i
            break
    
    while destIdx is not None:
        currTemp = cols[col][currRangeIdx]
        currDest = cols[col][destIdx]
        newRange = [currTemp[0], currDest[1]]
        cols[col].pop(currRangeIdx)
        cols[col].pop(destIdx)
        cols[col].append(newRange)
        currRangeIdx = len(cols[col]) - 1
        dest = newRange[1] + 1
        destIdx = None
        for i in range(len(cols[col])):
            if dest in cols[col][i]:
                destIdx = i
                break
    
    cols[col][currRangeIdx][1] += 1
    destRow = cols[col][currRangeIdx][1]
    
    rows[destRow].append([col, col])
    # print(destRow, col)
    return (destRow, col)

for t in range(int(input())):
    N, R, C, x, y = map(int, input().split())
    path = input()
    rows = [[] for i in range(R)]
    cols = [[] for i in range(C)]
    x -= 1
    y -= 1
    rows[x].append([y, y])
    cols[y].append([x, x])
    # print("         ", end = "")
    # for i in cols:
    #     print(i, end = "  ")
    # print()
    # for i in rows:
    #     print(i)
    for k in range(len(path)):
        if path[k] == 'E':
            x, y = cmdE(x, y)
        if path[k] == 'W':
            x, y = cmdW(x, y)
        if path[k] == 'N':
            x, y = cmdN(x, y)
        if path[k] == 'S':
            x, y = cmdS(x, y)
        # print("         ", end = "")
        # for i in cols:
        #     print(i, end = "  ")
        # print()
        # for i in rows:
        #     print(i)
    print("Case #" + str(t+1) + ": " + str(x+1) + " " + str(y+1))