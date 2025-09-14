from flask import Flask, render_template, request, redirect, url_for
import data_storage as blogs


app = Flask(__name__)

@app.route('/')
def index():
    """Home page"""
    # to fetch the blog posts from a file
    blog_posts = blogs.load_data()
    return render_template('index.html', posts=blog_posts)


@app.route('/add', methods=['GET', 'POST'])
def add():
    """To create a new blog"""
    if request.method == 'POST':
        # Add the code that handles adding a new blog
        blog_post = {}
        blog_post['title'] = request.form.get('title')
        blog_post['author'] = request.form.get('author')
        blog_post['content'] = request.form.get('content')
        blogs.post_data(blog_post)
        # Redirect back to index
        return redirect(url_for('index'))
    # GET request means render the page for adding new blog
    return render_template('add.html')


@app.route('/delete/<int:post_id>')
def delete(post_id):
    """To delete an existing blog"""
    blogs.delete_data(post_id)
    # Redirect back to index
    return redirect(url_for('index'))


@app.route('/update/<int:post_id>', methods = ['GET', 'POST'])
def update(post_id):
    """To update an exising blog"""
    # Fetch the blog posts from the JSON file
    post = blogs.fetch_post_by_id(post_id)
    if post is None:
        # Post not found
        return "Post not found", 404
    if request.method == 'POST':
        # Update the post in the JSON file
        blog_post = {}
        blog_post['id'] = post_id
        blog_post['title'] = request.form.get('title')
        blog_post['author'] = request.form.get('author')
        blog_post['content'] = request.form.get('content')
        blogs.update_data(blog_post)
        # Redirect back to index
        return redirect(url_for('index'))
    # Else, it's a GET request, so go to update blog page
    return render_template('update.html', post=post)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)