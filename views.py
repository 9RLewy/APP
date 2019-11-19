from flask import render_template, flash, redirect, session, url_for, request, g
from flask_admin.contrib.sqla import ModelView

from app import app, db, admin
from .models import Tasks, Students

from .forms import TasksForm, STasksForm, StudForm

import datetime

admin.add_view(ModelView(Tasks, db.session))
admin.add_view(ModelView(Students, db.session))


@app.route('/students', methods=['GET'])
def getAllStudents():
    students = Students.query.all()
    return render_template('students_list.html',
                           title='All Students',
                           students=students)


# homepage
@app.route("/")
def homepage():
    return render_template('index.html',
                           title='homepage',
                           )


@app.route('/create_student', methods=['GET', 'POST'])
def create_student():
    form = StudForm()
    flash('Errors="%s"' %
          form.errors)
    if form.validate_on_submit():
        t = Students(userId=form.userId.data, stuname=form.stuname.data, age=form.age.data)
        db.session.add(t)
        # database update and affirm
        db.session.commit()
        return redirect('/students')

    return render_template('create_student.html',
                           title='Create Student',
                           form=form)


# edit task
@app.route('/edit_student/<id>', methods=['GET', 'POST'])
def edit_student(id):
    student = Students.query.get(id)
    form = StudForm(obj=student)
    flash('Errors="%s"' %
          (form.errors))
    if form.validate_on_submit():
        t = student
        t.userId = form.userId.data
        t.stuname = form.stuname.data
        t.age = form.age.data
        db.session.commit()
        return redirect('/students')

    return render_template('edit_student.html',
                           title='Edit Student',
                           form=form)


@app.route('/delete_student/<id>', methods=['GET'])
def delete_student(id):
    student = Students.query.get(id)
    db.session.delete(student)
    db.session.commit()
    return redirect('/students')


# create a new task
@app.route('/create_task', methods=['GET', 'POST'])
def create_task():
    form = TasksForm()
    form.state.data = "No"
    flash('Errors="%s"' %
          form.errors)
    if form.validate_on_submit():
        t = Tasks(taskname=form.taskname.data, des=form.des.data, state=form.state.data, year=form.year.data)
        db.session.add(t)
        # database update and affirm
        db.session.commit()
        return redirect('/tasks')

    return render_template('create_task.html',
                           title='Create Student',
                           form=form)


# get all tasks (all tasks management page)
@app.route('/tasks', methods=['GET'])
def getAllTasks():
    tasks = Tasks.query.all()
    return render_template('task_list.html',
                           title='All Tasks',
                           tasks=tasks)


# edit task
@app.route('/edit_task/<id>', methods=['GET', 'POST'])
def edit_task(id):
    task = Tasks.query.get(id)
    form = TasksForm(obj=task)
    flash('Errors="%s"' %
          (form.errors))
    if form.validate_on_submit():
        t = task
        t.taskname = form.taskname.data
        t.des = form.des.data
        t.state = form.state.data
        t.year = form.year.data
        db.session.commit()
        return redirect('/tasks')

    return render_template('edit_task.html',
                           title='Edit Task',
                           form=form)


# delete task
@app.route('/delete_task/<id>', methods=['GET'])
def delete_task(id):
    task = Tasks.query.get(id)
    db.session.delete(task)
    db.session.commit()
    return redirect('/tasks')


# change a task's state: No to Yes
@app.route('/com_task/<id>', methods=['GET'])
def com_task(id):
    task = Tasks.query.get(id)
    if task.state == "No":
        task.state = "Yes"
        db.session.commit()
    return redirect('/tasks')


# change a task's state: Yes to No
@app.route('/recall_task/<id>', methods=['GET'])
def recall_task(id):
    task = Tasks.query.get(id)
    if task.state == "Yes":
        task.state = "No"
        db.session.commit()
    return redirect('/tasks')


# look all completed tasks
@app.route('/comp_tasks', methods=['GET'])
def getCompTasks():
    tasks = Tasks.query.filter_by(state='Yes').all()
    return render_template('comp_tasks.html',
                           title='All Tasks',
                           tasks=tasks)


# look all uncompleted tasks
@app.route('/uncomp_tasks', methods=['GET'])
def getUncompTasks():
    tasks = Tasks.query.filter_by(state='No').all()
    return render_template('uncomp_tasks.html',
                           title='All Tasks',
                           tasks=tasks)


# look all tasks in a specific day
@app.route('/sel_tasks', methods=['GET', 'POST'])
def getSelTasks():
    form = STasksForm()
    if form.validate_on_submit():
        # use the statement to get all entries in the database that the user wanted
        tasks = Tasks.query.filter_by(year=form.year.data).all()
        return render_template('lsel_task.html',
                               title='All Tasks',
                               tasks=tasks)
    return render_template('sel_tasks.html',
                           title='All Tasks',
                           form=form)


# get today's tasks
@app.route('/today_tasks', methods=['GET'])
def gettodayTasks():
    forms = STasksForm()
    # store today's time  in the form,then filter the corresponding tasks from the database
    forms.year.data = ((datetime.datetime.now() - datetime.timedelta(days=0)).strftime("%Y-%m-%d"))
    tasks = Tasks.query.filter_by(year=forms.year.data).all()
    return render_template('tod_tasks.html',
                           title='All Tasks',
                           tasks=tasks)


# tasks in 3 days
@app.route('/i3days_tasks', methods=['GET'])
def get3todayTasks():
    forms = STasksForm()
    forms.year.data = ((datetime.datetime.now() + datetime.timedelta(days=0)).strftime("%Y-%m-%d"))
    tasks = Tasks.query.filter_by(year=forms.year.data).all()
    task = tasks
    # get tasks in 3 days
    for t in range(1, 3):
        forms.year.data = ((datetime.datetime.now() + datetime.timedelta(days=t)).strftime("%Y-%m-%d"))
        tasks = Tasks.query.filter_by(year=forms.year.data).all()
        task = task + tasks
    return render_template('tasks3days.html',
                           title='All Tasks',
                           tasks=task)


# tasks in 15 days
@app.route('/i15days_tasks', methods=['GET'])
def get15todayTasks():
    forms = STasksForm()
    forms.year.data = ((datetime.datetime.now() + datetime.timedelta(days=0)).strftime("%Y-%m-%d"))
    tasks = Tasks.query.filter_by(year=forms.year.data).all()
    task = tasks
    # get tasks in 3 days
    for t in range(1, 15):
        forms.year.data = ((datetime.datetime.now() + datetime.timedelta(days=t)).strftime("%Y-%m-%d"))
        tasks = Tasks.query.filter_by(year=forms.year.data).all()
        task = task + tasks
    return render_template('tasks15days.html',
                           title='All Tasks',
                           tasks=task)
