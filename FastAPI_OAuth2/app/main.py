#app/main
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import uvicorn
from dotenv import load_dotenv
from app.database.connection import Base, engine, get_tables_and_columns, get_users_and_tables
from app.routers import user, auth
from fastapi.templating import Jinja2Templates

load_dotenv()

app = FastAPI(
    debug=True,
    title="Arcadiy"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

templates = Jinja2Templates(directory="templates")

Base.metadata.create_all(bind=engine)

app.include_router(user.router)
app.include_router(auth.router)

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def main(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

@app.get("/register", response_class=HTMLResponse)
async def get_register_form(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

@app.get("/login", response_class=HTMLResponse)
async def get_login_form(request: Request):
    return templates.TemplateResponse("entrance.html", {"request": request})


if __name__ == '__main__':
    # get_tables_and_columns()
    get_users_and_tables()
    uvicorn.run(app='main:app', reload=True)
