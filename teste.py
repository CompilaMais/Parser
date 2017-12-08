string_teste ='''SampleData = {
      BT0M7A1 1        184 151 250 256
                       184 151 254 284
      BT0M8A2 1        184 116 250 260
                       184 151 278 288
      BT0M9A3 1        180 157 254 260
                       180 157 254 260
      BT0M1A4 1        179 116 318 368
                       179 116 318 368
      BT0M2A5 1        184 116 254 260
                       184 116 254 260
      BT0M3A6 1        184 157 310 256
                       184 157 310 256
      BT0M4A7 1        184 116 310 260
                       184 116 310 288
      BT0M5A8 1        184 116 250 260
                       184 116 250 284
      BT0M6A9 1        184 116 254 256
                       184 116 254 288
    BT0M64A10 2        184 157 250 296
                       184 157 250 296
    BTOM73A11 1        184 116 250 260
                       184 116 250 260
   BT0M104A12 1        180 157 278 288
                       184 157 278 288
   BT0M118A13 1        180 157 314 288
                       180 157 314 288
   BT0M119A14 2        184 157 314 260
                       184 157 314 260
   BT0M125E15 1        180 157 250 300
                       180 157 250 300
   BT0M127E16 1        180 116 250 368
                       180 116 250 368
   BT0M128E17 1        184 157 254 296
                       184 157 254 296
    BT0M11A19 1        180 116 254 260
                       184 116 314 260
    BT0M12A20 1        184 157 254 288
                       184 157 254 288
    BT0M13A21 1        180 157 310 256
                       180 157 310 280
    BT0M14A22 1        184 116 310 296
                       184 116 310 296
    BT0M15A23 1        184 116 250 260
                       184 116 250 300
   BT0M108A25 1        184 116 250 256
                       184 157 314 288
   BT0M109A26 1        184 116 310 260
                       184 116 310 260
   BT0M126E27 1        184 116 274 260
                       184 116 310 288
   BT0M140E28 1        180 157 250 256
                       184 157 314 368
  }
  '''


def funcao(string):
    teste = string.split(" ")
    lista = []

    # print(teste)
    for letter in teste:
        if letter != '':
            lista.append(letter)

    lista_final = []
    print(lista)

    print("Tamanho lista: %s",len(lista))
    x = 3
    while x < len(lista):
        var = []
        var.append(lista[x])
        var.append(lista[x+1])
        var.append(lista[x+2])
        var.append(lista[x+3])
        var.append(lista[x+4])
        var.append(lista[x+5])
        var.append(lista[x+6])
        var.append(lista[x+7])
        var.append(lista[x+8])
        var.append(lista[x+9])

        lista_final.append(var)

        print("==========")
        print(var)
        print("==========")

        if(x+11 >= len(lista)):
            break
        else:
            x = x + 10

    print(lista_final)


funcao(string_teste)
