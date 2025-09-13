from flask import Flask, render_template
from data_fetch import load_data

JSON_FILE = 'data/blogs.json'
app = Flask(__name__)

@app.route('/')
def index():
    # to fetch the blog posts from a file
    blog_posts = load_data(JSON_FILE)
    return render_template('index.html', posts=blog_posts)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)