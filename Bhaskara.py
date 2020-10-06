try:
    a, b, c = [float(x) for x in input().split(' ')]

    delta = b**2 - (4 * a * c)

    if(delta < 0) or (a == 0):
        print('Impossivel calcular')
    else:
        raiz1 = (b*(-1) + delta**(1/2))/(2*a)
        raiz2 = (b*(-1) - delta**(1/2))/(2*a)
        print('R1 = {:.5f}\nR2 = {:.5f}'.format(raiz1, raiz2))

except:
    print('Impossivel calcular')
