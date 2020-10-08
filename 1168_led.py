while True:
    try:
        n = int(input())
        if((n >= 1) and (n <= 1000)):
            for item in range(n):
                num = int(input ())
                if((num >= 1) and (num <= 10**100)):
                    led = 0
                    num = str(num)
                    for y in num:
                        if((y == '6') or (y == '9') or (y == '0')):
                            led = led + 6
                        if((y == '2') or (y == '3') or (y == '5')):
                            led = led + 5
                        if(y == '1'):
                            led = led + 2
                        if(y == '7'):
                            led = led + 3
                        if(y == '4'):
                            led = led + 4
                        if(y == '8'):
                            led = led + 7
                    
                    print('{:d} leds'.format(led))
    except EOFError:
        break
