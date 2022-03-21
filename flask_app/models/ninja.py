from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__(self, data):
        self.dojo.id = data["dojo_id"]
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.age = data["age"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]



# c
    @classmethod 
    def create(cls,data):
        mysql = connectToMySQL("dojos_and_ninjas_schema")
        query = "INSERT INTO ninjas (dojo_id, first_name, last_name, age) Values (%(dojo_id)s,%(first_name)s, %(last_name)s, %(age)s);"
        ninja_id = mysql.query_db(query, data)

        return ninja_id
   

# read
# this is displaying the Ninjas(cities on the assignment yes? same as r in dojos?)


# u


# d