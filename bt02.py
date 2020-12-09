def Sort(A,p,r):
    if p < r:
        q = (p+r)//2
        Sort(A,p,q)
        Sort(A,q+1,r)
        Merge(A,p,q,r)
    return()


def Merge(A,p,q,r):   # функция, объединяющая и сортирующая две уже отсортированные части списка: A[p:q], A[q+1:r]
    A3 = [] # временный список для формирования общего отсортированного списка для двух списков A[p:q], A[q+1:r]
    i = p-1
    i1 = p-1   # счетчик значений списка A[p:q]
    i2 = q   # счетчик значений списка A[q+1:r]
    while i < r:
        while i1 < q and i2 < r:
            if A[i1] <= A[i2]: # сравниваем минимальные значения списков A[p:q] и A[q+1:r], отправляем минимум в А3
                A3.append(A[i1])
                i1 += 1
            else:
                A3.append(A[i2])
                i2 += 1
            i += 1
        if i1 == q:  # проверяем, закончилась ли раньше первая часть списка A[p:q]
            A3.append(A[i2]) # отправляем в А3 оставшиеся значения списка A[q+1:r]
            i2 += 1
        else:
            A3.append(A[i1])  # отправляем в А3 оставшиеся значения списка A[p:q]
            i1 += 1
        i += 1
    i4 = p
    i5 = 0
    while i4 <= r:
        A[i4-1] = A3[i5]
        i5+=1
        i4+=1
    return()

A = [5,2,4,6,1,3,2,6]
Sort(A,1,len(A))
print(A)
