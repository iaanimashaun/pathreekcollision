from flask import Flask, render_template
app = Flask(__name__)


app.config['ENV'] = 'development'
app.config['DEBUG'] = True
app.config['TESTING'] = True


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/about/")
def about():
    return render_template('about.html')

@app.route("/advice/")
def advice():
    return render_template('advice.html')

@app.route("/blog/")
def blog():
    return render_template('blog.html')

@app.route("/bookshelf/")
def bookshelf():
    return render_template('bookshelf.html')

@app.route("/culture/")
def culture():
    return render_template('culture.html')

@app.route("/fast/")
def fast():
    return render_template('fast.html')


@app.route("/growth/")
def growth():
    return render_template('growth.html')


if __name__ == "__main__":
    app.run()