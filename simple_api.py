from flask import Flask, json, jsonify


app = Flask(__name__)


@app.route('/<string:name>/<int:age>')
def home(name, age):
    return jsonify(
        {
            'name': name,
            'age': age,
            'msg': f'Hello {name}. You are {age}. :)'
        }
    )


if __name__ == '__main__':
    app.run(debug=True)