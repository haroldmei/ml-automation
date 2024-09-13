def reorganize(li, K):
    num1 = 0
    num2 = 0
    for i in range(len(li)):
        if li[i] < K:
            num1 += 1
        if li[i] > K:
            num2 += 1

    i, j = 0, num1
    #for i in range(len(li)):
    while i < len(li):
        #print(li)
        if i >= num1 and i < len(li) - num2:
            i += 1
            continue

        if li[i] == K:
            if li[j] != K:
                li[i], li[j] = li[j], li[i]
            j += 1
            #print(i, j, li)
        else:
            i += 1

    #print(li, num1, num2)

    i = 0
    j = len(li) - 1
    while True:
        if i >= num1 and j <= len(li) - num2:
            break
        if li[i] < K:
            i += 1
            continue
        if li[j] > K:
            j -= 1
            continue
        li[i], li[j] = li[j], li[i]
        i += 1
        j -= 1
    
    for i in range(num1, len(li) - num2):
        li[i] = K
    
    return li

L = [7,0,6,4,10,7,3,-4,3,12] 
K = 7

import random
for i in range(10000):
    a1, a2, a3 = random.randint(1,1000), random.randint(1,1000), random.randint(1,1000)
    #print(a1,a2,a3)
    l1 = random.sample(range(10000), a1)
    l2 = random.sample(range(10001, 20000), a2)
    lK = [10000] * a3

    ll = l1 + l2 + lK
    random.shuffle(ll)
    ll = reorganize(ll, 10000)

    l11 = ll[:a1]
    l12 = ll[-a2:]
    
    for i in range(len(l11)):
        assert(l11[i] < 10000)
    
    for i in range(len(l12)):
        assert(l12[i] > 10000)

print('successful')