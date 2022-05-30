import parser

from flask import Flask
from flask_restful import reqparse, abort, Api, Resource, request
from database import GetUser

app = Flask(__name__)
api = Api(app)

TODOS = {
    'todo1': {'task': 'build an API'},
    'todo2': {'task': '?????'},
    'todo3': {'task': 'profit!'},
}


def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in TODOS:
        abort(404, message="Todo {} doesn't exist".format(todo_id))


# Todo
# shows a single todo item and lets you delete a todo item


class Todo(Resource):
    def get(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        return TODOS[todo_id]

    def delete(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        del TODOS[todo_id]
        return '', 204

    def put(self, todo_id):
        args = parser.parse_args()
        task = {'task': args['task']}
        TODOS[todo_id] = task
        return task, 201


class Users(Resource):
    def get(self):
        my_user = GetUser()
        res = my_user.get_all_user()
        return res, 200


class User(Resource):
    def get(self, user_id):
        my_user = GetUser()
        res = my_user.get_user_by_id(user_id)
        return {'user': res}

    def delete(self, user_id):
        pass

    def put(self, user_id):
        pass

    def post(self, user_id):
        pass


# TodoList
# shows a list of all todos, and lets you POST to add new tasks
class TodoList(Resource):
    def get(self):
        return 'sss', 200

    def post(self):
        args = parser.parse_args()
        todo_id = int(max(TODOS.keys()).lstrip('todo')) + 1
        todo_id = 'todo%i' % todo_id
        TODOS[todo_id] = {'task': args['task']}
        return TODOS[todo_id], 201


##
## Actually setup the Api resource routing here
##
api.add_resource(TodoList, '/todos')
api.add_resource(Todo, '/todos/<todo_id>')
api.add_resource(Users, '/users')
api.add_resource(User, '/user/<user_id>')

if __name__ == '__main__':
    app.run(debug=True)
