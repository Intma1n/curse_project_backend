import psycopg2

MOCK = False


class Base:
    def __init__(self):
        if not MOCK:
            self.conn = psycopg2.connect(dbname='',
                                         user='',
                                         password='',
                                         host='')
            self.cursor = self.conn.cursor()


class GetUser(Base):

    def format_user(self, user):
        return {
            'id': user[0],
            'name': user[1],
            'password': user[2],
            'surname': user[3],
            'email': user[4],
            'type_of_user': user[5]
        }

    def get_all_user(self):
        """
        GET
        :return:
        """
        if MOCK:
            return ['FirstUser', 'SecondUser']
        self.cursor.execute("SELECT * FROM users")
        list_users = list(self.cursor.fetchall())
        list_result = list()
        for user in list_users:
            dict_res = self.format_user(user)
            list_result.append(dict_res)
        return list_result

    def get_user_by_id(self, id):
        """
        GET
        :param id:
        :return:
        """
        if MOCK:
            return [f'FirstUser{id}']
        self.cursor.execute(f"SELECT * FROM users where id = {id}")
        res = list(self.cursor.fetchall())[0]
        return self.format_user(res)

    def delete_user_by_id(self, id):
        """
        DELETE
        :param id:
        :return:
        """
        try:
            if MOCK:
                return True
            self.cursor.execute(f"delete from users where id = {id}")
            return True
        except Exception as err:
            print(f'its exception into deleting = {err}')
            return False

    def create_new_user(self, name, password, surname, email, type_):
        """
        POST
        :param name:
        :param password:
        :param surname:
        :param email:
        :param type_:
        :return:
        """
        try:
            if MOCK:
                return True
            sql = f"insert into users(name, password, surname, email, type_) values ('{name}', '{password}', '{surname}', '{email}','{type_}');"
            self.cursor.execute(sql)
            self.conn.commit()
            return True
        except Exception as err:
            print(f'Error into create_new_user = {err}')
            return False

    def update_user(self, id, args: dict):
        """
        PUT - FIX BUG
        :param id:
        :param args:
        :return:
        """
        if MOCK:
            return True
        try:
            if args['name']:
                name = args['name']
                sql = f"update users set name = '{name}' where id = {id}"
                self.cursor.execute(sql)
                self.conn.commit()
            if args['password']:
                password = args['password']
                sql = f"update users set password = '{password}' where id = {id}"
                self.cursor.execute(sql)
                self.conn.commit()
            if args['surname']:
                surname = args['surname']
                sql = f"update users set email = '{surname}' where id = {id}"
                self.cursor.execute(sql)
                self.conn.commit()
            if args['email']:
                email = args['email']
                sql = f"update users set email = '{email}' where id = {id}"
                self.cursor.execute(sql)
                self.conn.commit()
            if args['type_'] and args['type_'] in ('organizer', 'reenactor''default_user'):
                type_ = args['type_']
                sql = f"update users set type_ = '{type_}' where id = {id}"
                self.cursor.execute(sql)
                self.conn.commit()
            return True
        except Exception as err:
            print(f'Error in put_user = {err}')
            return False


class GetBudget(Base):
    def get_all_budget(self):
        """*
        GET
        :return:
        """
        if MOCK:
            return [{'SOMETHING': 'like budget'}]
        sql = "select * from budget_log"
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        return list(res)

    def get_budget_by_id(self, id):
        """
        GET
        :param id:
        :return:
        """
        self.cursor.execute(f"SELECT * FROM budget_log where id = {id}")
        res = self.cursor.fetchall()
        return list(res)

    def create_new_budget(self, amount, type_budget):
        """
        POST
        :param name:
        :param password:
        :param surname:
        :param email:
        :param type_:
        :return:
        """
        try:
            sql = f"insert into budget_log(amount, type_budget) values ('{amount}','{type_budget}');"
            self.cursor.execute(sql)
            return True
        except Exception:
            return False

    def update_budget(self, id, args: dict):
        """
        PUT - FIX BUG
        :param id:
        :param args:
        :return:
        """
        for arg in args:
            if arg == 'amount':
                amount = args['amount']
                sql = f"update budget_log set amount = '{amount}' where id = {id}"
                self.cursor.execute(sql)
            elif arg == 'type_budget' and (args['type_budget'] == 'received' or args['type_budget'] == 'spent'):
                type_budget = args['type_budget']
                sql = f"update budget_log set type_budget = '{type_budget}' where id = {id}"
                self.cursor.execute(sql)

    def delete_budget_by_id(self, id):
        """
        DELETE
        :param id:
        :return:
        """
        try:
            self.cursor.execute(f"delete from budget_log where id = {id}")
            return True
        except Exception:
            return False


