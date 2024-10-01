planets = [('수성', 2439, 0.4), ('금성', 6052, 0.7), ('태양', 695000, 0),
          ('지구', 6378, 1), ('화성', 3390, 1.5), ('목성', 71492, 5.2)]

print('태양계 행성의 크기(반지름)로 정렬')
planets.sort(key = lambda radius: radius[1], reverse= 1)
print(planets)

print('태양계 행성의 태양과의 거리로 정렬')
planets.sort(key = lambda distance: distance[2])
print(planets)