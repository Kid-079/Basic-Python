access_number = 60

for i in range(0,50):
	print(i)

	if i is access_number:
		print('Identified', i, 'Access Number')
		break
else:
	print('Cannot Access, Number Not Identified')

print("Progress Outside Loop")