from flask import Flask  
app = Flask(__name__)    
@app.route('/')          
def hello_world():
    return 'Hello World!'

@app.route(('/dojo'))
def dojoo():
    return "Dojo!"

@app.route('/say/<name>')
def hi_flask(name):
    return "Hi " + name +"!"

# @app.route('/repeat/<num>/<name>') 
# def repeat_words(num,name):
#     str = " "
#     for i in range(int(num)):
#         str=str + name 
#     return str   

@app.route('/repeat/<num>/<name>') 
def repeat_words(num,name):
    str = ''
    for i in range(int(num)):
        str=str + '<p> '+name  +' </p>'
    return str   


if __name__=="__main__":      
    app.run(debug=True)