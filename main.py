import os

from fastapi import FastAPI

from google.cloud import storage
from google.cloud import vision
from models import Parking
from orm import query_all_parking, insert_parking

app = FastAPI()


os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/your/path/file.json"
storage_client = storage.Client()

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
    blob.download_to_filename(f"/your/download/path/{blob}")
    return {"download": "success"}

@app.get("/vision/{bucket}/{folder}/{file}")
def get_vision(bucket: str, folder: str, file: str):
    image_uri = f"gs://{bucket}/{folder}/{file}"
    client = vision.ImageAnnotatorClient()
    image = vision.Image()
    image.source.image_uri = image_uri
    response = client.text_detection(image=image)
    r = response.text_annotations[0].description
    return {"vision_result": r}

@app.get("/parking")
def query_parking():
    return query_all_parking()

@app.post("/parking")
def create_parking(parking_info: Parking):
    insert_parking(
        parking_info.floor,
        parking_info.zone,
        parking_info.parking_number,
        parking_info.license_plate
    )
    return {"result": "success"}

# run server
# uvicorn main:app --reload --host 0.0.0.0 --port 8000