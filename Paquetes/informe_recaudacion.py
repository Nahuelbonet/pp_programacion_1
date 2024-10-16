def ordenar_por_insercion(recaudacion):
    sorted_list = []
    
    for value in recaudacion:
        sorted_list = sorted_list + [value]
        
        for i in range(len(sorted_list) - 1, 0, -1):
            if sorted_list[i] > sorted_list[i - 1]:
                sorted_list[i], sorted_list[i - 1] = sorted_list[i - 1], sorted_list[i]
            else:
                break
            
    return sorted_list