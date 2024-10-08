while True:
    N = int(input())
    if N == 0:
        break 

    pA = 0
    pB = 0

    for _ in range(N):
        A, B = map(int, input().split())
        if A > B:
            pA += 1 
        elif B > A:
            pB += 1 



    print(pA, pB)