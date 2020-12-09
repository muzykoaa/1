def Merge(A,p,q,r):   # функция, объединяющая и сортирующая две уже отсортированные части списка: A[p:q], A[q+1:r]
    top_border2 = r
    if q < r-1:
        q2 = (q + r) // 2
        top_border1 = Merge(A, p, q, q2)
        top_border2 = Merge(A, top_border1+1, q2, r)
    elif q < r:
        top_border2 = Insert_its_place(A, p, r)
    else:
        top_border2 = r
    return (top_border2)

def Sort(A, p, r):
    if p < r:
        q = (p + r) // 2
        Sort(A, p, q)
        Sort(A, q + 1, r)
        Merge(A, p, q, r)
    return ()

def Insert_its_place(A, p, r):   # функция, ранжирующая элемент A[r] в возрастающий список A[p:r-1]
    q = (p + r) // 2
    result = r
    while q < r:
        if A[r-1] < A[q-1]:
            result = q
            A.insert(result - 1, A[r - 1])
            A.pop(r)
            r = result
            if q > p:
                result = Insert_its_place(A, p, q)
        else:
            if q < r - 1:
                result = Insert_its_place(A, q+1, r)
                q = (q + r + 1) // 2
            elif A[r-1] < A[q-1]:
                result = q
                A.insert(q - 1, A[r - 1])
                A.pop(r)
                r = q
            else:
                r = q
    return(result)

A = [5,2,4,6,1,3,2,6]
Sort(A,1,len(A))
print(A)