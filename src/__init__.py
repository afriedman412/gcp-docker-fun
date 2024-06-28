from flask import Flask
import os
from dotenv import load_dotenv


app = Flask(__name__)
load_dotenv()


@app.route('/')
def home() -> str:
    if os.getenv("PASSWORD") == "creamcheese1000":
        return "secret content!"
    return "locked out!"


def f():
    return
