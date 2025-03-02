import requests

url = "http://127.0.0.1:1234/v1/chat/completions"
headers = {"Content-Type": "application/json"}
data = {
    "model": "deepseek-r1-distill-qwen-7b",
    "messages": [{"role": "user", "content": "Hello!"}]
}

response = requests.post(url, json=data, headers=headers)
print(response.json()["usage"])  # Shows prompt_tokens, completion_tokens, and total_tokens
