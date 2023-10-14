numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

ind = numbers.index(None)
numbers.pop(ind)
numbers.insert(ind, sum(numbers) / (len(numbers) + 1))

print("Измененный список:", numbers)
