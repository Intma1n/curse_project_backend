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


@app.route('/equipment', methods=['GET'])
def get_equipment():
    res = singlton.my_equipment.get_all_equipment()
    return jsonify(res)


@app.route('/equipment/<id>', methods=['GET'])
def get_equipment_by_id(id):
    if id.isdigit():
        id = int(id)
    else:
        raise ValueError('Bad argument id')
    res = singlton.my_equipment.get_equipment_by_id(id)
    return jsonify(res)


@app.route('/equipment', methods=["POST"])
def post_equipment():
    name = request.values.get('name')
    access_type = request.values.get('access_type')
    is_available = request.values.get('is_available')
    type_equip = request.values.get('type_equip')
    res = singlton.my_equipment.create_new_equipment(name=name,
                                                     access_type=access_type,
                                                     is_available=is_available,
                                                     type_equip=type_equip)
    if res:
        return 'Equipment was created'
    else:
        raise ValueError('Bad request')


@app.route('/equipment/<id>', methods=["PUT"])
def put_equipment(id):
    my_dict = dict()
    my_dict['name'] = request.values.get('name')
    my_dict['access_type'] = request.values.get('access_type')
    my_dict['is_available'] = request.values.get('is_available')
    my_dict['type_equip'] = request.values.get('type_equip')
    res = singlton.my_equipment.update_equipment(id=id, args=my_dict)
    if res:
        return 'Equipment was updated'
    else:
        raise ValueError('Bad request')


@app.route('/equipment/<id>', methods=['DELETE'])
def delete_user(id):
    if id.isdigit():
        id = int(id)
    res = singlton.my_equipment.delete_equipment(id)
    if res:
        return 'Equipment was successfully delete!'
    else:
        raise ValueError('Bad Request Error')


@app.route('/budget', methods=["GET"])
def get_budget():
    res = singlton.my_budget.get_all_budget()
    return jsonify(res)


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
