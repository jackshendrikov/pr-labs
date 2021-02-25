while True:
    try:
        n = int(input("Enter N: "))
    except ValueError:
        print("Enter correct number!")
    else:
        if n <= 100:
            print("Error: N must be greater than 100!")
        else:
            for i in range(11, n + 1):
                s = i
                i = (i-1) + i*i
                if i < 11:
                    i = 10
                print(i)
            break
