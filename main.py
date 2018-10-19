from flask import Flask, request, redirect, render_template, flash, session
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog2:password@localhost:8889/build-a-blog2'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)
app.secret_key = 'y337kGcys&zP3B'

class Blog(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    blog = db.Column(db.String(1200))

    def __init__(self, name, blog):
        self.name = name
        self.blog = blog
    
   

def blog_name_validate(name):
    if name == "":
        return "Please enter a title"
    else:
        return ""

def blog_body_validate(content):
    if content == "":
        return "Please enter a blog entry"
    else:
        return ""


@app.route('/blogs', methods=['GET', 'POST'])
def blogs():

    id = request.args.get('id')
    if id != None:
        data=Blog.query.filter_by(id=id).all()
        return render_template('blogs.html', title=data[0].name, blogs=data[0], single_post=True)
    else:
        data=Blog.query.all()
        return render_template('blogs.html', title="Build A Blog", blogs=data, single_post=False)
    
@app.route('/newposts', methods=['GET', 'POST'])
def create_blog():
    if request.method == 'POST':
        blog_name = request.form.get('name')
        blog_body = request.form.get('content')
        if blog_name_validate(blog_name) or blog_body_validate(blog_body) != "":
            return render_template('newposts.html', title="Add a blog", title_error=blog_name_validate(blog_name), content_error=blog_body_validate(blog_body), old_name=blog_name, old_post=blog_body)
        else:
            new_blog = Blog(blog_name, blog_body)
            db.session.add(new_blog)
            db.session.commit()
            return redirect('/blogs?id=' + str(new_blog.id))
    else:
        return render_template("newposts.html", title="Add a blog")    

   


if __name__ == '__main__':
    app.run()