class GetEquipment(Base):

    def format_equipment(self, equipment):
        return {
            'id': equipment[0],
            'name': equipment[1],
            'is_available': equipment[2],
            'type_equip': equipment[3]
        }

    def get_all_equipment(self):
        """
        GET
        :return:
        """
        if MOCK:
            return [{'id': 1,
                     'name': 'test_name',
                     'access_type': 'asd',
                     'type_equip': 'some_type'},
                    {'id': 2,
                     'name:' 'test_second_name,'
                     'access_type': 'asdasd',
                     'type': 'other_type'}]
        sql = "select * from equipment"
        self.cursor.execute(sql)
        list_equipment = list(self.cursor.fetchall())
        res_list = list()
        for equipment in list_equipment:
            res_list.append(self.format_equipment(equipment))
        return list(res_list)

    def get_equipment_by_id(self, id):
        """
        GET
        :param id:
        :return:
        """
        if MOCK:
            return [{'id': id,
                     'name': 'test_name',
                     'access_type': 'asd',
                     'type_equip': 'some_type'}]
        self.cursor.execute(f"SELECT * FROM equipment where id = {id}")
        res = list(self.cursor.fetchall())[0]
        return self.format_equipment(res)

    def create_new_equipment(self, name, access_type, is_available, type_equip):
        """
        POST
        :param name:
        :param password:
        :param surname:
        :param email:
        :param type_:
        :return:
        """
        try:
            if MOCK:
                return True
            sql = f"insert into equipment(name, access_type, is_available, type_equip) values " \
                  f"('{name}', '{access_type}', '{is_available}', '{type_equip}');"
            self.cursor.execute(sql)
            self.conn.commit()
            return True
        except Exception as err:
            print(f'error in creating equipment = {err}')
            return False

    def update_equipment(self, id, args: dict):
        """
        PUT - FIX BUG
        :param id:
        :param args:
        :return:
        """
        if MOCK:
            return True
        try:
            if args['name']:
                name = args['name']
                sql = f"update equipment set name = '{name}' where id = {id}"
                self.cursor.execute(sql)
                self.conn.commit()
            if args['access_type'] and args['access_type'] in ('organizer', 'reenactor', 'default_user'):
                access_type = args['access_type']
                sql = f"update equipment set access_type = '{access_type}' where id = {id}"
                self.cursor.execute(sql)
                self.conn.commit()
            if args['is_available']:
                is_available = args['is_available']
                sql = f"update equipment set is_available = '{is_available}' where id = {id}"
                self.cursor.execute(sql)
                self.conn.commit()
            if args['type_equip'] and args['type_equip'] in ('special', 'common'):
                type_equip = args['type_equip']
                sql = f"update equipment set type_equip = '{type_equip}' where id = {id}"
                self.cursor.execute(sql)
                self.conn.commit()
            return True
        except Exception as err:
            print(f'its put equipment error = {err}')
            return False

    def delete_equipment(self, id):
        """
        DELETE
        :param id:
        :return:
        """
        try:
            if MOCK:
                return True
            self.cursor.execute(f"delete from budget_log where id = {id}")
            return True
        except Exception:
            return False


class GetReconstruction(Base):
    def get_all_reconstructions(self):
        """
        GET
        :return:
        """
        if MOCK:
            return [{'id': 1,
                     'description': 'its my desc',
                     'place': 'test_place',
                     'payment': 'some method of this',
                     'id_org': 1,
                     'time': 'time1'},
                    {'id': 2,
                     'description': 'its not my desc',
                     'place': 'test_new_place',
                     'payment': 'some asdasdmethod of this',
                     'id_org': 2,
                     'time': 'time2'}
                    ]
        sql = "select * from reconstruction"
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        return list(res)

    def get_reconstruction_by_id(self, id):
        """
        GET
        :param id:
        :return:
        """
        if MOCK:
            return [{'id': id,
                     'description': 'its my desc',
                     'place': 'test_place',
                     'payment': 'some method of this',
                     'id_org': 1,
                     'time': 'time1'}]
        self.cursor.execute(f"SELECT * FROM equipment where id = {id}")
        res = self.cursor.fetchall()
        return list(res)

    def create_new_reconstruction(self, description, place, payment, id_org, time):
        """
        POST
        :param name:
        :param password:
        :param surname:
        :param email:
        :param type_:
        :return:
        """
        try:
            if MOCK:
                return True
            sql = f"insert into equipment(description, place, payment, id_org, time) values " \
                  f"('{description}', '{place}', '{payment}',id_org, '{time}');"
            self.cursor.execute(sql)
            return True
        except Exception:
            return False

    def update_reconstruction(self, id, args: dict):
        """
        PUT - FIX BUG
        :param id:
        :param args:
        :return:
        """
        for arg in args:
            if arg == 'description':
                description = args['description']
                sql = f"update reconstruction set description = '{description}' where id = {id}"
                self.cursor.execute(sql)
            elif arg == 'place':
                place = args['place']
                sql = f"update reconstruction set place = '{place}' where id = {id}"
                self.cursor.execute(sql)
            elif arg == 'id_org':
                id_org = args['id_org']
                sql = f"update reconstruction set id_org = '{id_org}' where id = {id}"
                self.cursor.execute(sql)
            elif arg == 'time':
                time = args['time']
                sql = f"update reconstruction set time = '{time}' where id = {id}"
                self.cursor.execute(sql)

    def delete_reconstruction(self, id):
        """
        DELETE
        :param id:
        :return:
        """
        if MOCK:
            return True
        try:
            self.cursor.execute(f"delete from reconstruction where id = {id}")
            return True
        except Exception:
            return False


class RegistrationForReconstruction(Base):
    def reg(self, id_user, id_rec, time):
        try:
            sql = f"insert into register_for_rec(id_user, id_rec, time) values " \
                  f"({id_user}, {id_rec}, '{time}');"
            self.cursor.execute(sql)
            return True
        except Exception:
            return False


class GetStatement(Base):
    def create_statement(self, id_req, id_equip, id_org, text_):
        """
        POST
        :param name:
        :param password:
        :param surname:
        :param email:
        :param type_:
        :return:
        """
        try:
            sql = f"insert into statement(id_req, id_equip, id_org, id_org, time) values " \
                  f"(id_req, id_equip, id_org,id_org, '{text_}');"
            self.cursor.execute(sql)
            return True
        except Exception:
            return False


def main():
    my_user = GetUser()
    dict_change = {'email': 'asdasdasd@gmail.com', 'name': 'ash'}
    # my_user.update_new_user(2, dict_change)
    res = my_user.get_user_by_id(2)
    print(res)


if __name__ == '__main__':
    main()
