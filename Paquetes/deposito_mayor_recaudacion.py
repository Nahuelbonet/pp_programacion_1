
def deposito_mayor_recaudacion(inventario, precios):
    recaudacion = {}
    
    for item in inventario:
        provincia = item[0]
        tipo = item[1]
        cantidad = item[2]
        
        if provincia not in recaudacion:
            recaudacion[provincia] = 0
        recaudacion[provincia] += cantidad * precios[tipo]

    mayor_recaudacion = -1
    provincia_mayor = ""
    
    for provincia in recaudacion:
        total = recaudacion[provincia]
        
        if total > mayor_recaudacion:
            mayor_recaudacion = total
            provincia_mayor = provincia
    
    return provincia_mayor