import json
from textwrap import indent

JSON_FILE = 'data/blogs.json'


def load_data():
    with open(JSON_FILE,"r",encoding='UTF-8') as handle:
        return json.load(handle)

def save_data(blog_posts):
    with open(JSON_FILE, "w") as handle:
        return json.dump(blog_posts, handle, indent=4)

def post_data(post, filepath):
   blog_posts = load_data()
   if blog_posts:
       max_id = max([blog['id'] for blog in blog_posts])
       post_id = max_id + 10
       post['id'] = post_id
   else:
       post['id'] = 10
   post_id = str(len(blog_posts)*10 + 10)

   #post[post_id] = post
   blog_posts.append(post)
   save_data(blog_posts)


def delete_data(post_id):
    blog_posts = load_data()
    for blog in blog_posts:
        if blog['id'] == post_id:
            blog_posts.remove(blog)
            break
    save_data(blog_posts)
