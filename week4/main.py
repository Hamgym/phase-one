from fastapi import FastAPI, Request
app = FastAPI()

from starlette.middleware.sessions import SessionMiddleware
app.add_middleware(SessionMiddleware, secret_key="meme")

from fastapi.staticfiles import StaticFiles
app.mount("/static", StaticFiles(directory="static"), name="static_files")

from fastapi.templating import Jinja2Templates
templates = Jinja2Templates(directory="templates")


from fastapi.responses import HTMLResponse, RedirectResponse
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request, name="index.html"
    )

from fastapi import Form
@app.post("/signin")
async def signin(request: Request, username: str = Form(), password: str = Form()):
    if username=="" or password=="":
        return RedirectResponse("/error?message=請輸入使用者名稱及密碼", status_code=303)
    elif username=="test" and password=="test":        
        request.session["SIGNED-IN"] = "TRUE"
        return RedirectResponse("/member", status_code=303)
    else:
        return RedirectResponse("/error?message=帳號、或密碼輸入錯誤", status_code=303)

@app.get("/error", response_class=HTMLResponse)
async def error(request: Request, message: str):
    return templates.TemplateResponse(
        request=request, name="error.html", context={"message":message}
    )

@app.get("/member", response_class=HTMLResponse)
async def member(request: Request):    
    signed = request.session.get("SIGNED-IN", "FALSE")
    if signed == "TRUE":        
        return templates.TemplateResponse(
            request=request, name="member.html"
        )
    else:
        return RedirectResponse("/")

@app.get("/signout")
async def signout(request: Request):    
    request.session["SIGNED-IN"] = "FALSE"
    return RedirectResponse("/")

@app.get("/square/{num}", response_class=HTMLResponse)
async def square(request: Request, num: int):
    result = num**2
    return templates.TemplateResponse(
            request=request, name="square.html", context={"result": result}
    )