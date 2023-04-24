from dotenv import load_dotenv
import os
load_dotenv()

host = os.environ.get('host', 'localhost') # rabbitmq host
port = os.environ.get('port', '5672')
storage = os.environ.get('storage', 'local')
queue = os.environ.get('queue', 'myqueue')

