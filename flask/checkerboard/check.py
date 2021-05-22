from flask import Flask, render_template
app = Flask(__name__)
#http://localhost:5000 - should display 8 by 8 checkerboard
@app.route('/')
def index():
    return render_template("index.html",num_row=8,num_col=8)

#http://localhost:5000/4 - should display 8 by 4 checkerboard
@app.route('/<num>')
def checker1(num):
     return render_template("index.html",num_row=int(num),num_col=8) 
@app.route('/<num>/<num1>')
def checker2(num,num1):
     return render_template("index.html",num_row=int(num),num_col=int(num1))
                  
if __name__=="__main__":
    app.run(debug=True)