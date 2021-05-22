from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return render_template("play.html")
@ app.route("/play/<int:x>")
def repeat(x):
    return render_template("index.html",times=x) 

@ app.route("/play/<int:x>/<color>")
def color(x,color):
    return render_template("index2.html",times=x,c=color)

          
if __name__=="__main__":
    app.run(debug=True)
