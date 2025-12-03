import os

from dotenv import load_dotenv
from pyprojroot import here

root = here()
dotenv_path = root / ".env"
load_dotenv(dotenv_path=dotenv_path)

AOC_SESSION = os.getenv("AOC_SESSION")

data_dir = root / "data"
