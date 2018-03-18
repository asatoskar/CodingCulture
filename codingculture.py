import os

from flask import Flask, render_template, request
from flask_dropzone import Dropzone
from mitra.src.utils.neo4j_utils import *

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
        f.save(os.path.join(app.config['UPLOADED_PATH'], f.filename))
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
