import facebook
import requests

def get_fb_token():
	client_id = "408715946337328"
	client_secret = "7210163f251f9e28f5ea16319655f06a"
	graph = facebook.GraphAPI()
	access_token = graph.get_app_access_token(client_id, client_secret)
	print("---------------------- " + access_token)
	