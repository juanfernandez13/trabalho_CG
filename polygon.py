import numpy as np

def scanline(points):
    npArr = np.array(points)
    npArr = np.unique(npArr, axis=0)
    np.sort(npArr)

    intersections = []
    for i in range(0, len(npArr)-1):
        if(npArr[i][0] == npArr[i+1][0]):
            #print("Na linha ",  npArr[i][0], "as colunas variam de ", npArr[i][1], " ATE ", npArr[i+1][1] )
            for j in range(npArr[i][1], npArr[i+1][1]+1):
                intersections.append((npArr[i][0], j))

    return np.unique(intersections, axis=0)
