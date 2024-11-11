numbers = [2, 7, 11, 15]
target = 17

index1 = 0
index2 = len(numbers) - 1

while True:
    if numbers[index1] + numbers[index2] == target:
        print(index1+1, index2+1)
        break
    elif numbers[index1] + numbers[index2] < target:
        index1 = index1 + 1
    elif numbers[index1] + numbers[index2] > target:
        index2 = index2 - 1
    else:
        print("False")
        break
