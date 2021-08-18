from Queen_Bot import main as run
from dotenv import load_dotenv
import os
load_dotenv()
if __name__ == '__main__':
    run(os.getenv("use_token"))