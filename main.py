import os
import sys

# add parent directory to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from simplewriting.analysis import markov_generation, clean_text, load_text
from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = "secret-key"

@app.route('/')
def index():
    base_dir = os.path.dirname(__file__)
    file_path = os.path.join(base_dir, "data", "dostoyevsky.txt")

    text = load_text(file_path)
    words = clean_text(text)
    return render_template(
        "index.html",
        generated_text=markov_generation(words, length=10)
    )
    
if __name__ == "__main__":
    app.run(debug=True)