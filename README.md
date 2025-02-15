# Deep Learning Translation API

This repository contains a Deep Learning Translation API built using FastAPI. The API allows for translation requests between supported languages, leveraging a pre-trained T5 model from the Hugging Face library. The translations are processed asynchronously to handle long translation requests efficiently.

## Supported Languages

- English
- French
- German
- Romanian

## Endpoints

### 1. Root Endpoint

**Route:** `/`  
**Method:** `GET`  
**Description:** Test if the API is working.  
**Response:**
```json
{
  "message": "Hello world"
}
```

### 2. Translate Endpoint

**Route:** `/translate`  
**Method:** `POST`  
**Description:** Submit a translation request. The translation is processed asynchronously.  
**Request Body:**
```json
{
  "text": "Your text here",
  "base_lang": "English",
  "final_lang": "French"
}
```
**Response:**
```json
{
  "task_id": 1
}
```

### 3. Results Endpoint

**Route:** `/results`  
**Method:** `GET`  
**Description:** Retrieve the result of a translation request using the `task_id`.  
**Query Parameters:**
- `t_id`: The ID of the translation task.

**Response:**
```json
{
  "translation": "Votre texte ici"
}
```

## Technologies Used

- [FastAPI](https://fastapi.tiangolo.com/)
- [Peewee ORM](http://docs.peewee-orm.com/en/latest/)
- [Hugging Face Transformers](https://huggingface.co/transformers/)
- [T5 Model](https://huggingface.co/t5-small)
- [Uvicorn](https://www.uvicorn.org/)
- [PyTorch](https://pytorch.org/)

## Project Structure

- `main.py`: Defines the FastAPI application and routes.
- `models.py`: Defines the database models using Peewee ORM.
- `tasks.py`: Contains background tasks for storing, running, and retrieving translations.
- `requirements.txt`: Lists the dependencies required to run the project.

## Setup and Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/marwanhegazy-10/deep-learning-translation-api.git
   cd deep-learning-translation-api
   ```

2. Create a virtual environment and activate it:
   ```sh
   python3 -m venv venv
   source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
   ```

3. Install the dependencies:
   ```sh
   pip install -r requirements.txt
   ```

4. Run the FastAPI application:
   ```sh
   uvicorn main:app --reload
   ```

## Usage

1. Start the FastAPI server by running the command mentioned above.
2. Access the API documentation at `http://127.0.0.1:8000/docs` for interactive API exploration.

## Acknowledgements

This project was developed with guidance and resources from [Dataquest](https://www.dataquest.io/).
