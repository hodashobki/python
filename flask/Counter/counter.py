from flask import Flask , render_template, redirect,request,session
app=Flask(__name__)
app.secret_key="secret"


@app.route("/")
def index():
    if "counter" in session:
        session["counter"]+=1
        
    else:
        session["counter"]=0
        
    return render_template("index.html" ,counter=session["counter"])        
        

@app.route('/plustwo')
def plus_two():
    session['counter']+=1
    return redirect('/')
@app.route('/reset')
def reset():
    session['counter']=0
    return redirect('/') 


if __name__=="__main__":
    app.run(debug = True)            