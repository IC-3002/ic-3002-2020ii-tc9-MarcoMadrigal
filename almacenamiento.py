def maximizar(As, D):

    lista_ordenada = sorted(As, key=segundo)
    peso = 0
    M = []

    for x in range(len(As)):
        
        if peso+lista_ordenada[x][1] <=D:
            peso += lista_ordenada[x][1]
            M.append(lista_ordenada[x])

        else:
            break

    return M


def segundo(elemento):

    return elemento[1]