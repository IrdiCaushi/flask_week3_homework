from flask_restful import Resource
from flask import jsonify

students_list = [
    {"id": 1, "name": "Irdi Caushaj"},
    {"id": 2, "name": "Orges Mihaj"},
    {"id": 3, "name": "Besar Limani"}
]

class Student_one(Resource):
    
    
    # The POST method implementation  ---Crud (Create of CRUD)               
    def post(self,student_id,name):
        for i in range(len(students_list)):
            if students_list[i-1]['id'] == student_id:
                id_exist = True
        
        if id_exist == False:
            students_list.append(dict({'id': student_id, 'name': name}))
            return jsonify(students_list)
        else:
            return "ID already exist"

    # The PUT method implementation ---crUd (Update of CRUD)
    def put(self,student_id,name):
        for a in students_list:
            if a["id"] == student_id:
                a.update({'name': name})
                return jsonify(a)

        students_list.append(dict({'id': student_id, 'name': name}))
        return jsonify(students_list)


class Student_two(Resource):

    #The GET method implementation  ---cRud (Retrieve of CRUD)
    def get(self, student_id):
        flag = False
        for student in students_list:
            if student["id"] == student_id:
                flag = True
                return jsonify(student)
        if flag == False:    
            return "ID not Found!"


    # The DELETE method implementation ---cruD (Delete of CRUD)
    def delete(self, student_id):
        flag = False
        for i in range(len(students_list)): 
            if students_list[i]['id'] == student_id: 
                del students_list[i]
                flag = True 
                return "Student deleted!"

        if flag == False:
            return "ID not Found!"


class All_students(Resource):
    def get(self):
        return jsonify(students_list)