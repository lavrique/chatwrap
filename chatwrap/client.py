#description: Client class for Chat wrap
# Sends requests ro the LLM server/API

import requests

class LLMClient:
  '''
  text
  connect to LLM server
  send request to LLM server and return response
  '''

  def __init__(self, url):
    self.url = url
    
    print (f'Connecting to llm server at: {url}')
    
    response = requests.get(f'{self.url}/v1/models')
    if response.status_code == 200:
      print('Connected to LLM server')
      
      models = response.json()
      
      print(f'Availeable models: {models}')
      
  def send_request(self, prompt, model= "hermes-3-llama-3.2-3b", temperature=0.7, stream=False):
    body = {
      "prompt": prompt,
      "model": model,
      "messages": [ 
        { "role": "system", "content": "Always answer in rhymes." },
        { "role": "user", "content": prompt }
      ], 
      "temperature": temperature, 
      "max_tokens": 1000,
      "stream": stream
    }
    
    headers = {
      'Content-type': "application/json"
    }
    response = requests.post(f'{self.url}/v1/chat/completions', json=body, headers=headers)
    
    if response.status_code == 200:
        print(f'Response: {response.json()}')
    else:
      print (f'error, {response.json()}')
    
  
    
