from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html')

@app.route("/recent-post")
def recentpost():
    return render_template('recent-post.html')

@app.route("/about-me")
def about_me():
    return render_template('about-me.html')

if __name__ == '__main__':

    app.run(debug=True, host='0.0.0.0')
