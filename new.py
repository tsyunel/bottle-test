from bottle import Bottle, run


app = Bottle()

@app.get("/")
def hello():
    return "<h1>hello world</h1>"   

@app.get("/movies")
def movies():
    return "<h1><i>a lot movies</i></h1>"  
    
