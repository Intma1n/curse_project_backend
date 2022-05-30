from flask import Flask, jsonify, request
from like_controller import singlton

app = Flask(__name__)


@app.route('/register_for_reconstruction', methods=["GET"])
def get_register_for_rec():
    res = singlton.my_register_for_rec.get()
    if res:
        return jsonify(res)
    else:
        raise ValueError('Bad data')


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


@app.route('/users', methods=['POST'])
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
def delete_equipment(id):
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


@app.route('/reconstructions', methods=['GET'])
def get_reconstruction():
    res = singlton.my_reconstruction.get_all_reconstructions()
    return jsonify(res)


@app.route('/reconstruction/<id>', methods=['GET'])
def get_reconstruction_by_id(id):
    if id.isdigit():
        id = int(id)
    else:
        raise ValueError('Bad argument id')
    res = singlton.my_reconstruction.get_reconstruction_by_id(id)
    return jsonify(res)


@app.route('/reconstructions/', methods=['POST'])
def post_reconstructions():
    description = request.values.get('description')
    place = request.values.get('place')
    payment = request.values.get('payment')
    id_org = request.values.get('id_org')
    time = request.values.get('time')
    res = singlton.my_reconstruction.create_new_reconstruction(description=description,
                                                               place=place,
                                                               payment=payment,
                                                               id_org=id_org,
                                                               time=time)
    if res:
        return 'User was updated'
    else:
        raise ValueError('Bad request')


@app.route('/reconstruction/<id>', methods=["PUT"])
def put_reconstruction(id):
    my_dict = dict()
    my_dict['description'] = request.values.get('description')
    my_dict['place'] = request.values.get('place')
    my_dict['id_org'] = request.values.get('id_org')
    my_dict['time'] = request.values.get('time')
    res = singlton.my_equipment.update_equipment(id=id, args=my_dict)
    if res:
        return 'Equipment was updated'
    else:
        raise ValueError('Bad request')


@app.route('/reconstruction/<id>', methods=['DELETE'])
def delete_reconstruction(id):
    if id.isdigit():
        id = int(id)
    res = singlton.my_reconstruction.delete_reconstruction(id)
    if res:
        return 'Reconstruction was successfully delete!'
    else:
        raise ValueError('Bad Request Error')


@app.route('/register_for_reconstruction', methods=['POST'])
def reg_for_reconstruction():
    id_user = request.values.get('id_user')
    id_rec = request.values.get('id_rec')
    time = request.values.get('time')
    res = singlton.my_register_for_rec.reg(id_user=id_user,
                                           id_rec=id_rec,
                                           time=time)
    if res:
        return 'Registration was successfully done'
    else:
        raise ValueError('Bad request')


@app.route('/statement', methods=['POST'])
def post_statement():
    id_req = request.values.get('id_req')
    id_equip = request.values.get('id_equip')
    id_org = request.values.get('id_org')
    text_ = request.values.get('text_')
    res = singlton.my_statement.create_statement(id_req=id_req,
                                                 id_equip=id_equip,
                                                 id_org=id_org,
                                                 text_=text_)
    if res:
        return 'Registration for statement was done'
    else:
        raise ValueError('Bad request')


if __name__ == '__main__':
    app.run()
