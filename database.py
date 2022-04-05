import psycopg2

MOCK = True


class Base:
    def __init__(self):
        if not MOCK:
            self.conn = psycopg2.connect(dbname='historical_reconstruction',
                                     user='postgres',
                                     password='144ntthbssioeay',
                                     host='localhost')
            self.cursor = self.conn.cursor()


class GetUser(Base):

    def get_all_user(self):
        """
        GET
        :return:
        """
        if MOCK:
            return ['FirstUser', 'SecondUser']
        self.cursor.execute("SELECT * FROM users")
        res = self.cursor.fetchall()
        return list(res)

    def get_user_by_id(self, id):
        """
        GET
        :param id:
        :return:
        """
        if MOCK:
            return [f'FirstUser{id}']
        self.cursor.execute(f"SELECT * FROM users where id = {id}")
        res = self.cursor.fetchall()
        return list(res)

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
        except Exception:
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
            sql = f"insert into users(name, password, surname, email, type_) values ({name}, {password}, '{surname}', '{email}','{type_}');"
            self.cursor.execute(sql)
            return True
        except Exception:
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
        for arg in args:
            if arg == 'name':
                name = args['name']
                sql = f"update users set name = '{name}' where id = {id}"
                self.cursor.execute(sql)
            elif arg == 'password':
                password = args['password']
                sql = f"update users set password = '{password}' where id = {id}"
                self.cursor.execute(sql)
            elif arg == 'surname':
                surname = args['surname']
                sql = f"update users set email = '{surname}' where id = {id}"
                self.cursor.execute(sql)
            elif arg == 'email':
                email = args['email']
                sql = f"update users set email = '{email}' where id = {id}"
                self.cursor.execute(sql)
            elif arg == 'type_' and (args['type_'] =='organizer' or args['type_'] == 'reenactor' or args['type_']=='default_user'):
                type_ = args['type_']
                sql = f"update users set type_ = '{type_}' where id = {id}"
                self.cursor.execute(sql)


class GetBudget(Base):
    def get_all_budget(self):
        """*
        GET
        :return:
        """
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
    def get_all_equipment(self):
        """
        GET
        :return:
        """
        sql = "select * from equipment"
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        return list(res)

    def get_equipment_by_id(self, id):
        """
        GET
        :param id:
        :return:
        """
        self.cursor.execute(f"SELECT * FROM equipment where id = {id}")
        res = self.cursor.fetchall()
        return list(res)

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
            sql = f"insert into equipment(name, access_type, is_available, type_equip) values " \
                  f"('{name}', '{access_type}', '{is_available}', '{type_equip}');"
            self.cursor.execute(sql)
            return True
        except Exception:
            return False

    def update_equipment(self, id, args: dict):
        """
        PUT - FIX BUG
        :param id:
        :param args:
        :return:
        """
        for arg in args:
            if arg == 'name':
                name = args['name']
                sql = f"update equipment set name = '{name}' where id = {id}"
                self.cursor.execute(sql)
            elif arg == 'access_type' and (args['access_type'] == 'organizer' or args['access_type'] == 'reenactor', args['default_user'] == 'default_user'):
                access_type = args['access_type']
                sql = f"update equipment set access_type = '{access_type}' where id = {id}"
                self.cursor.execute(sql)
            elif arg == 'is_available':
                is_available = args['is_available']
                sql = f"update equipment set is_available = '{is_available}' where id = {id}"
                self.cursor.execute(sql)
            elif arg == 'type_equip' and (args['type_equip'] == 'special' or args['type_equip'] == 'common'):
                type_equip = args['type_equip']
                sql = f"update equipment set type_equip = '{type_equip}' where id = {id}"
                self.cursor.execute(sql)

    def delete_equipment(self, id):
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


class GetReconstruction(Base):
    def get_all_reconstructions(self):
        """
        GET
        :return:
        """
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
        self.cursor.execute(f"SELECT * FROM equipment where id = {id}")
        res = self.cursor.fetchall()
        return list(res)

    def create_new_reconstruction (self, description, place, payment, id_org, time):
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
        try:
            self.cursor.execute(f"delete from reconstruction where id = {id}")
            return True
        except Exception:
            return False



def main():
        my_user = GetUser()
        dict_change = {'email': 'asdasdasd@gmail.com', 'name': 'ash'}
        #my_user.update_new_user(2, dict_change)
        res = my_user.get_user_by_id(2)
        print(res)

if __name__ == '__main__':
    main()

