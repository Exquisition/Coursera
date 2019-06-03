from math import floor, ceil


def karasutba(x, y):


    # base case for recursion, single digit number
    if x < 10 and y < 10:
        return x * y

    n = len(str(x))
    nOver2 = int(ceil(float(n)/2))

    # compute the higher order and lower order bits of number
    a = int(floor(x / 10 ** nOver2))
    b = int(x % (10 ** nOver2))

    c = int(floor(y / 10 ** nOver2))
    d = int(y % (10 ** nOver2))

    # 3 recursive calls instead of 4
    step1 = karasutba(a, c)
    step2 = karasutba(b, d)
    step3 = karasutba(a+b, c+d)

    # applying gauss trick to compute ab + cd
    gauss_trick = step3 - step2 - step1

    answer = pow(10, n)*step1 + pow(10, nOver2)*gauss_trick + step2

    return answer


print(karasutba(5678, 1234))
print(5678*1234)