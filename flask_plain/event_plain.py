from flask import Flask, request, jsonify

app = Flask(__name__, static_url_path='/static')



event_list = [
    {"id": 1, "event": "Quiz 1"},
    {"id": 2, "event": "Mid-Term"},
    {"id": 3, "event": "Final"}
]

#----------------------------- Method Section --------------------------------------

# The GET method implementation  ---cRud (Retrieve of CRUD)
def get_event(event_id):
    flag = False
    for event in event_list:
        if event["id"] == event_id:
            flag = True
            return jsonify(event)
    if flag == False:    
        return "ID not Found!"

# The DELETE method implementation ---cruD (Delete of CRUD)
def delete_event(event_id):
    flag = False
    for i in range(len(event_list)): 
        if event_list[i]['id'] == event_id: 
            del event_list[i] 
            flag = True
            return "Event deleted!"

    if flag == False:
        return "ID not Found!"

# The PUT method implementation ---crUd (Update of CRUD)
def put_event(event_id, event):
    id_exist = False

    for a in event_list:
        if a["id"] == event_id:
            a.update({'event': event})
            id_exist = True
            return jsonify(a)

    if id_exist == False:
        event_list.append(dict({'id': event_id, 'event': event}))
        return jsonify(event_list)

    return jsonify(event_list)

# The POST method implementation  ---Crud (Create of CRUD)           
def post_event(event_id, event):
    id_exist = False
    for i in range(len(event_list)):
        if event_list[i-1]['id'] == event_id:
            id_exist = True
    
    if id_exist == False:
        event_list.append(dict({'id': event_id, 'event': event}))
        return jsonify(event_list)
    else:
        return "ID already exist"
    
# The GET all-events method implementation
def get_events():
    return jsonify(event_list)


#------------------- Route mapping to the methods declared above -----------------------------

@app.route('/')
def main():
    return "Hi from Irdi Caushaj"



@app.route('/v3/event/<int:event_id>', methods=["GET","DELETE"])
def event_crud_gd(event_id):
    if request.method == "GET":
        return get_event(event_id)
    else:
        return delete_event(event_id)
   


@app.route('/v3/event/<int:event_id>/<event>', methods=["POST","PUT"])
def event_crud_pp(event_id, event):
    if request.method == "POST":
        return post_event(event_id, event)
    else:
        return put_event(event_id, event)



@app.route('/v3/events', methods=["GET"])
def event_retrieve():
    return get_events()