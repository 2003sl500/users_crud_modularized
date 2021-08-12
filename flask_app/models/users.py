from flask_app.config.mysqlconnection import connectToMySQL

DATABASE = 'usersdb2'
class Users:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        # make sure to call the connectToMySQL function with the schema you are targeting
        results = connectToMySQL(DATABASE).query_db(query)
        # create an empty list to append our instances of users
        users = []
        # iterate over the db results and create instances of users with cls
        for user in results:
            users.append( cls(user) )
        return users

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users ( first_name , last_name , email , created_at , updated_at ) VALUES ( %(fname)s , %(lname)s , %(email)s , NOW(), NOW() );"
        #  data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL(DATABASE).query_db(query, data)

    user_result = ""
    @classmethod
    def single_user(cls, id):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        data = {'id':id}
        # make sure to call the connectToMySQL function with the schema you are targeting
        results = connectToMySQL(DATABASE).query_db(query, data)
        # create an empty list to append our instances of users
        users = []
        # iterate over the db results and create instances of users with cls
        for user in results:
            users.append( cls(user) )

        print("Results, single user: ", results)
        return users

    @classmethod
    def edit(cls, data, id):
        print("entered edit()")
        query = "UPDATE users SET first_name = %(fname)s, last_name = %(lname)s, email = %(email)s, updated_at = NOW() WHERE id = %(id)s;"
        id = {
            'id': id
        }
        print("query: ", query)
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def delete(cls, data, id):
        print("entered delete method in users.py, id: ", id)
        query = "DELETE FROM users WHERE id = %(id)s;"
        id = {
            'id': id
        }
        print("query: ", query)
        return connectToMySQL(DATABASE).query_db(query, data)
    