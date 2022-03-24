from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from logic.person import Person
from logic.documents import Documents

app = Flask(__name__)
bootstrap = Bootstrap(app)
model_people = []
model_document = []


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/person', methods=['GET'])
def person():
    return render_template('person.html')


@app.route('/person_detail', methods=['POST'])
def person_detail():
    id_person = request.form['id_person']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    p = Person(id_person=id_person, name=first_name, last_name=last_name)
    model_people.append(p)
    return render_template('person_detail.html', value=p)


@app.route('/people')
def people():
    data = [(i.id_person, i.name, i.last_name) for i in model_people]
    print(data)
    return render_template('people.html', value=data)


@app.route('/books')
def books():
    data = [(i.id_document, i.title, i.number_page, i.category, i.name, i.last_name) for i in model_document]
    print(data)
    return render_template('books.html', value=data)


@app.route('/docs_detail', methods=['POST'])
def document_detail():
    id_document = request.form['id_document']
    title = request.form['title']
    number_page = request.form['number_page']
    category = request.form['category']
    name_author = request.form['name_author']
    name_author2 = request.form['name_author2']

    p = Documents(id_document=id_document, title=title, number_page=number_page, category=category,
                  name_author=name_author + ',' + name_author2 , name_author2=name_author2)
    model_document.append(p)
    return render_template('docs_detail.html', value=p)


@app.route('/docs', methods=['GET'])
def document():
    return render_template('docs.html')


if __name__ == '__main__':
    app.run()
