import requests
import time

url = "http://127.0.0.1:8080/verify_cairo_address"

data = {
    'address': 'التجمع الخامس'
}

start_time = time.time()

response = requests.post(url, json=data)

end_time = time.time()
elapsed_time_ms = (end_time - start_time) * 1000  

print("Response:")
print(response.text)
print(f"Time taken: {elapsed_time_ms:.2f} ms")
