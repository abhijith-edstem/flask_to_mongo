from flask import Flask, jsonify, request
from flask_mongoengine import MongoEngine
from models import User

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    "db": "myapp",
    'username':'rootuser',
    'password':'rootpass'
}
db = MongoEngine(app)

@app.route('/data', methods=['POST'])
def data():
    body = request.json
    try:
        user = User(**body).save()
        return jsonify(user)
    except:
        return "you have an error"


if __name__ == '__main__':
    app.run(debug=True)
