from flask import Flask, jsonify, request
from like_controller import singlton
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)


@app.route('/register_for_reconstruction', methods=["GET"])
def get_register_for_rec():
    res = singlton.my_register_for_rec.get()
    response = jsonify(res)
    response.headers.add("Access-Control-Allow-Origin", "*")

    if res:
        return response
    else:
        raise ValueError('Bad data')


@app.route('/users', methods=['GET'])
def get_users():
    res = singlton.my_user.get_all_user()
    response = jsonify(res)
    return response


@app.route('/user/<id>', methods=['GET'])
def get_user_by_id(id):
    if id.isdigit():
        id = int(id)
    else:
        raise ValueError('Bad argument id')
    res = singlton.my_user.get_user_by_id(id)
    response = jsonify(res)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


@app.route('/users', methods=['POST'])
@cross_origin()
def post_users():
    print(request.json)
    name = request.json.get('name')
    password = request.json.get('password')
    surname = request.json.get('surname')
    email = request.json.get('email')
    type_ = request.json.get('type_')
    res = singlton.my_user.create_new_user(name=name,
                                           surname=surname,
                                           password=password,
                                           email=email,
                                           type_=type_)
    if res:
        return jsonify(type_, email)
    else:
        # raise ValueError('Bad request')
        return request


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
    response = jsonify(res)
    return response


@app.route('/equipment/<eq_id>', methods=['GET'])
@cross_origin()
def get_equipment_by_id(eq_id):
    if eq_id.isdigit():
        eq_id = int(eq_id)
    else:
        raise ValueError('Bad argument id')
    res = singlton.my_equipment.get_equipment_by_id(id)

    return res


@app.route('/equipment', methods=["POST"])
@cross_origin()
def post_equipment():
    name = request.json.get('name')
    access_type = request.json.get('access_type')
    is_available = request.json.get('is_available')
    type_equip = request.json.get('type_equip')
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
    response = jsonify(res)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


@app.route('/reconstruction/<id>', methods=['GET'])
def get_reconstruction_by_id(id):
    if id.isdigit():
        id = int(id)
    else:
        raise ValueError('Bad argument id')
    res = singlton.my_reconstruction.get_reconstruction_by_id(id)
    response = jsonify(res)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


@app.route('/reconstructions/', methods=['POST'])
@cross_origin()
def post_reconstructions():
    description = request.json.get('description')
    place = request.json.get('place')
    payment = request.json.get('payment')
    id_org = request.json.get('id_org')
    time = request.json.get('time')
    res = singlton.my_reconstruction.create_new_reconstruction(description=description,
                                                               place=place,
                                                               payment=payment,
                                                               id_org=id_org,
                                                               time=time)
    if res:
        return 'Reconstruction was updated'
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
@cross_origin()
def reg_for_reconstruction():
    id_user = request.json.get('id_user')
    id_rec = request.json.get('id_rec')
    time = request.json.get('time')
    res = singlton.my_register_for_rec.reg(id_user=id_user,
                                           id_rec=id_rec,
                                           time=time)
    if res:
        return 'Registration was successfully done'
    else:
        # raise ValueError('Bad request')
        return 'sdfsdf'


@app.route('/statement', methods=['POST'])
@cross_origin()
def post_statement():
    id_req = request.json.get('id_req')
    id_equip = request.json.get('id_equip')
    id_org = request.json.get('id_org')
    text_ = request.json.get('text_')
    res = singlton.my_statement.create_statement(id_req=id_req,
                                                 id_equip=id_equip,
                                                 id_org=id_org,
                                                 text_=text_)
    if res:
        return 'Registration for statement was done'
    else:
        # raise ValueError('Bad request')
        return 'sdfsd'


if __name__ == '__main__':
    app.run()
