for i in range(10):
	if i%2 == 0: continue
	elif i%7 == 0: break
	else: print(i)
else:
	print('end')


print("\n2........")

for i in range(3, 12, 4):
	print(i+5, end=' ')
else:
	print('end')

print("3.....")
for i in range(8, 2, -2):
	print(i+1)
	if i == 9 : break

print('range(0-5)')
x=0
for i in range (0,5):
    x+=i
print (x)
