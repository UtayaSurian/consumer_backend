from dotenv import load_dotenv
import os
load_dotenv()

host = os.environ.get('host', 'localhost') # rabbitmq host
storage = os.environ.get('storage', 'local')
queue = os.environ.get('queue', 'myqueue')

