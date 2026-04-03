from simplewriting.analysis import markov_generation
from simplewriting.analysis import clean_text
from simplewriting.analysis import load_text

@app.route('/')
def analyze():
    text = load_text(data/dostoevsky.txt)
    words = clean_text(text)
    return render_template(
        "index.html",
        generated_text=markov_generation(words, length=10)
    )