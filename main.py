from flask import Flask, jsonify, request, abort
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
    if (
            not request.json
            or not request.json.get("name")

    ):
        abort(400)

    body = request.json
    try:
        user = User(**body).save()
        return jsonify(user)
    except:
        return "you have an error"


@app.route('/data', methods=['GET'])
def data_display():
    try:
        users = User.objects.all()
        return jsonify(users)
    except:
        abort(404)


@app.route('/data/<user_id>', methods=['GET'])
def info_of_user(user_id):
    try:
        person = User.objects(id=user_id).get()
        return jsonify(person)
    except:
        abort(404)



if __name__ == '__main__':
    app.run(debug=True)
