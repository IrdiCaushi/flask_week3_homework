from flask import Flask, request, jsonify

app = Flask(__name__, static_url_path='/static')



students_list = [
    {"id": 1, "name": "Irdi Caushaj"},
    {"id": 2, "name": "Orges Mihaj"},
    {"id": 3, "name": "Besar Limani"}
]

#----------------------------- Method Section --------------------------------------

# The GET method implementation  ---cRud (Retrieve of CRUD)
def get_student(student_id):
    flag = False
    for student in students_list:
        if student["id"] == student_id:
            flag = True
            return jsonify(student)
    if flag == False:    
        return "ID not Found!"

# The DELETE method implementation ---cruD (Delete of CRUD)
def delete_student(student_id):
    flag = False
    for i in range(len(students_list)): 
        if students_list[i]['id'] == student_id: 
            del students_list[i]
            flag = True 
            return "Student deleted!"

    if flag == False:
        return "ID not Found!"

# The PUT method implementation ---crUd (Update of CRUD)
def put_student(student_id, name):
    id_exist = False

    for a in students_list:
        if a["id"] == student_id:
            a.update({'name': name})
            id_exist = True
            return jsonify(a)

    if id_exist == False:
        students_list.append(dict({'id': student_id, 'name': name}))
        return jsonify(students_list)

    return jsonify(students_list)

# The POST method implementation  ---Crud (Create of CRUD)           
def post_student(student_id, name):
    id_exist = False
    for i in range(len(students_list)):
        if students_list[i-1]['id'] == student_id:
            id_exist = True
    
    if id_exist == False:
        students_list.append(dict({'id': student_id, 'name': name}))
        return jsonify(students_list)
    else:
        return "ID already exist"
    
# The GET all-events method implementation
def get_students():
    return jsonify(students_list)


#------------------- Route mapping to the methods declared above -----------------------------

@app.route('/')
def main():
    return "Hi from Irdi Caushaj"



@app.route('/v1/student/<int:student_id>', methods=["GET","DELETE"])
def student_crud_gd(student_id):
    if request.method == "GET":
        return get_student(student_id)
    else:
        return delete_student(student_id)
   


@app.route('/v1/student/<int:student_id>/<name>', methods=["POST","PUT"])
def student_crud_pp(student_id, name):
    if request.method == "POST":
        return post_student(student_id, name)
    else:
        return put_student(student_id, name)



@app.route('/v1/students', methods=["GET"])
def student_r():
    return get_students()

