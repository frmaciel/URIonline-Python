while True:
    try:
        n = int(input())
        for x in range (n):
            num = str(input())
            led = 0
            z = len(num)
            for y in range(z):
                if((num[y] == 6) or (num[y] == 9) or (num[y] == 0)):
                    led = led + 6
                if((num[y] == 2) or (num[y] == 3) or (num[y] == 5)):
                    led = led + 5
                if(num[y] == 1):
                    led = led + 2
                if(num[y] == 7):
                    led = led + 3
                if(num[y] == 4):
                    led = led + 4
                if(num[y] == 8):
                    led = led + 7
            
            print('{:d} leds'.format(led))
    except EOFError:
        break
