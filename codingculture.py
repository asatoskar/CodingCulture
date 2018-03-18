import os

from flask import Flask, render_template, request
from flask_dropzone import Dropzone
from mitra.src.utils.neo4j_utils import get_graph_connection, create_image_node, create_image_tag_relationship, create_tag_node
from mitra.src.utils.image_utils import get_image_hash
# from classify_image import predict

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
conn = get_graph_connection(host="localhost", port="7474", user_name="neo4j", password="neo")

app.config.update(
	UPLOADED_PATH=os.path.join(basedir, 'uploads'),
	DROPZONE_ALLOWED_FILE_TYPE='image',
	DROPZONE_MAX_FILE_SIZE=3,
	DROPZONE_MAX_FILES=30,
)

drop_zone = Dropzone(app)


@app.route('/', methods=['POST', 'GET'])
def upload():
	if request.method == 'POST':
		f = request.files.get('file')
		file_path = os.path.join(app.config['UPLOADED_PATH'], f.filename)
		f.save(file_path)
		image_hash = get_image_hash(file_path)
		# call predict here
		image_node = create_image_node(name=str(f.filename), image_hash=str(image_hash))
		tag_node = create_tag_node(tag_name="")  # Result of the prediction in tag name
		image_tag_relationship = create_image_tag_relationship(image_node, tag_node)
		conn.create(image_tag_relationship)
	return render_template('index.html')


if __name__ == '__main__':
	app.run(debug=True)
