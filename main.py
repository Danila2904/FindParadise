from random import randint

plane_size = 20
plane = [0] * plane_size
######
paradise_count = 0

# забиваем массив матрицей нулей
for i in range(plane_size):
    plane[i] = [0] * plane_size

# генерируем острова
for y in range(plane_size - 2):
    for x in range(plane_size - 2):
        plane[y+1][x+1] = randint(0, 1)
        print(plane[y+1][x+1], end=" ")
    print()


def find(x: int, y: int) -> None:
    if plane[y][x] == 1:
        plane[y][x] = 0
        find(x+1, y)
        find(x-1, y)
        find(x, y+1)
        find(x, y-1)


for y in range(plane_size):
    for x in range(plane_size):
        if plane[y][x] == 1:
            find(x, y)
            paradise_count += 1

# выводим посмотреть

print(paradise_count)

