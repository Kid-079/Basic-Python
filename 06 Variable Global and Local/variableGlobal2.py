# Variable Global

string1 = 'Teruslah Melangkah Karena Pasti Ada 1 Dari Sejuta Manusia Yang Mengingatnya'
string2 = 'Cause Zero Still Have Values'

def stringText1(text):
	global string1
	string1 = newString1
	print('TEXT --> ',string1)

def stringText2(text,writer):
	global string1,string2
	string1 = text
	string2 = writer

#1
# stringText1('A')
stringText2('A','B')

#2
print(string1)
print(string1,string2)