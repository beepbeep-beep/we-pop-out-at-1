from flask import Flask, request, redirect
from urllib.parse import quote

app = Flask(__name__)

@app.route('/')
def index():
    return '''
      <form method="get">
        <input name="q" placeholder="Search privately" required />
        <button>Go</button>
      </form>
    '''

@app.route('/search')
def search():
    q = request.args.get('q', '')
    return redirect(f"https://html.duckduckgo.com/html/?q={quote(q)}")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
