import os

from flask import Flask, redirect, render_template, request, session, url_for
#from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
from flask_dropzone import Dropzone
from mitra.src.utils.neo4j_utils import get_graph_connection, create_image_node, create_image_tag_relationship, create_tag_node
from mitra.src.utils.image_utils import get_image_hash, get_domcolors
from classify_image import predict

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
conn = get_graph_connection(host="localhost", port="7474", user_name="neo4j", password="password")

app.config.update(
	UPLOADED_PATH=os.path.join(basedir, 'uploads'),
	DROPZONE_ALLOWED_FILE_TYPE='image',
	DROPZONE_MAX_FILE_SIZE=3,
	DROPZONE_MAX_FILES=30,
)



drop_zone = Dropzone(app)

app.config['DROPZONE_UPLOAD_MULTIPLE'] = False
app.config['DROPZONE_ALLOWED_FILE_CUSTOM'] = True
app.config['DROPZONE_ALLOWED_FILE_TYPE'] = 'image/*'


#app.config['UPLOADED_PHOTOS_DEST'] = os.getcwd() + '/uploads'

#photos = UploadSet('photos', IMAGES)
#configure_uploads(app, photos)
#patch_request_class(app)


@app.route('/', methods=['POST', 'GET'])
def upload():
	if request.method == 'POST':
		f = request.files.get('file')
		f.save(os.path.join(app.config['UPLOADED_PATH'], f.filename))
		file_path="uploads/"+f.filename
		image_hash = get_image_hash(file_path)
		imgcols = get_domcolors(file_path)
		tags = predict(file_path)
		print(type(tags))
		first_tag = list(tags.keys())[0]
		image_node = create_image_node(name=str(f.filename), image_hash=str(image_hash), dom_colours=str(imgcols))
		tag_node = create_tag_node(tag_name=first_tag)  # Result of the prediction in tag name
		image_tag_relationship = create_image_tag_relationship(image_node, tag_node)
		conn.create(image_tag_relationship)
	return render_template('index.html')


if __name__ == '__main__':
	app.run(debug=True)