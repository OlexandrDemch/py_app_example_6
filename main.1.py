nums = list(map(int, input("Нажмите enter для старта ").split()))

print(nums)

what = int(input("suma - 1 \n dobutok - 2 \n"))

if what == 1:
    print(f"Введите 3 числа через enter")
    a = int(input())
    b = int(input())
    c = int(input())
    print(a + b + c)

elif what == 2:
    print(f"Введите 3 числа через enter")
    a = int(input())
    b = int(input())
    c = int(input())
    print(a * b * c)
