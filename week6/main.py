from fastapi import FastAPI, Request, Form
app = FastAPI()

from starlette.middleware.sessions import SessionMiddleware
app.add_middleware(SessionMiddleware, secret_key="meme")

from fastapi.staticfiles import StaticFiles
app.mount("/static", StaticFiles(directory="static"), name="static_files")

from fastapi.templating import Jinja2Templates
templates = Jinja2Templates(directory="templates")

# Don’t push code including your daily password
import mysql.connector
mydb = mysql.connector.connect(
    user = "",
    password = "",
    host = "localhost",
    database = "website"
)
cursor = mydb.cursor()


from fastapi.responses import HTMLResponse, RedirectResponse
@app.get("/", response_class=HTMLResponse)
async def home(request:Request):
    return templates.TemplateResponse(
        request=request, name="index.html"
    )

@app.post("/signup")
async def signup(request:Request, name:str=Form(), username:str=Form(), password:str=Form()):
    cursor.execute(f"SELECT * FROM member WHERE username='{username}'")
    row = cursor.fetchone()
    if row != None:
        return RedirectResponse("/error?message=使用者名稱重複", status_code=303)
    else:
        cursor.execute(
            f"INSERT INTO member(name, username, password) VALUES('{name}', '{username}', '{password}')"
        )
        mydb.commit()
        return RedirectResponse("/", status_code=303)

@app.get("/error", response_class=HTMLResponse)
async def error(request:Request, message:str):
    return templates.TemplateResponse(
        request=request, name="error.html", context={"message":message}
    )

@app.post("/signin")
async def signin(request:Request, username:str=Form(), password:str=Form()):
    cursor.execute(f"SELECT * FROM member WHERE username='{username}' AND password='{password}'")
    row = cursor.fetchone()
    if row != None:
        request.session["SIGNED-IN"] = "TRUE"
        request.session["member_id"] = row[0]
        request.session["name"] = row[1]
        request.session["username"] = row[2]
        return RedirectResponse("/member", status_code=303)
    else:
        return RedirectResponse("/error?message=帳號或密碼輸入錯誤", status_code=303)

@app.get("/member", response_class=HTMLResponse)
async def member(request:Request):
    signed = request.session.get("SIGNED-IN", "FALSE")
    if signed == "TRUE":
        name = request.session.get("name", None)
        member_id = request.session.get("member_id", None)
        cursor.execute("SELECT member.name, message.content, member.id, message.id FROM member JOIN message ON member.id=message.member_id ORDER BY message.id")
        message = cursor.fetchall()
        return templates.TemplateResponse(
            request=request, name="member.html", context={"member_id": member_id, "name": name, "message": message}
        )
    else:
        return RedirectResponse("/")

@app.get("/signout")
async def signout(request:Request):
    request.session.clear()
    return RedirectResponse("/")

@app.post("/createMessage")
async def createMessage(request:Request, message:str=Form()):
    member_id = request.session.get("member_id", None)
    cursor.execute(f"INSERT INTO message(member_id, content) VALUES({member_id}, '{message}')")
    mydb.commit()
    return RedirectResponse("/member", status_code=303)

@app.post("/deleteMessage")
async def deleteMessage(request:Request, message_id:str=Form()):
    member_id = request.session.get("member_id", None)
    cursor.execute(f"SELECT * FROM message WHERE id={message_id} AND member_id={member_id}")
    row = cursor.fetchone()
    if row:
        cursor.execute(f"DELETE FROM message WHERE id={message_id}")
        mydb.commit()
        return RedirectResponse("/member", status_code=303)
    else:
        request.session.clear()
        return RedirectResponse("/", status_code=303)