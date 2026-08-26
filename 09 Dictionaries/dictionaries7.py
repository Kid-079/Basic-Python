# Dictionaries
# data = {key:value,key:value} <- Key -> Keyword

A = {
		"id": 123,
		#"name" : "Salaman"
		"name" : "Knight"
	}

B = {
		"id": 456,
		#"name": "Paparoti"
		"name": "Cowboy"
	}

C = {
		"id": 789,
		#"name": "Semir Khan"
		"name": "Beast"
	}

data = {
	"1" : A,
	"2" : B,
	"3" : C
}

print(data)
print("\n")

# Access Data
print("Access Data :")
print(data["2"])
print(B["name"])
