



from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates #Loads HTML files from templates folder.

from app.translator import translate_text
from app.language_detector import detect_language

app = FastAPI()

# Static folder
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates folder
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )


@app.get("/translate")
async def translate(text: str, target_language: str):

    source_language = detect_language(text)

    translated = translate_text(
        text,
        source_language,
        target_language
    )

    return {
        "translated_text": translated
    }
    
    
# I developed a real-time translation backend using FastAPI. 
# The application serves frontend templates using Jinja2 and 
# static assets using StaticFiles. The /translate API receives 
# user text and target language as query parameters. 
# The system first detects the source language dynamically, 
# then passes the text through a transformer-based translation pipeline. 
# Finally, the translated output is returned as a JSON response and 
# rendered on the frontend asynchronously using JavaScript fetch requests