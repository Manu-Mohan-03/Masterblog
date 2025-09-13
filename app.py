from flask import Flask, render_template, request, redirect, url_for
import data_storage as blogs


app = Flask(__name__)

@app.route('/')
def index():
    # to fetch the blog posts from a file
    blog_posts = blogs.load_data()
    return render_template('index.html', posts=blog_posts)


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        # Add the code that handles adding a new blog
        blog_post = request.form.get()
        blogs.post_data(blog_post)
        return redirect(url_for('index'))
    return render_template('add.html')


@app.route('/delete/<int:post_id>')
def delete(post_id):
    blogs.delete_data(post_id)
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)


@app.route('/update/<post_id>', methods = ['GET', 'POST'])
def update(post_id):
    # Fetch the blog posts from the JSON file
    post = blogs.fetch_post_by_id(post_id)
    if post is None:
        # Post not found
        return "Post not found", 404
    if request.method == 'POST':
        # Update the post in the JSON file
        # Redirect back to index
        blog = request.form.get()
        blogs.update_data(post_id,blog)
    else:
        # Else, it's a GET request
        # So display the update.html page
        return render_template('update.html', post=post)
