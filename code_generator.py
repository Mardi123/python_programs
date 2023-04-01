import requests
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("prompt", help="prompt to send to chat-gpt")
parser.add_argument("file_name", help="filename of the output program")
args = parser.parse_args()

open_ai_url_end_point = "https://api.openai.com/v1/completions"
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " +  OPENAI_API_KEY
}

request_data = {
    
    "model": "text-davinci-003", #model used for training
    "prompt": f"Write a Python code for {args.prompt} , only code no text", #prompt to be sent to api
    "max_tokens": 100, #size of output
    "temperature": 0   #creativity
  
}

response = requests.post(open_ai_url_end_point, headers=headers, json=request_data)

if response.status_code == 200:
    with open(args.file_name, 'w') as fgpt:
        fgpt.write(response.json()["choices"][0]["text"])
else:
    print(f"Request failed with status code {response.status_code}")
