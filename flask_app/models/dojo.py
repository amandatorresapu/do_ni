from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja

class Dojo:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]



# c
    @classmethod 
    def create(cls,data):
        mysql = connectToMySQL("dojos_and_ninjas_schema")
        query = "INSERT INTO dojos (name) Values (%(name)s);"
        return mysql.query_db(query, data)

# r
# this is displaying the names(cities on the assignment yes?)
    @classmethod
    def get_all(cls):
        mysql = connectToMySQL("dojos_and_ninjas_schema")
        results = mysql.query_db("SELECT * FROM dojos;")
        all_dojos = []
        if results:
            for row in results:
                    all_dojos.append(cls(row))
            return all_dojos
        

# get one with ninjas belong to that dojo
# u
    @classmethod
    def get_all_ninjas(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
        results = connectToMySQL("dojos_and_ninjas_schema").query_db(query, data)
        if results:
            dojo = cls(results[0])
            if results[0]["ninjas.id"]:
                dojo.ninjas = []
                for row in results:
                    data = {
                        "id": row ["ninjas.id"],
                        "First Name": row["first_name"],
                        "Last Name": row["last_name"],
                        "Age": row["age"],
                        "dojo_id": row["dojo_id"],
                        "created_at": row["ninjas.created_at"],
                        "updated_at": row["ninjas.updated_at"]
                    }
                    temp_ninja = ninja.Ninja(data)
                    dojo.ninjas.append(temp_ninja)
            return dojo

# d