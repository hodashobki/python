from flask import Flask ,render_template 
app = Flask(__name__)    
@app.route('/')         
def hello_world():
    return render_template  ("index.html")

@app.route('/users/<username>/<id>') # for a route '/users/____/____', two parameters in the url get passed as username and id
def show_user_profile(username, id):
    print(username)
    print(id)
    return "username: " + username + ", id: " + id

if __name__=="__main__":     
    app.run(debug=True)   
