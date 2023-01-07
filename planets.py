def planets(planetSize, c, orbits):
    planetDict = {}
    count = 0
    for element in orbits:
        planetDict[element] = 1 + planetDict.get(element, 0)
        
    for planet in planetDict:
        if planetDict[planet] < c:
            count += planetDict[planet]
        else:
            count += c
    
    print(count)
size = int(input())
for _ in range(size):
    planetSize, c = map(int, input().split(" "))
    orbits = list(map(int, input().split(" ")))
    planets(planetSize, c, orbits)
