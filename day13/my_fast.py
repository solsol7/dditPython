from fastapi import FastAPI, Form, Request
import uvicorn
from starlette.responses import HTMLResponse
from fastapi.params import Form
from fastapi.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles

templates = Jinja2Templates(directory="templates")
app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def forw(request: Request):
    return templates.TemplateResponse('forw.html', {'request':request})

@app.get("/ajax", response_class=HTMLResponse)
async def ajax(request: Request, e_id:str):
    
    result = "맛있다"
    return templates.TemplateResponse("ajax.html",{"request":request, "result":result})

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
