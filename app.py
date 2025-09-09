from fastapi import FastAPI

app = FastAPI(__name__)

@app.get('/version')
def version():
    return {'version' : 1}

@app.get('/')
def page():
    return 'dev'
