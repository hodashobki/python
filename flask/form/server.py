from logging import debug
from flask import Flask, app , render_template, request,redirect,session
app=Flask (__name__)
app.secret_key="keep it secret, keep it safe"

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/user", methods=["Post"])
def user_info():
    session["user_name"]=request.form["user_name"]
    session["email"]=request.form["email"]
    return redirect("/show")

@app.route("/show")
def show_user():
    return render_template("index1.html" ,name=session["user_name"], email=session["email"])



if __name__=="__main__":
    app.run(debug = True)    

