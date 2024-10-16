
def total_juguetes_por_provincia(inventario):
    total_por_provincia= []
    provincias= []
    
    for item in inventario:
        provincia = item [0]
        cantidad = item[2]
        
        if provincia not in provincias:
            provincias = provincias + [provincia]
            total_por_provincia = total_por_provincia + [provincia, cantidad]
            
        else:
            for total in total_por_provincia:
                if total[0] == provincia:
                    total[1] += cantidad
                    break
                
        return total_por_provincia