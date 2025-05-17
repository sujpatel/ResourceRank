import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import praw

load_dotenv()

app = Flask(__name__)
CORS(app)

reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent=os.getenv("REDDIT_USER_AGENT")
)

@app.route('/search')
def search():
    query = request.args.get("q","")
    posts = reddit.subreddit("learnprogramming").search(query, limit=3)
    
    results = []
    
    for post in posts:
        post.comments.replace_more(limit=0)
        top_comment = post.comments[0].body if post.comments else ""
        
        results.append({
            "title": post.title,
            "url": post.url,
            "top_comment": top_comment
        })
        
    return jsonify({"results": results})

if __name__ == '__main__':
    app.run(debug=True)
    