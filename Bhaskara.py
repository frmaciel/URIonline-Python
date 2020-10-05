def isFloat(num): 
	try: 
		float(str(num)) 
		return True 
	except ValueError: 
		return False


try:
    # str_a = input('Insira o valor do A: ')
    # while(not isFloat(str_a)):
        #print("Insira valores float")
    #     str_a = input('Insira o valor do A: ')

    # str_b = input('Insira o valor do B: ')
    # while(not isFloat(str_b)):
    #     print("Insira valores float")
    #     str_b = input('Insira o valor do B: ')

    # str_c = input('Insira o valor do C: ')
    # while(not isFloat(str_c)):
    #     print("Insira valores float")
    #     str_c = input('Insira o valor do C: ')

    a = float(input('Insira o valor do A: '))
    b = float(input('Insira o valor do B: '))
    c = float(input('Insira o valor do C: '))
    # a = float(str_a)
    # b = float(str_b)
    # c = float(str_c)

    delta = b**2 - (4 * a * c)
    

except:
    print("Impossível calcular")


else:
    if(delta < 0) or ((2*a) == 0):
        print("Impossível calcular")
    else:
        raiz1 = (b*(-1) + delta**(1/2))/(2*a)
        raiz2 = (b*(-1) - delta**(1/2))/(2*a)
        print("R1 = {:.5f}".format(raiz1))
        print("R2 = {:.5f}".format(raiz2))
