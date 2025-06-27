import os
import urllib.request
import zipfile

MODEL_URL = "https://alphacephei.com/vosk/models/vosk-model-small-en-us-0.15.zip"
MODEL_ZIP = "vosk-model.zip"
MODEL_FOLDER = "vosk-model-small-en-us-0.15"

def download_model():
    if os.path.exists(MODEL_FOLDER):
        print(f"[INFO] Model folder '{MODEL_FOLDER}' already exists. Skipping download.")
        return

    print(f"[INFO] Downloading model from {MODEL_URL}...")
    urllib.request.urlretrieve(MODEL_URL, MODEL_ZIP)
    print("[INFO] Download complete.")

    print("[INFO] Extracting model...")
    with zipfile.ZipFile(MODEL_ZIP, 'r') as zip_ref:
        zip_ref.extractall()
    os.remove(MODEL_ZIP)
    print(f"[INFO] Model extracted to '{MODEL_FOLDER}' and zip deleted.")

if __name__ == "__main__":
    download_model()
