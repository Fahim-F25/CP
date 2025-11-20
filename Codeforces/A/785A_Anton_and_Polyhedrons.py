n = int(input())
totalFaces = 0
for _ in range(n):
    s = input()
    if s == 'Tetrahedron':
        totalFaces += 4
    elif s == 'Cube':
        totalFaces += 6
    elif s == 'Octahedron':
        totalFaces += 8
    elif s == 'Dodecahedron':
        totalFaces += 12
    elif s == 'Icosahedron':
        totalFaces += 20
print(totalFaces)