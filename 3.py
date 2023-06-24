def skat(A, Na, B, Nb):
    skat = []
    for i in range(Na):
        res = False
        for j in range(Nb):
            if A[i] == B[j]:
                res = True
                break
        if not res:
            skat.append(A[i])
    return skat
