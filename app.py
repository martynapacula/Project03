import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'task_manager'
app.config["MONGO_URI"] = 'mongodb+srv://first_user14:F1rstUser@project03-4ieku.mongodb.net/task_manager?retryWrites=true&w=majority'
mongo = PyMongo(app)


@app.route('/')
@app.route('/get_experiment')
def get_experiment():
    return render_template("tasks.html",
                           tasks=mongo.db.tasks.find())


@app.route('/add_experiment')
def add_experiment():
    return render_template('addtask.html',
                           categories=mongo.db.categories.find())


@app.route('/insert_experiment', methods=['POST'])
def insert_experiment():
    tasks = mongo.db.tasks
    tasks.insert_one(request.form.to_dict())
    return redirect(url_for('get_experiment'))


@app.route('/edit_experiment/<task_id>')
def edit_experiment(task_id):
    the_task = mongo.db.tasks.find_one({"_id": ObjectId(task_id)})
    all_categories = mongo.db.categories.find()
    return render_template('edittask.html', task=the_task,
                           categories=all_categories)


@app.route('/update_experiment/<task_id>', methods=["POST"])
def update_experiment(task_id):
    tasks = mongo.db.tasks
    tasks.update({'_id': ObjectId(task_id)},
    {
        'experiment_name': request.form.get('experiment_name'),
        'Category_name': request.form.get('Category_name'),
        'description': request.form.get('description'),
        'beginning_date': request.form.get('beginning_date'),
        'non_hazardous': request.form.get('non_hazardous')

    })
    return redirect(url_for('get_experiment'))


@app.route('/delete_experiment/<task_id>')
def delete_experiment(task_id):
    mongo.db.tasks.remove({'_id': ObjectId(task_id)})
    return redirect(url_for('get_experiment'))


@app.route('/get_cat_experiment')
def get_cat_experiment():
    return render_template('categories.html',
                           categories=mongo.db.categories.find())
                       

@app.route('/edit_cat_experiment/<category_id>')
def edit_cat_experiment(category_id):
    return render_template('editcategory.html',
    category=mongo.db.categories.find_one({'_id': ObjectId(category_id)}))

@app.route('/update_cat_experiment/<category_id>', methods=['POST'])
def update_cat_experiment(category_id):
    mongo.db.categories.update(
        {'_id': ObjectId(category_id)},
        {'Category_name': request.form.get('Category_name')})
    return redirect(url_for('get_cat_experiment'))

@app.route('/delete_cat_experiment/<category_id>')
def delete_cat_experiment(category_id):
    mongo.db.categories.remove({'_id': ObjectId(category_id)})
    return redirect(url_for('get_cat_experiment'))


    
@app.route('/insert_cat_experiment', methods=['POST'])
def insert_cat_experiment():
    category_doc = {'Category_name': request.form.get('Category_name')}
    mongo.db.categories.insert_one(category_doc)
    return redirect(url_for('get_cat_experiment'))


@app.route('/add_cat_experiment')
def add_cat_experiment():
    return render_template('addcategory.html')


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=False)
