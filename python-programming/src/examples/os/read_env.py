import os
import dotenv

dotenv.load_dotenv()
print(os.environ.get('SOME_THING'))
print(os.getenv('SOME_THING'))
