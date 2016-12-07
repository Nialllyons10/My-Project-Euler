def largePalindrome():
  lst = []
  for i in range(100, 999):
    for j in range(100, 999):
      num = i * j
      if str(num) == str(num)[::-1]:
        lst.append(num)

	print(max(lst))
