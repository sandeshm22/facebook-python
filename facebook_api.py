import facebook
import os
import requests
#import python_api
import cassandra_cluster

def fetchfriends(myID, graphAPI):
   myFriendsURL = "/" + myID + "/"
   graph.request()


def getMyPageDetails(myID, graphAPI):
   myPages = "/" + myID + "/pages"


def downloadfile(imageSRC, photoID):
   image_url = imageSRC

   # URL of the image to be downloaded is defined as image_url
   r = requests.get(image_url)  # create HTTP response object

   # send a HTTP request to the server and save
   # the HTTP response in a response object called r
   with open(photoID + ".png", 'wb') as f:
      # Saving received content as a png file in
      # binary format

      # write the contents of the response (r.content)
      # to a new file in binary mode.
      f.write(r.content)

def main():
   graph = facebook.GraphAPI(access_token='EAAFzuZAjLpDABAHCYgkZAE0VUIsXvbCMRkHdG7w1fzUN0zD1Ude6DDPei4MgGDsz5YKZAi4pCptoQKvpX0wLx7rkRS2w5tE7hUHwk7S5UxUpgkMXlNKJp79GUHN84h0XW1qZB0DMLqOL0OK8ovZBZAjxsKt1kizanIQoxajCKxNvA8e4A5cDHfuhb8KM8dWSsZD',version = 3.1)
   user = graph.request('/me?fields=id,name')
   userID = user['id']
   cassandra_cluster.insertUser(user) 
   userPhotosURL = "/"+userID+"/photos/"
   userPhotos = graph.request(userPhotosURL)
   #print(friendsList)
   #likesData = graph.request("/+" + userID+"/likes")
   #print(likesData['data'])

   #likes = likesData['data']
   #for like in likes:
      #print(like['id'])
      #likeURL = "/" + like['id']
      #likeData = graph.request(likeURL)
      #print(likeData)


   for photo in userPhotos['data']:
      photoURL = "/" + photo['id'] + "?fields=images"
      photoData = graph.request(photoURL)
      image = photoData['images']
      downloadfile(image[0]['source'], photo['id'])

main()
