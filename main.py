from fastapi import FastAPI, Depends, HTTPException, status, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/home", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        name="home.html",
        context={"request": request}
    )

@app.get("/reviews", response_class=HTMLResponse)
def reviews(request: Request):
    return templates.TemplateResponse(
        name="reviews.html",
        context={"request": request}
    )

@app.get("/about", response_class=HTMLResponse)
def about(request: Request):
    return templates.TemplateResponse(
        name="about.html",
        context={"request":request}
    )