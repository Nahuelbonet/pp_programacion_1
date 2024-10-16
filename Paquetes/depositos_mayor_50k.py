
def depositos_mayor_50k(inventario):
    provincias = []
    
    total_por_provincia = {}
    
    for i in range(len(inventario)):
        provincia = inventario[i][0]
        cantidad = inventario[i][2]


        if provincia in total_por_provincia:
            total_por_provincia[provincia] += cantidad
        else:
            total_por_provincia[provincia] = cantidad


    for provincia, total in total_por_provincia.items():
        if total > 50000:
            provincias += [provincia]

    return provincias
