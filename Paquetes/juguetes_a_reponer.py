
def juguetes_a_reponer(inventario):
    a_reponer = []
    
    for item in inventario:
        if item[2] < 500:
            a_reponer = a_reponer + [item]
            
    return a_reponer