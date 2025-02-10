#DescriptionL Command line interface chat wrap

from argparse import ArgumentParser
from chatwrap.client import LLMClient

LLM_SERVER_URL = 'http://localhost:1234'

def cli(params):
  print(f'Hello: {params.prompt}')
  
  client = LLMClient(LLM_SERVER_URL)
  
  client.send_request(params.prompt)
    
if __name__ == '__main__':
  args = ArgumentParser('Chat Wrap')

  # because it does not have --, it is mendatory
  args.add_argument('prompt', help='prompt to generate text from')
  args.add_argument('--version', action='version', version='%(prog)s 0.1')
  args.add_argument('--model', help='model to use', default='gpt 2')
  args.add_argument('--temperature', type=float, help='temperature for sampling', default=0.7)
  args.add_argument('--streaming', action='store_true', help='streaming mode')

  params = args.parse_args()

  cli(params)