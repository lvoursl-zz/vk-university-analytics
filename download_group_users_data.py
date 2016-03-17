from urllib.request import urlopen
from time import sleep 
import json

# загрузка юзеров с группы ВК

token = '4f318b471cda5c6bd6337cfc2644b478038ee7bb09a6158395101a036b834fc315c19b3fec6b9e28ea370'
offset = 0

while offset != 31068:
	try:	
		request = urlopen('https://api.vk.com/method/groups.getMembers?group_id=469&fields=schools&count=1&offset=' + str(offset)  + '&access_token=' + token)
		data = eval(request.read())
		data = json.loads(json.dumps(data))

		data_file = open('data_spbgu_bigget_group.json', 'a+')
		print(data['response']['users'], file = data_file, end = "\n")
		data_file.close()

		offset += 1
		print(offset)
	except Exception as e:
		print(str(e))
		print(offset)
		if ('charmap' in str(e)): 
			offset += 1