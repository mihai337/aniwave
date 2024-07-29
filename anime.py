import requests
from flask import Flask, Response
from flask_cors import CORS
import urllib3
import asyncio
import json

app = Flask(__name__)
CORS(app)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get_filename(url):
    response = requests.get(url)
    start = response.text.find("<h4>")
    end = response.text.find("</h4>")
    return response.text[start+4:end]

@app.get('/download/<id>')
async def download(id):
    
    url = f"https://www.mp4upload.com/{id}"
   
    headers = {
    "Host": "www.mp4upload.com",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Content-Type": "application/x-www-form-urlencoded",
    "Origin": "https://www.mp4upload.com",
    "Referer": "https://www.mp4upload.com/ngx727ufjvgi",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Te": "trailers",
    }

    # Data payload for the POST request
    data = {
        "op": "download2",
        "id": "ngx727ufjvgi",
        "rand": "",
        "referer": "https://www.mp4upload.com/ngx727ufjvgi",
        "method_free": "Free Download",
        "method_premium": "",
    }

    data["id"] = url.split("/")[-1]
    data["referer"] = url
    headers["Referer"] = url
   
    response = requests.post(url,headers=headers, data=data, stream=True, verify=False)
    headers = {
        "Content-Length": response.headers.get('content-length', 0),
        'Access-Control-Allow-Origin': '*'
    }
    
    return Response(response.iter_content(chunk_size=1024*1024), content_type=response.headers['content-type'], headers=headers)

@app.get("/download/filename/<id>")
async def filename(id):
    url = f'https://www.mp4upload.com/{id}'
    response = {
        "filename": get_filename(url)
    }
    response = json.dumps(response).encode('utf-8')
    return Response(response, content_type="application/json", headers={'Access-Control-Allow-Origin': '*'})

if __name__ == "__main__":
    app.run("0.0.0.0", 5000)

