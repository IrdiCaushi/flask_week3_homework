from flask import Flask, request, jsonify

app = Flask(__name__, static_url_path='/static')



course_list = [
    {"id": 1, "name": "COS340a"},
    {"id": 2, "name": "COS310a"},
    {"id": 3, "name": "COS220b"}
]

#----------------------------- Method Section --------------------------------------

# The GET method implementation  ---cRud (Retrieve of CRUD)
def get_course(course_id):
    flag = False
    for course in course_list:
        if course["id"] == course_id:
            flag = True
            return jsonify(course)
    if flag == False:    
        return "ID not Found!"

# The DELETE method implementation ---cruD (Delete of CRUD)
def delete_course(course_id):
    flag = False
    for i in range(len(course_list)): 
        if course_list[i]['id'] == course_id: 
            del course_list[i]
            flag = True
            return "Course deleted!"

    if flag == False:
        return "ID not Found!"

# The PUT method implementation ---crUd (Update of CRUD)
def put_course(course_id, name):
    id_exist = False

    for a in course_list:
        if a["id"] == course_id:
            a.update({'name': name})
            id_exist = True
            return jsonify(a)

    if id_exist == False:
        course_list.append(dict({'id': course_id, 'name': name}))
        return jsonify(course_list)

    return jsonify(course_list)

# The POST method implementation  ---Crud (Create of CRUD)           
def post_course(course_id, name):
    id_exist = False
    for i in range(len(course_list)):
        if course_list[i-1]['id'] == course_id:
            id_exist = True
    
    if id_exist == False:
        course_list.append(dict({'id': course_id, 'name': name}))
        return jsonify(course_list)
    else:
        return "ID already exist"
    
# The GET all-events method implementation
def get_courses():
    return jsonify(course_list)


#------------------- Route mapping to the methods declared above -----------------------------

@app.route('/')
def main():
    return "Hi from Irdi Caushaj"



@app.route('/v2/course/<int:course_id>', methods=["GET","DELETE"])
def course_crud_gd(course_id):
    if request.method == "GET":
        return get_course(course_id)
    else:
        return delete_course(course_id)
   


@app.route('/v2/course/<int:course_id>/<name>', methods=["POST","PUT"])
def course_crud_pp(course_id, name):
    if request.method == "POST":
        return post_course(course_id, name)
    else:
        return put_course(course_id, name)



@app.route('/v2/courses', methods=["GET"])
def course_retrieve():
    return get_courses()

