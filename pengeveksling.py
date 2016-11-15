from sys import stdin

Inf = 1000000000


def min_coins_greedy(coins, value):
    # SKRIV DIN KODE HER
    if value == 0:
        return 0
    if r[value] < Inf:
        return r[value]

    for c in coins:
        if c <= value:
            return 1 + min_coins_greedy(coins, value - c)
    


def min_coins_dynamic(coins, value):
    # SKRIV DIN KODE HER
    # return min_coins_bottom(coins, value)
    return min_coins_memo(coins, value, r)


def min_coins_memo(coins, value, r):
    if r[value] < Inf:
        return r[value]
    best = Inf
    for c in coins:
        if c <= value:
            best = min(best, 1 + min_coins_memo(coins, value - c, r))
    r[value] = best
    # print("best =", best, "value =", value)
    return best


def min_coins_bottom(coins, value):
    
    for i in range(value+1):
        for c in coins:
            if i < c:
                break
            r[i] = min(r[i], 1 + r[i-c])
    
    return r[value]
        



def can_use_greedy(coins):
    # bare returner False her hvis du ikke klarer aa finne ut
    # hva som er kriteriet for at den graadige algoritmen skal fungere
    # SKRIV DIN KODE HER
    
    # for i in range(len(coins)-1):
    #     if coins[i] / 2 != coins[i+1]:
    #         return False
    
    sum = 0
    for c in coins:
        if c <= sum:
            return False
        sum += c

    return True
        
    # return coins[-1]*2 == sum


coins = []
for c in stdin.readline().split():
    coins.append(int(c))
coins.sort()
coins.reverse()

method = stdin.readline().strip()
values = []
for line in stdin:
    values.append(int(line))
maxvalue = max(max(values), max(coins))
r = [Inf]*(maxvalue+1)
r[0] = 0
for c in coins:
    r[c] = 1

for i in range(coins[-1]):
    r[i] = 0
# print(coins)
if method == "graadig" or (method == "velg" and can_use_greedy(coins)):
    for value in values:
        print(min_coins_greedy(coins, value))
else:
    for value in values:
        print(min_coins_dynamic(coins, value))
# print(r)
