from id_from_username import IdFromUsername 

from friends import Friends 
 
str = input("Введите ник:")

if str != "":
	uclient = IdFromUsername(str) 
	uid = uclient.execute() 
 
	friends_client = Friends(uid) 
	friends = friends_client.execute() 
 
 
	for (age, count) in friends: 
		print('{} {}'.format(int(age), '#' * count)) 