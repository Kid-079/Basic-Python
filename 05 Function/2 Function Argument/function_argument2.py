# Simple Function Argument
def Student(name):
	print('Student Name : ', name)

Student('Semir Khan')
print('\n')

# Keywords Argument
def Teacher(name,lesson):
	print('Name   : ', name)
	print('Lesson : ', lesson)

Teacher(name='A',lesson='1')
print('\n')
Teacher(lesson='2', name='B')
print('\n')
Teacher('Sports','C') # Wrong Example
print('\n')

# Function use Default Argumen
def Security(name,shift='Morning',condition='Good',signed='No',galak='No'):
	print('Security  : ', name)
	print('Shift     : ', shift)
	print('Condition : ', condition)
	print('Signed    : ', signed)
	print('Galak     : ', galak)

Security('1')
print('\n')
Security('2', condition='Not Good', signed='Yes', galak="Yes")
print('\n')
Security('3', shift="Night")
print('\n')
Security('4', condition='Not Good', signed='Yes', shift='Night', galak='Very Galak')