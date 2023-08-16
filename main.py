from flask import Flask, render_template
from requests import get
from post import Post

app = Flask(__name__)

response = get("https://api.npoint.io/c790b4d5cab58020d391").json()
post_objects = []
for post in response:
    post_object = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_objects.append(post_object)


@app.route('/')
def home():
    return render_template("index.html", all_posts=post_objects)

@app.route("/<int:index>")
def show_post(index):
    for post_n in post_objects:
        if post_n.id == index:
            return render_template("post.html", post=post_n)



if __name__ == "__main__":
    app.run(debug=True)
