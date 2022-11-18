nums = list(map(int, input("Введите 3 числа через пробел: ").split()))

print(nums)

what = int(input("Максимум - 1 \n Минимум - 2 \n Среднее - 3\n"))

if what == 1:

    print(f"Максимальное: {max(nums)}")

elif what == 2:

    print(f"Минимальное: {min(nums)}")

elif what == 3:

    print(f"Среднее: {sum(nums) / len(nums)}")