while True:
    try:
        r1, x1, y1, r2, x2, y2 = [int(x) for x in input().split()]
        dist_orig1_orig2 = (((x1-x2)**2)+((y1-y2)**2))**(1/2)
        cond_relacao_circulo = ""
        
        if r2 > r1:
            print('MORTO')
        else:        
            if(dist_orig1_orig2 > r1 + r2):
                cond_relacao_circulo = "externas"
            if(dist_orig1_orig2 == r1 + r2):
                cond_relacao_circulo = "tang_externa"
            if(dist_orig1_orig2 == r1 - r2):
                cond_relacao_circulo = "tang_interna"
            if((dist_orig1_orig2 > r1 - r2) and (dist_orig1_orig2 < r1 + r2)):
                cond_relacao_circulo = "secantes"
            if(dist_orig1_orig2 < r1 - r2):
                cond_relacao_circulo = "internas"

            if ((cond_relacao_circulo == "tang_interna") or (cond_relacao_circulo == "internas")):
                print('RICO')
            else:
                print('MORTO')

    except EOFError:
        break
