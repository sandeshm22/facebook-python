import sys
import facebook
import mongodb_db_api
import json
import requests 

#640079569360625?fields=id,name,album,backdated_time,from,icon,name_tags,place,likes,reactions,sharedposts
program_name = sys.argv[0]
arguments = sys.argv[1:]
count = len(arguments)
print(arguments)

def get_graph():
	graph = facebook.GraphAPI(access_token='EAAFzuZAjLpDABAMrYM0vJSRWUhNxckm6CIUqOx5Ho8YE7Dx2QZCNAaqKerkb99xefe8x4kHKMbzyhThOIk9dXoIx1HQ4RydvwVROa6dA8SdWpZAOWRhdywThMpzlS0QkkyPVWen9GfZBZBA0rBfb4yurkBZBUZBNU1wrWzKK4pFLUIDnsxqcThZAZBiXXwEC9bdEZD',version = 3.1)
	return graph

	
	
def get_user_photos(user, graph):
	photos = user['photos']
	data = photos['data']
	cursor = photos['paging']['next']
	#print(cursor)
	print("Inserting " + str(len(data)))
	mongodb_db_api.save_to_db_collection(data,'user')
	for i in range(1,5) :
		print(str(i))
		cursor_response = requests.get(cursor)
		cursor_data = cursor_response.json() 
		print("Inserting 111" + str(len(cursor_data['data'])))
		mongodb_db_api.save_to_db_collection(cursor_data['data'], 'user')
		cursor = cursor_data['paging']['next']

def main():
	mode_string = arguments[0]
	mode= mode_string.split("=")
	
	if mode[1]=='database' :
		print(mode[1])
		graph = get_graph()
		user = get_user_data()
		photos = get_user_photos(user, graph)
		mongodb_db_api.save_to_db_collection(user, 'user')
		mongodb_db_api.print_collection('user')

def get_user_data():
	graph = get_graph() 
	user = graph.request('/me?fields=id,name,photos')
	return user
   
main()