from dotenv import load_dotenv
import os
load_dotenv()

host = os.environ.get('host', 'localhost') # rabbitmq server's hostname
port = os.environ.get('port', '5672') # rabbitmq server's port
storage = os.environ.get('storage', 'local') # to store locally
queue = os.environ.get('queue', 'basic_queue') # queue name

