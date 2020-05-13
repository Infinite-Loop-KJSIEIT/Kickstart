for t in range(int(input())):
    N, Q = map(int, input().split())
    A = input()
    frq = [[0] for i in range(26)]
    for i in A:
        for j in range(26):
            if ord(i)-65 == j:
                frq[j].append(frq[j][-1] + 1)
            else:
                frq[j].append(frq[j][-1])
        
    # for i in frq:
    #     print(*i)
    
    yCount = 0
    for q in range(Q):
        flag = True
        l, r = map(int, input().split())
        count = 0
        if r-l+1 %2 :
            count = 1
        i = 0
        while i < 26 and flag:
            if (frq[i][r] - frq[i][l-1]) % 2:
                count -= 1
                if count < 0:
                    flag = False
                    break
            i += 1
        
        if flag:
            yCount += 1
    
    print("Case #" + str(t+1) + ": " + str(yCount))