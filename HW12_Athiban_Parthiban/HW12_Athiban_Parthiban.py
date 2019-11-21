""" Home Work #12 """

from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/instructors')
def hello():
    db_path = "/Users/athibanp/athiban/ms-cs/SSW-810/Assignments/810_hw11.db"
    db = sqlite3.connect(db_path)
    ins_data_db = list()
    query = ''' SELECT CWID, Name, Dept, T.Course, T.STUDENTS
                        FROM instructors , (select Course, count(StudentCWID) AS STUDENTS, InstructorCWID  from grades group by Course, InstructorCWID) as T
                            WHERE instructors.CWID = T.InstructorCWID '''

    for cwid, name, dept, course, students in db.execute(query):
        ins_data_db.append((cwid, name, dept, course, students))
    return render_template('instructors.html',
                            title="Instructors Table",
                            my_header="Stevens Repository",
                            table_title="Instructor details",
                            instructors=ins_data_db)


app.run(debug=True)
