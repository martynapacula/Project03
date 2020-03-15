import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'task_manager'
app.config["MONGO_URI"] = 'mongodb+srv://first_user14:F1rstUser@project03-4ieku.mongodb.net/task_manager?retryWrites=true&w=majority'
mongo = PyMongo(app)


@app.route('/add_task')
def add_task():
    return render_template('addtask.html')


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=False)

