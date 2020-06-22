my_list = [1, 2, 3, 5, 6, 11, 12, 18, 19, 21]
prime_numbers = []
for item in my_list:
  if item == 2:
    prime_numbers.append(item)
  if item % 2 == 0 or item <= 1:
    continue

  if item > 2:  
    range_limit = int(item**0.5) + 1
    for divider in range(3, range_limit, 2):
        if item % divider == 0:
          continue
    prime_numbers.append(item)
for item in prime_numbers:
  print(item)
print("Martwa Papuga")
