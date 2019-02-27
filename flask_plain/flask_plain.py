from flask import Flask, request, jsonify

app = Flask(__name__, static_url_path='/static')


#-------------- Lists --------------------------------------------------------------

course_list = [
    {"id": 1, "name": "COS340a"},
    {"id": 2, "name": "COS310a"},
    {"id": 3, "name": "COS220b"}
]

event_list = [
    {"id": 1, "name": "Quiz 1"},
    {"id": 2, "name": "Mid-Term"},
    {"id": 3, "name": "Final"}
]

students_list = [
    {"id": 1, "name": "Irdi Caushaj"},
    {"id": 2, "name": "Orges Mihaj"},
    {"id": 3, "name": "Besar Limani"}
]

#-----------------------------------------------------------------------------------

#----------------------------- Method Section --------------------------------------

# The GET method implementation  ---cRud (Retrieve of CRUD)
def get(id_kind, list_kind):
    flag = False
    for value in list_kind:
        if value["id"] == id_kind:
            flag = True
            return jsonify(value)
    if flag == False:    
        return "ID not Found!"


# The DELETE method implementation ---cruD (Delete of CRUD)
def delete(id_kind, list_kind):
    flag = False
    for i in range(len(list_kind)): 
        if list_kind[i]['id'] == id_kind: 
            del list_kind[i]
            flag = True 
            return "Deleted!"

    if flag == False:
        return "ID not Found!"


# The PUT method implementation ---crUd (Update of CRUD)
def put(id_kind, list_kind, label):
    for a in list_kind:
        if a["id"] == id_kind:
            a.update({'name': label})
            return jsonify(a)
        else:
            id_exist = True
    if id_exist == True:
        list_kind.append(dict({'id': id_kind, 'name': label}))
        return jsonify(list_kind)


# The POST method implementation  ---Crud (Create of CRUD)           
def post(id_kind, list_kind, label):
    id_exist = False
    for i in range(len(list_kind)):
        if list_kind[i-1]['id'] == id_kind:
            id_exist = True
    
    if id_exist == False:
        list_kind.append(dict({'id': id_kind, 'name': label}))
        return jsonify(list_kind)
    else:
        return "ID already exist"


# The GET all-events method implementation
def get_all(list_kind):
    return jsonify(list_kind)


#------------------- Route mapping to the methods declared above for STUDENTS -----------------------------

@app.route('/')
def student():
    return "Hi from Irdi Caushaj"



@app.route('/v1/student/<int:student_id>', methods=["GET","DELETE"])
def student_crud_gd(student_id):
    if request.method == "GET":
        return get(student_id, students_list)
    else:
        return delete(student_id, students_list)
   


@app.route('/v1/student/<int:student_id>/<name>', methods=["POST","PUT"])
def student_crud_pp(student_id, name):
    if request.method == "POST":
        return post(student_id, students_list, name)
    else:
        return put(student_id, students_list, name)



@app.route('/v1/students', methods=["GET"])
def student_r():
    return get_all(students_list)

#------------------- Route mapping to the methods declared above for STUDENTS -----------------------------


#------------------- Route mapping to the methods declared above for COURSES-----------------------------

@app.route('/')
def course():
    return "Hi from Irdi Caushaj"



@app.route('/v2/course/<int:course_id>', methods=["GET","DELETE"])
def course_crud_gd(course_id):
    if request.method == "GET":
        return get(course_id, course_list)
    else:
        return delete(course_id, course_list)
   


@app.route('/v2/course/<int:course_id>/<name>', methods=["POST","PUT"])
def course_crud_pp(course_id, name):
    if request.method == "POST":
        return post(course_id, course_list, name)
    else:
        return put(course_id, course_list, name)



@app.route('/v2/courses', methods=["GET"])
def course_retrieve():
    return get_all(course_list)

#------------------- Route mapping to the methods declared above for COURSES-----------------------------


#------------------- Route mapping to the methods declared above for EVENTS-----------------------------

@app.route('/')
def event():
    return "Hi from Irdi Caushaj"



@app.route('/v3/event/<int:event_id>', methods=["GET","DELETE"])
def event_crud_gd(event_id):
    if request.method == "GET":
        return get(event_id, event_list)
    else:
        return delete(event_id, event_list)
   


@app.route('/v3/event/<int:event_id>/<event>', methods=["POST","PUT"])
def event_crud_pp(event_id, event):
    if request.method == "POST":
        return post(event_id, event_list, event)
    else:
        return put(event_id, event_list, event)



@app.route('/v3/events', methods=["GET"])
def event_retrieve():
    return get_all(event_list)

#------------------- Route mapping to the methods declared above for EVENTS-----------------------------
