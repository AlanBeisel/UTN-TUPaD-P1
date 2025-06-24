def funcion_s(vector, largo):
    total = 0
    if largo == 0:
        total = 0
    else:
        total = vector[largo - 1] + funcion_s(vector, largo - 1)
    return total

vector = [0] * 100
vector[0] = 1
vector[1] = 1
vector[2] = 1
vector[3] = 2
vector[4] = 1
largo = 6

print(funcion_s(vector, largo - 1))