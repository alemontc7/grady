from flask import Flask, redirect, render_template, request, url_for
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('mongodb://localhost:27017/')
db = client['Universidad'] 
subjects_collection = db['materias']

@app.route('/')
def index():
    subjects_data = subjects_collection.find()
    subjects = [subject['subject_name'] for subject in subjects_data]
    return render_template('index.html', subjects=subjects)

@app.route('/register_subject', methods=['POST'])
def register_subject():
    dict = request.form.to_dict()
    subjects_count = subjects_collection.count_documents({})
    dict['_id'] = str(subjects_count)
    subjects_collection.insert_one(dict)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)