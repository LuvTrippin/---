# 1 Task
num = 3846.15
rnum = num
rnum /= 10
rnum = round(rnum) * 10
DELTA = abs(rnum - num)
delta = DELTA / abs(rnum)
print("Задача 1")
print(f"Абсолютная погрешность: {DELTA}, Относительая погрешность: {delta}", end="\n\n")

# 2 Task
DELTA = abs(-0.0351) * 13.4
print("Задача 2")
print(f"Абсолютная погрешность: {DELTA}%", end="\n\n")

# 3 Task
DELTA = 0.0048
X = 0.54325
X1 = 0.54325 + 0.0048
X2 = 0.54325 - 0.0048
ans1 = str(round(X - X1, 5)).count("0")
ans2 = str(round(X - X2, 5)).count("0")
print("Задача 3")
print(f"Количество верных цифр в X1: {ans1}, количество верных цифр в X2: {ans2}", end="\n\n")

# 4 Task

X = 0.07281
delta = 1.43/100

DELTA = X * delta

X1 = X + DELTA
X2 = X - DELTA

ans1 = str(round(X - X1, 9)).count("0")
ans2 = str(round(X - X2, 9)).count("0")
print("Задача 4")
print(f"Количество верных цифр в X1: {ans1}, количество верных цифр в X2: {ans2}")
