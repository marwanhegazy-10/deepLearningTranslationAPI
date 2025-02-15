from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel, validator
import tasks

app = FastAPI()

# Due to specific model that we are using these are the languages that are supported
languages = ["English", "French", "German", "Romanian"]

class Translation(BaseModel):
    text: str
    base_lang: str
    final_lang: str


    @validator('base_lang', 'final_lang')
    def valid_lang(cls, lang):
        if lang not in languages:
            raise ValueError("Invalid language")
        return lang


## Route 1:/
## Test if everything is working
## ("message": "Hello world"
@app.get("/")
def get_root():
    return {"message": "Hello world"}

## Route 2: /translate - translate input
## Take in a translation request and store it in the db
## Return a translation id
    ## Not going to do the translation immediately in the request because certain long translations can take a while to process and that can cause the initial web request to time out
@app.post("/translate")
def post_translation(t: Translation, background_tasks: BackgroundTasks):
    # Store the translation
    # Run translation in background
    t_id = tasks.store_translation(t)
    background_tasks.add_task(tasks.run_translation, t_id)
    return {"task_id": t_id}


## Route 3: /results
## Take in a translation id
## Return the translated text
@app.get("/results")
def get_translation(t_id: int):
    return {"translation": tasks.find_translation(t_id)}