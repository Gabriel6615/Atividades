while True:
    while True:
        nota1 = float(input())
        if 0 <= nota1 <= 10:
            break
        else:
            print("nota invalida")
    
    while True:
        nota2 = float(input())
        if 0 <= nota2 <= 10:
            break
        else:
            print("nota invalida")
    
    media = (nota1 + nota2) / 2
    print(f"media = {media:.2f}")
    
    while True:
        print("novo calculo (1-sim 2-nao)")
        opcao = int(input())
        if opcao == 1 or opcao == 2:
            break
    
    if opcao == 2:
        break