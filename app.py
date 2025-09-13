from flask import Flask, render_template, request, redirect, url_for
from data_storage import load_data, post_data, delete_data


app = Flask(__name__)

@app.route('/')
def index():
    # to fetch the blog posts from a file
    blog_posts = load_data()
    return render_template('index.html', posts=blog_posts)


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        # Add the code that handles adding a new blog
        blog_post = request.form.get()
        post_data(blog_post)
        return redirect(url_for('index'))
    return render_template('add.html')


@app.route('/delete',<post_id>)
def delete(post_id):
    delete_data(post_id)
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)