from flask import Flask, render_template, request, redirect,session
app=Flask(__name__)
app.secret_key="Secret"

@app.route("/")
def show_index():
    return render_template("index.html")


@app.route("/survey" ,methods=["Post"])
def survey_result():
    session["user-name"]=request.form["user-name"]
    session["location"]=request.form["location"]
    session["comment"]=request.form["comment"]
    session["pyth"]=request.form["pyth"]
    session["language"]=request.form["language"]
    return redirect("/show")


@app.route("/show")
def show_info():
    return render_template("info.html" ,name=session["user-name"], location=session["location"],
    language =session["language"], course1= session["pyth"],
     comment=session["comment"])

@app.route('/goback')
def go_back():
    session.clear()
    return redirect('/')


if __name__==("__main__"):
    app.run(debug=True)    