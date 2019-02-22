from flask import Flask, jsonify
from flask_restful import Resource, Api
from models.course_module import Course_one, All_courses, Course_two
from models.student_module import Student_one, All_students, Student_two
from models.event_module import Event_one, All_events, Event_two


app = Flask(__name__)

api = Api(app)

@app.route('/')
def home():
    return 'Hello from Irdi Caushaj'

 
api.add_resource(Course_one, '/course/<int:course_id>/<name>')
api.add_resource(Course_two, '/course/<int:course_id>/')

api.add_resource(Student_one, '/student/<int:student_id>/<name>')
api.add_resource(Student_two, '/student/<int:student_id>/')

api.add_resource(Event_one, '/event/<int:event_id>/<event>')
api.add_resource(Event_two, '/event/<int:event_id>/')


api.add_resource(All_courses, '/courses/')
api.add_resource(All_students, '/students/')
api.add_resource(All_events, '/events/')