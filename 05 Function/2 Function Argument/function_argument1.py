# Simple Function Argument
def Student(name):
	print('Student Name : ', name)

Student('Semir Khan')
print('\n')

# Keywords Argument
def Teacher(name,lesson):
	print('Name   : ', name)
	print('Lesson : ', lesson)

Teacher(name='Pasqualito',lesson='Read and Write')
print('\n')
Teacher(lesson='Cooking', name='Kripik Khan')
print('\n')
Teacher('Read and Write','Suraj') # Wrong Example
print('\n')

# Function use Default Argumen
def Security(name,shift='Morning',galak='No'):
	print('Security : ', name)
	print('Shift    : ', shift)
	print('Galak    : ', galak)

Security('1')
print('\n')
Security('2', galak="Very Very Galak")
print('\n')
Security('3', shift="Night")
print('\n')
Security('4', shift='Night', galak='Yes')

