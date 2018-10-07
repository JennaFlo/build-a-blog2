from flask import Flask, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:password@localhost:8889/get-it-done'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

class Task(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    blog = db.Column(db.String(1200))

    def __init__(self, name):
        self.name = name
    
    def __init__(self, blog):
        self.blog = blog

def blog_name():
    if blog_name == "":
        return "Please enter a title"
    else:
        return ""

def blog_body():
    if blog_body == "":
        return "Please enter a blog entry"
    else:
        return ""

blogs = []

@app.route('/', methods=['GET', 'POST'])
def blogs():
    if request.method == 'POST':
        blog_name = request.form['name']
        blog_body = request.form['body']
        new_blog = Blog(blog_name, blog_body)
        db.session.add(blog_name)
        db.session.add(blog_body)
        db.session.commit()

    blogs = blog.query.all()

    return render_template('blogs.html', title='Build a Blog!', blog = blog, name = name)



if __name__ == '__main__':
    app.run()