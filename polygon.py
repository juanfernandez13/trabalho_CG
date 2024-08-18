import numpy as np

def scanline(points):
    npArr = np.array(points)
    #remove repetições
    npArr = np.unique(npArr, axis=0)
    #ordena
    np.sort(npArr)

    intersections = []
    #faz um range entre todos os pontos da borda
    for i in range(0, len(npArr)-1):
        #Ver o próximo elemento está na mesma coluna mas em linhas diferentes
        if(npArr[i][0] == npArr[i+1][0]):
            #Adiciona todos os elementos não foram adicionados
            for j in range(npArr[i][1], npArr[i+1][1]+1):
                intersections.append((npArr[i][0], j))

    return np.unique(intersections, axis=0)
