from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def inicio():
	return {"menssage ": "My first API"}

@app.get("/sobre")
def sobre():
	return {
	"linguagens": "Py, Js, JAVA, C, C++",
	"Nome": "William Gabriel",
	"Idade": 17,
	}
