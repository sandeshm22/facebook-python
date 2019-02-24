import cassandra
from cassandra.cluster import Cluster

def init():
	cluster = Cluster()
	cluster.protocol_version=5
	cluster.allow_beta_protocol_version=True
	session = cluster.connect()
	session.execute("use facebook_keyspace")
	return session
	
def insertUser(user):
	session = init()
	
	#insert_user = 
	session.execute("INSERT INTO user_data (userid, fbuser_id, name) VALUES (1,'" +  str(user['id']) + "','"+ user['name']+"')")
	#insert_user = session.prepare("INSERT INTO user_data (fbuser_id, name) VALUES (%s, %s)",(user['id'], user['name']))
	#batch = SimpleStatement(consistency_level=ConsistencyLevel.QUORUM)
    #batch.add(insert_user, user['id'], user['name'])
	
	#session.execute(insert_user, (user['id'], user['name']))
	#session.execute(insert_user)
	