

def area(L,W):
    areaValue=L*W
    return areaValue

def perimeter(L,W):
    perimeterValue=((2*L)+(2*W))
    return perimeterValue

def volume(L,W,H):
    volumeValue=(L*W*H)
    return volumeValue

def surfaceArea(L,W,H):
    surfaceAreaValue = ((L*W*2)+(L*H*2)+(W*H*2))
    return surfaceAreaValue





assert area(10,10) == 100
assert area(0,9999) == 0
assert area(5,8) == 40
assert perimeter(10,10 == 40)
assert perimeter(0, 9999) == 19998
assert perimeter(5,8) == 26
assert volume(10,10,10) == 1000
assert volume(9999,0,9999) == 0
assert volume(5,8,10) == 400
assert surfaceArea(10,10,10) == 600
assert surfaceArea(9999,0,9999) == 199960002
assert surfaceArea(5,8,10) == 340