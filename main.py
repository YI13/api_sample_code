import os
from fastapi import FastAPI
from google.cloud import storage
from google.cloud import vision
from sql import insert_data

app = FastAPI()


os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/your/path/file.json"
project_id = "your-project-123456789"
storage_client = storage.Client()
bucket_name = "parking_image"

@app.get("/")
def hellp_world():
    return {"Hello": "World"}

@app.get("/buckets/{bucket}/blobs")
def list_blobs_by_bucket(bucket):
    """Lists all the blobs in the bucket."""
    blobs = storage_client.list_blobs(bucket)
    return [blob.name for blob in blobs]

@app.get("/buckets/{bucket}/{blob}")
def download_blob_from_bucket(bucket, blob):
    bucket = storage_client.get_bucket(bucket)
    blob = bucket.blob(blob)
    blob.download_to_filename(f"/your_path/{blob}")
    return {"download": "success"}

@app.get("/vision/{bucket}/{file}")
def get_vision(bucket: str, file: str):
    image_uri = f"gs://{bucket}/{file}"
    client = vision.ImageAnnotatorClient()
    image = vision.Image()
    image.source.image_uri = image_uri
    response = client.text_detection(image=image)
    r = response.text_annotations[0].description
    return {"vision_result": r}

# test
@app.post("/insert_db")
def set_db():
    insert_data("car1", "test")