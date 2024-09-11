import requests
import json

url = 'http://localhost:11434/api/generate'
myobj = {
   "model": "tinyllama",
   "prompt":"why is the sky is blue",
   "stream":False
}
x = requests.post(url, json = myobj)

print(x["response"])


