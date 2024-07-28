from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pathlib import Path

app = FastAPI()

# Подключение статики
app.mount("/css", StaticFiles(directory="css"), name="css")
app.mount("/js", StaticFiles(directory="js"), name="js")
app.mount("/libs", StaticFiles(directory="libs"), name="libs")
app.mount("/mail", StaticFiles(directory="mail"), name="mail")
app.mount("/media", StaticFiles(directory="media"), name="media")
app.mount("/plugins", StaticFiles(directory="plugins"), name="plugins")
app.mount("/fonts", StaticFiles(directory="fonts"), name="fonts")
app.mount("/images", StaticFiles(directory="images"), name="images")


@app.get("/", response_class=HTMLResponse)
async def read_index():
    index_path = Path("index.html")
    return index_path.read_text(encoding="utf-8")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
