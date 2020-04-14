from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET KEY'] = '41ecc1788dbebaa1eccb8ce56834d0b3'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
posts = [
    {
        "author": "Rhys Murage",
        "title": "Blog Post 1",
        "content": "First post content",
        "date_posted": "April 21, 2020"

    },
    {
        "author": "Jane Doe",
        "title": "Blog Post 2",
        "content": "Second post content",
        "date_posted": "April 21, 2018"

    }
]


@app.route('/')
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)


@app.route("/home2")
def home2():
    return render_template("home2.html", posts=posts)


@app.route('/about')
def about():
    return render_template("about.html", title=about)


@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template("register.html", title="Register", form=form)


if __name__ == '__main__':
    app.run(debug=True)
# commit
