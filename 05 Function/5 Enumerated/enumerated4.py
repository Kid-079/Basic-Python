# Combine 2 list in one loop

superheroes = [ 'Kamen Rider',
				'Ultaramang',
				'Supermen',
				'Mak Lemper',
				'Wiro Sableng'    
			  ]

superheroes_name = [ 'A',
		             'B',
		             'C',
		             'D'
			       ]      

# 1. Enumerate --> Enumerate will automatically return indeks and value
for i,heroes in enumerate(superheroes):
	print(i,":",heroes)
print()

# 2. Zip --> Combine List
for heroes, name in zip(superheroes,superheroes_name):
	print(heroes,'Superheroes Name : ',name)
print()

# 3. Set
playlist1 = {'Kamen Rider','Ultaramang','Supermen','Mak Lemper','Wiro Sableng'}
playlist2 = {'Kamen Rider, Ultaramang, Supermen, Mak Lemper, Wiro Sableng'}
print(playlist1)
print(playlist2)
print("\n")

# Set Playlist Not Sorted ---> Shuffle
print('-- Shuffle --')
for name in playlist1:
	print(name)
print()

# Set Playlist Sorted     ---> Not Shuffle
print('-- Not Shuffle --')
for name in sorted(playlist1):
	print(name)
print()

# 4. Dictionaries -- Loop
playlist3 = {'Paparoti' : '1',
			 'Mak Lemper' : '2'
			}
for i in playlist3.keys():           # Playlist Name 
	print(i)
print("="*20) 

for i in playlist3.values():         # Playlist Number 
	print(i)
print("="*20) 

for i in playlist3.items():          # Show Both 
	print(i)
print("="*20) 

for i,j in playlist3.items():        # Show Both 
	print(i,'Playlist Number',j)
print("="*20) 

for i in reversed(range(1,5,1)):     # Reversed 
	print(i)
print("="*20) 