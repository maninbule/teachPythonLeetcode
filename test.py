



x = 17
isPrime = True
for y in range(2,x):
    if x % y == 0:
        isPrime = False
        break
if isPrime:
    print("yes")
else:
    print("no")