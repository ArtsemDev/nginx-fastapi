from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.requests import Request
from uvicorn.middleware.proxy_headers import ProxyHeadersMiddleware

templating = Jinja2Templates(directory="templates")
static = StaticFiles(directory="static")

app = FastAPI()
app.mount(path="/static", app=static, name="static")
app.add_middleware(
    middleware_class=ProxyHeadersMiddleware,
    trusted_hosts=("*", )
)


@app.get("/")
async def index(request: Request):
    return templating.TemplateResponse(
        name="index.html",
        context={
            "request": request
        }
    )
