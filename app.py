from flask import Flask, jsonify, request
from like_controller import singlton

app = Flask(__name__)


@app.route('/users', methods=['GET'])
def get_users():
    res = singlton.my_user.get_all_user()
    return jsonify(res)


@app.route('/user/<id>', methods=['GET'])
def get_user_by_id(id):
    if id.isdigit():
        id = int(id)
    else:
        raise ValueError('Bad argument id')
    res = singlton.my_user.get_user_by_id(id)
    return jsonify(res)


@app.route('/users/', methods=['POST'])
def post_users():
    name = request.values.get('name')
    password = request.values.get('password')
    surname = request.values.get('surname')
    email = request.values.get('email')
    type_ = request.values.get('type_')
    res = singlton.my_user.create_new_user(name=name,
                                           surname=surname,
                                           password=password,
                                           email=email,
                                           type_=type_)
    if res:
        return 'User was updated'
    else:
        raise ValueError('Bad request')


@app.route('/users/<id>', methods=['PUT'])
def put_users(id):
    my_dict = dict()
    my_dict['name'] = request.values.get('name')
    my_dict['password'] = request.values.get('password')
    my_dict['surname'] = request.values.get('surname')
    my_dict['email'] = request.values.get('email')
    my_dict['type_'] = request.values.get('type_')
    res = singlton.my_user.update_user(id=id, args=my_dict)
    if res:
        return 'User was updated'
    else:
        raise ValueError('Bad request')


@app.route('/user/<id>', methods=['DELETE'])
def delete_user(id):
    if id.isdigit():
        id = int(id)
    res = singlton.my_user.delete_user_by_id(id)
    if res:
        return 'User was successfully delete!'
    else:
        raise ValueError('Bad Request Error')


@app.route('/')
def get_equipment():
    return 'Hello World!'


@app.route('/')
def post_equipment():
    return 'Hello World!'


@app.route('/')
def put_equipment():
    return 'Hello World!'


@app.route('/')
def delete_equipment():
    return 'Hello World!'


@app.route('/')
def get_budget():
    return 'Hello World!'


@app.route('/')
def get_reconstruction():
    return ''


@app.route('/')
def post_reconstruction():
    return ''


@app.route('/')
def put_reconstruction():
    return ''


@app.route('/')
def delete_reconstruction():
    return ''


@app.route('/')
def reg_for_reconstruction():
    return ''


@app.route('/')
def post_statement():
    return ''


if __name__ == '__main__':
    app.run()
