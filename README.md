
# SentimentLab — Real-time Sentiment Analysis (Flask + TextBlob)

A professional, production-ready starter for sentiment analysis on user-provided text.
It uses **TextBlob** to compute **Sentiment (Positive/Negative/Neutral)** along with **Polarity** and **Subjectivity** scores.

## Features
- Clean, responsive UI (Bootstrap 5)
- Real-time analysis (no DB)
- Input validation (1–5000 chars) & sanitization (bleach)
- CSRF protection (Flask-WTF)
- Color-coded results + progress bars
- Optional gauges (Chart.js)
- Simple session-based recent history (last 5)
- REST API: `POST /api/analyze` (JSON: `{ "text": "..." }`)
- Basic rate limiting with Flask-Limiter
- Docker & Heroku-friendly (Gunicorn)

## Quickstart

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python -m textblob.download_corpora  # one-time for TextBlob
export FLASK_APP=app.py  # Windows PowerShell: $Env:FLASK_APP="app.py"
export FLASK_ENV=development
flask run
```

Then open http://127.0.0.1:5000/

### API Example
```bash
curl -X POST http://127.0.0.1:5000/api/analyze -H "Content-Type: application/json" -d "{\"text\": \"I love this!\\"}"
```

## Configuration
- `SECRET_KEY` (env var) for sessions/CSRF.
- Rate limiting defaults to `60/minute` globally; endpoints have explicit limits too.

## Testing
```bash
pytest -q
```

## Deployment
Use Gunicorn in production:
```bash
gunicorn -w 2 -b 0.0.0.0:5000 app:create_app()
```

### Docker (optional)
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt && python -m textblob.download_corpora
ENV PORT=5000
CMD ["gunicorn", "-w", "2", "-b", "0.0.0.0:5000", "app:create_app()"]
```

## Notes
- **Polarity thresholds**: > 0.05 positive, < -0.05 negative, else neutral.
- No database is used. For history persistence, add a DB or cache.
- Avoid exposing `SECRET_KEY` publicly.
