from fastapi import FastAPI

# creating instace of an app
app=FastAPI()

# / means base url or localhost. '/' is called as path
#.get or post is called as operation
#@app decorator is called path operation decorator
@app.get('/')
#this function is called path operation function
def index():
    return {"data":{"name":"Aman"}}

@app.get('/about')
def about():
    return {"data":'about page'}




# to start virtual env - source <path>/env/acivate
#command to run the server - uvicorn main:app --reload
# it means file name is "main" and instance name is "app"

#ow the above code works
'''
1) From fastapi import FastAPI
2) Then we create an instace of an app (we pass the file name in uvicorn command. Here the file name is main so we 
are passing main in uvicorn command. We have instace name ass so we pass main:app in uvicorn . If the name is different we will
pass different name. -- reload is not mandatory .It just reload everyhimr there is a code change i.e its keep tracking the 
changes.


'''