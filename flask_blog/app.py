from flask import Flask, render_template

 
app = Flask(__name__)

@app.route("/")
def index():
    article = dict()
    article["title"] = "test"
    article["body"] = "Test 5555"
    article["author"] = "Selcuk Akarın"
    return render_template('index.html', article = article)

@app.route("/about")
def about():
    return "Hakkında"

@app.route("/about/selcuk")
def about_selcuk():
    return "Selcuk hakkında"

 
if __name__ == "__main__":
    app.run(debug=True)

