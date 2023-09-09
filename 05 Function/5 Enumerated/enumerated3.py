# Combine 2 list in one loop

superheroes = [ 'Kamen Rider',
				'Ultaramang',
				'Supermen',
				'Mak Lemper',
				'Wiro Sableng'  # Create List superheroes_name to show this superheroes  
			  ]

superheroes_name = [ 'A',
		             'B',
		             'C',
		             'D',
		             # 'E'     # Create List superheroes_name
			       ]      

for heroes, name in zip(superheroes,superheroes_name):
	print(heroes,'Superheroes Name : ',name)
print()
