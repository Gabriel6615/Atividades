def main():
    dia_inicio = input().split()
    hora_inicio = input().split(" : ")
    dia_fim = input().split()
    hora_fim = input().split(" : ")
    
    dia_i = int(dia_inicio[1])
    hora_i, min_i, seg_i = map(int, hora_inicio)
    
    dia_f = int(dia_fim[1])
    hora_f, min_f, seg_f = map(int, hora_fim)
    
    total_seg_inicio = seg_i + min_i*60 + hora_i*3600 + dia_i*86400
    total_seg_fim = seg_f + min_f*60 + hora_f*3600 + dia_f*86400
    
    diferenca_seg = total_seg_fim - total_seg_inicio
    
    dias = diferenca_seg // 86400
    resto = diferenca_seg % 86400
    
    horas = resto // 3600
    resto %= 3600
    
    minutos = resto // 60
    segundos = resto % 60
    
    print(f"{dias} dia(s)")
    print(f"{horas} hora(s)")
    print(f"{minutos} minuto(s)")
    print(f"{segundos} segundo(s)")

if __name__ == "__main__":
    main()