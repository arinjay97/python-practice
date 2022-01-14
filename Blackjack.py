def blackjack(a, b, c):
    total = a+b+c
    if total <= 21:
        return total
    else:
        if a == 11 or b == 11 or c == 11:
            total2 = total - 10
            if total2 > 21:
                return 'BUST'
            else:
                return total2
        else:
            return 'BUST'


print(blackjack(5,6,7))
print(blackjack(9,9,9))
print(blackjack(9,9,11))
print(blackjack(11,11,10))