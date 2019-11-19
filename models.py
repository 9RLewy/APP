from app import db


# initialize one table called Tasks in the database
class Tasks(db.Model):
    taskId = db.Column(db.Integer, primary_key=True)
    taskname = db.Column(db.String(250), index=True)
    des = db.Column(db.String(250), index=True)
    state = db.Column(db.String(250), index=True)
    year = db.Column(db.Date)

    def __repr__(self):
        return self.year + ' ' + self.taskname + ' ' + self.state


class Students(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, index=True)
    stuname = db.Column(db.String(250), index=True)
    age = db.Column(db.Integer, index=True)

    def __repr__(self):
        return self.userId + ' ' + self.stuname + ' ' + self.age
