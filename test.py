from fastapi import FastAPI
import requests

app = FastAPI()
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow requests from any origin (replace with your frontend URL in production)
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

# Replace 'file_path' with the path to the file you want to upload
file_path = './test.cbl'
files = {'file': open(file_path, 'rb')}

# Replace 'http://your_api_url_here/generate_code' with the actual URL of your FastAPI server endpoint
url = 'https://needfit-legacy-codeconverter.onrender.com/generate_code'


@app.get("/generate")
def generate():
    response = requests.post(url, files=files)

    if response.status_code == 200:
        # Do something with the response
        with open('generated_code.py', 'wb') as f:
            f.write(response.content)
        print('File saved as generated_code.py')
    else:
        print('Error:', response.status_code)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
