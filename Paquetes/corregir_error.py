
def corregir_error(inventario):
    corregido = []
    
    for item in inventario:
        if item[2] >= 0:
            corregido = corregido + [item]
            
    return corregido