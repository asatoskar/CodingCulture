from py2neo import Graph, authenticate, Node, Relationship


def get_graph_connection(host="localhost", port="7474", user_name="neo4j", password="neo"):
	try:
		authenticate(host + ":" + port, user_name, password)
		return Graph("http://" + host + ":" + port + "/db/data/")
	except BaseException as e:
		print(e)
		print("Couldn't connect to neo4j database.")


def create_tag_node(tag_name):
	return Node("TAG", name=tag_name)


def create_image_node(name, image_hash):
	return Node("IMAGE", name=name, hash=image_hash)


def create_image_tag_relationship(image_node, tag_node):
	return Relationship(image_node, "IS", tag_node)


def __main__():
	conn = get_graph_connection()
	img_node = create_image_node("dummy1", "hash1")
	tag_node = create_tag_node("dummy")
	rel = create_image_tag_relationship(img_node, tag_node)
	conn.create(rel)
	print(conn, img_node, tag_node, rel)


if __name__ == "__main__":
	__main__()
