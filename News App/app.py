from flask import Flask, render_template, request, session, redirect, url_for
import requests
from datetime import datetime
import math

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # needed for session
API_KEY = "1781c6e459db41b9b808fb6d7ac47231"
PAGE_SIZE = 10

@app.route('/', methods=['GET', 'POST'])
def index():
    query = request.form.get('query') if request.method == 'POST' else request.args.get('query', '')
    page = int(request.args.get('page', 1))
    articles = []
    total_results = 0

    if query:
        url = (
            f"https://newsapi.org/v2/everything?"
            f"q={query}&from=2025-04-24&sortBy=publishedAt&"
            f"pageSize={PAGE_SIZE}&page={page}&apiKey={API_KEY}"
        )
        response = requests.get(url)
        data = response.json()
        articles = data.get("articles", [])
        total_results = data.get("totalResults", 0)

        # Save to search history
        if 'history' not in session:
            session['history'] = []
        if query not in session['history']:
            session['history'].append(query)
            session.modified = True

    total_pages = math.ceil(total_results / PAGE_SIZE)
    return render_template(
        'index.html',
        articles=articles,
        query=query,
        page=page,
        total_pages=total_pages,
        history=session.get('history', [])
    )

@app.route('/clear-history')
def clear_history():
    session.pop('history', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
