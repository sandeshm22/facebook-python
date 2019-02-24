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
	graph = facebook.GraphAPI(access_token='EAAFzuZAjLpDABAPaf2H2dTmeI7nn8j0AXUTvvs6lWQ9TfZAhhNrUiPyOod3PaJMdkqHbNgL8gS4WTPerOhu04Y4p6XEGXBE9QIrceZC1TqBfS407aaKN5IJdVa4ZB8kdygTFsLy1Ia7bgbWEWlIisxZCcL2XnkIo20H7ZBN1lSo1Wr0ylbSx3vFXxuu9B2V9AZD',version = 3.1)
	return graph


def load_photos():
	all_photos = mongodb_db_api.get_all_documents('user')
	graph = get_graph()
	i=0
	for item  in all_photos :
		photo_id = item['id']
		url = photo_id + '?fields=id,name,album,backdated_time,from,icon,name_tags,place,likes,reactions,sharedposts'
		#print(url)
		photo_data = graph.request(url)
		photo_data['_id'] = photo_data['id']
		#print(photo_data)
		mongodb_db_api.save_to_db_collection_by_name(photo_data, 'photo_data')
			
	
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
	
	if mode[1]=='fetch' :
		print(mode[1])
		graph = get_graph()
		user = get_user_data()
		photos = get_user_photos(user, graph)
		mongodb_db_api.save_to_db_collection(user, 'user')
		mongodb_db_api.print_collection('user')
	else :
		print(mode[1])
		load_photos()
	
def get_user_data():
	graph = get_graph() 
	user = graph.request('/me?fields=id,name,photos')
	return user
   
main()