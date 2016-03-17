from urllib.request import urlopen
from time import sleep 
import json
import ast

schools_dict = {}

def add_school(school):
	global schools_dict
	if school in schools_dict:
		schools_dict[school] += 1
	else:
		schools_dict[school] = 1


# загрузка юзеров с группы ВК

'''token = '4f318b471cda5c6bd6337cfc2644b478038ee7bb09a6158395101a036b834fc315c19b3fec6b9e28ea370'
offset = 4015

while offset != 11828:
	try:	
		request = urlopen('https://api.vk.com/method/groups.getMembers?group_id=41638345&fields=schools&count=1&offset=' + str(offset)  + '&access_token=' + token)
		data = eval(request.read())
		data = json.loads(json.dumps(data))

		data_file = open('data.json', 'a+')
		print(data['response']['users'], file = data_file, end = "\n")
		data_file.close()

		offset += 1
		print(offset)
	except Exception as e:
		print(str(e))
		print(offset)
		if ('charmap' in str(e)): 
			offset += 1'''


# считывание данных о пользователях с json файла с последующим составлением списка школ
i = 0

with open('data.json', 'r', encoding = 'cp1251') as data_file:
	try:
		'''data = eval(data_file.read())
		data = json.loads(json.dumps(data))
		print(data[0]['first_name'])'''
		for line in data_file:
			if len(line) > 3 :
				print(i)
				i += 1
				line = '' + line[1:]
				line = line[:len(line) - 2] + ''

				#data = json.loads(json.dumps(line), strict=False)
				#print(type(data))
				data = ast.literal_eval(line)
				
				if 'schools' in data:
					#print(data['schools'])
					str_school_data = str(data['schools'])
					if len(str_school_data) > 3 : 
						#print(str_school_data)
						str_school_data = '' + str_school_data[1:]
						str_school_data = str_school_data[:len(str_school_data) - 1] + ''
						school_data = ast.literal_eval(str_school_data)
						#print(str(type(school_data)))

						if type(school_data) is dict:					
							#print(school_data['name'])
							add_school(school_data['name'])
						elif type(school_data) is tuple:
							# если школы пользователей образовали кортеж, значит их несколько
							school_data_list = list(school_data)
							for school in school_data_list:
								#print(school['name'])
								add_school(school['name'])
	except Exception as e:
		print(str(e))


school_stats_file = open('spbseu', 'w+')

for w in sorted(schools_dict, key = schools_dict.get, reverse = True):
	print(w, schools_dict[w], file = school_stats_file)