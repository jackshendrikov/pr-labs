from random import randrange
try:
    size = int(input("Enter array size: "))
except ValueError:
    print("Enter correct size!")
else:
    a = [randrange(10, 100) for i in range(size)]
    print("Generated List: ", a)
    a.append(0)
    b, count = [], 1

    for i in range(size):
        b.append(a[i])
        if a[i + 1] > a[i]: count += 1
        elif count > 1:
            b.append(count)
            count = 1

    print("New List: ", list(map(lambda x: x, b)), '\n' + '-'*50)
    print('Sum of elements in list - ', sum(b))
