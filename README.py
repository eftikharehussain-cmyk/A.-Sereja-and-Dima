# A.-Sereja-and-Dima
n = int(input())
lst = list(map(int, input().split()))
lst1 = []
lst2 = []
lst3 = []
for i in range(n):
	_max = max(lst[0], lst[-1])
	if i % 2 == 0:
		lst1.append(_max)
		if lst[-1] == _max:
			x = lst.pop(-1)
		else:
			x = lst.pop(0)
	else:
		lst2.append(_max)
		if lst[-1] == _max:
			x = lst.pop(-1)
		else:
			x = lst.pop(0)
sereja = sum(lst1)
dima = sum(lst2)
lst3.append(sereja)
lst3.append(dima)
print(*lst3)
