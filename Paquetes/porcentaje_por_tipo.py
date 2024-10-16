
def porcentaje_por_tipo(inventario):
    total_juguetes = sum(item[2] for item in inventario)
    porcentajes = {}
    
    for item in inventario:
        tipo = item[1]
        cantidad = item[2]
        
        if tipo not in porcentajes:
            porcentajes[tipo] = 0
        porcentajes[tipo] += cantidad
    
    for tipo in porcentajes:
        porcentajes[tipo] = (porcentajes[tipo] / total_juguetes) * 100
    
    return porcentajes