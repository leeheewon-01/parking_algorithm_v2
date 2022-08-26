import random
for _ in range(12):
    print(random.randrange(1000, 9999))
    print(1, end=" ")
    print(random.randrange(10, 23), end=" ")
    print(random.randrange(10, 59))
for _ in range(24):
    print(random.randrange(1000, 9999))
    print(random.randrange(0, 1), end=" ")
    print(random.randrange(10, 23), end=" ")
    print(random.randrange(10, 59))