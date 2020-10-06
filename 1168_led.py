while True:
    try:
        n = int(input())
        for x in range (0, n):
            num = str(input())
            print(len(num))
    except EOFError:
        break
