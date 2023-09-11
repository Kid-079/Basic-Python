# Inheritance Method
class A():

	def __init__(self,name,genre,condition):
		self.name = name
		self.genre = genre
		self.condition = condition

	def check_id_person(self):
		print('name',self.name,'Genre:',self.genre,'Condition:',self.condition)

class Person(A):

	def check_id_person(self):
		print('Check Person')

person_1 = A('name_person_1','name_genre','Ready')
person_2 = Person('name_person_2','name_genre','Not Ready')

# print(person_1.check_id_person())
# print(person_2.check_id_person())

person_1.check_id_person()
person_2.check_id_person()