import requests

# URL of the POST request
url = input("Enter the URL of the episode: ")
#"https://www.mp4upload.com/ngx727ufjvgi"

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

# Make the POST request
response = requests.post(url,headers=headers, data=data, stream=True, verify=False)

# Print the response
print(response.status_code)

file_path = "downloaded_file.mp4"
total_size = int(response.headers.get('content-length', 0))
downlaoed_size = 0
print(f"File size: {total_size / 1024 / 1024:.2f} MB")

with open(file_path, 'wb') as file:
    for chunk in response.iter_content(chunk_size=1024*1024):
        if chunk:
            file.write(chunk)
            downlaoed_size += len(chunk)
            print(f"Downloaded {downlaoed_size / total_size * 100:.2f}%", flush=True, end='\r')


print(f"File downloaded and saved as {file_path}")
