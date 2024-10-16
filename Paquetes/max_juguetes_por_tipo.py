
def max_juguetes_por_tipo (inventario):
    maximos= {}

    for item in inventario:
        tipo = item[1]
        cantidad = item [2]
        provincia = item[0]

        if tipo not in maximos or cantidad > maximos [tipo][0]:
            maximos[tipo] = (cantidad,provincia)
            
    return maximos