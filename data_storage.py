import json

JSON_FILE = 'data/blogs.json'


def load_data():
    """To read all the blogs from JSON file"""
    with open(JSON_FILE,"r",encoding='UTF-8') as handle:
        return json.load(handle)


def save_data(blog_posts):
    """To save(overwrite) all the details to JSON file"""
    with open(JSON_FILE, "w") as handle:
        return json.dump(blog_posts, handle, indent=4)

def post_data(post):
    """To add a new blog to JSON"""
    blog_posts = load_data()
    if blog_posts:
        max_id = max([blog['id'] for blog in blog_posts])
        post_id = max_id + 10
        post['id'] = post_id
    else:
        post['id'] = 10
    # Add blogs to JSON
    blog_posts.append(post)
    # Save JSON
    save_data(blog_posts)


def delete_data(post_id):
    """To delete blog from JSON file"""
    blog_posts = load_data()
    # To find the matching blog
    for blog in blog_posts:
        if blog['id'] == post_id:
            #Removed from JSON
            blog_posts.remove(blog)
            # Save JSON
            save_data(blog_posts)
            return True
    return None


def fetch_post_by_id(post_id):
    """To fetch a specific blog details using the ID(post_id)"""
    blog_posts = load_data()
    for blog in blog_posts:
        if blog['id'] == post_id:
            return blog
    return None


def update_data(new_blog):
    """Update the blog. id will be same and is a key in new_blog"""
    blog_posts = load_data()
    # Fetching the old blog with same ID
    for blog in blog_posts:
        if blog['id'] == new_blog['id']:
            # update the dictionary with new details
            blog.update(new_blog)
            # Saving JSON
            save_data(blog_posts)
            return True
    return None




