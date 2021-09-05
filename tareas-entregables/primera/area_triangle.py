def area(v):
    return (1/2)*abs((v[1][0]*v[2][1]-v[2][0]*v[1][1]-v[0][0]*v[2][1]+v[2][0]*v[0][1]+v[0][0]*v[1][1]-v[1][0]*v[0][1]))

if __name__ == "__main__":
    vertices = [[0,0],[0,1],[1,0]]
    areaTriangle  = area(vertices);

    print(f'Area of tirangle is {areaTriangle}')