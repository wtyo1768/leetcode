

amount = 2
coins = [1]
outputs = [0] + [1e4] * (amount)



for i, goal in enumerate(range(amount+1)):
    for input in coins:
        if goal+input<=amount:

            outputs[goal+input] = min(outputs[goal+input], outputs[i]+1)


print(outputs)
if outputs[amount]==1e4:
    print('outputs', -1)
else:
    print('outputs', outputs[amount])