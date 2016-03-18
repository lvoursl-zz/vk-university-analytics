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

# считывание данных о пользователях с json файла с последующим составлением списка школ
i = 0

with open('data_spbgu_bigget_group.json', 'r', encoding = 'cp1251') as data_file:
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

				data = ast.literal_eval(line)
				
				if 'schools' in data:		
					
					str_school_data = str(data['schools'])
					
					if len(str_school_data) > 3 : 
						
						str_school_data = '' + str_school_data[1:]
						str_school_data = str_school_data[:len(str_school_data) - 1] + ''
						school_data = ast.literal_eval(str_school_data)					

						if type(school_data) is dict:												
							add_school(school_data['name'])
						elif type(school_data) is tuple:
							# если школы пользователей образовали кортеж, значит их несколько
							school_data_list = list(school_data)
							for school in school_data_list:								
								add_school(school['name'])
	except Exception as e:
		print(str(e))


school_stats_file = open('spbgu_big_dataset', 'w+')

for w in sorted(schools_dict, key = schools_dict.get, reverse = True):
	print(w, schools_dict[w], file = school_stats_file)