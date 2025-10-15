
import os
from flask import Flask, render_template, request, jsonify, session, redirect, url_for, flash
from flask_wtf import FlaskForm, CSRFProtect
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length
from textblob import TextBlob
from markupsafe import Markup
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import bleach

# -------------------
# Configuration
# -------------------
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key-change-me')
    app.config['WTF_CSRF_ENABLED'] = True
    app.config['MAX_CONTENT_LENGTH'] = 1 * 1024 * 1024  # 1MB safety for form posts

    # Security headers - basic hardening
    @app.after_request
    def set_security_headers(response):
        response.headers['X-Content-Type-Options'] = 'nosniff'
        response.headers['X-Frame-Options'] = 'DENY'
        response.headers['Referrer-Policy'] = 'no-referrer-when-downgrade'
        response.headers['X-XSS-Protection'] = '0'
        csp = (
            "default-src 'self' https://cdn.jsdelivr.net https://cdnjs.cloudflare.com; "
            "script-src 'self' https://cdn.jsdelivr.net https://cdnjs.cloudflare.com; "
            "style-src 'self' 'unsafe-inline' https://cdn.jsdelivr.net https://cdnjs.cloudflare.com; "
            "img-src 'self' data:; "
            "font-src 'self' https://cdn.jsdelivr.net https://cdnjs.cloudflare.com data:"
        )

        response.headers['Content-Security-Policy'] = csp
        return response

    csrf = CSRFProtect(app)

    limiter = Limiter(
        get_remote_address,
        app=app,
        storage_uri="memory://",
        default_limits=["60 per minute"]
    )

    class AnalyzeForm(FlaskForm):
        text = TextAreaField('Enter text to analyze', validators=[
            DataRequired(message="Please enter some text."),
            Length(min=1, max=5000, message="Text must be between 1 and 5000 characters.")
        ])
        submit = SubmitField('Analyze')

    def analyze_text(raw_text: str):
        # Sanitize/normalize input
        cleaned = bleach.clean(raw_text, strip=True)
        blob = TextBlob(cleaned)
        polarity = float(blob.sentiment.polarity)  # -1 to 1
        subjectivity = float(blob.sentiment.subjectivity)  # 0 to 1

        # Classification thresholds
        if polarity > 0.05:
            sentiment = "Positive"
        elif polarity < -0.05:
            sentiment = "Negative"
        else:
            sentiment = "Neutral"

        return {
            "sentiment": sentiment,
            "polarity": polarity,
            "subjectivity": subjectivity,
            "text": cleaned
        }

    @app.route("/", methods=["GET", "POST"])
    @limiter.limit("30/minute")
    def index():
        form = AnalyzeForm()
        result = None
        if form.validate_on_submit():
            data = analyze_text(form.text.data)
            # store last 5 analyses in session (no database)
            history = session.get("history", [])
            history.insert(0, {"text": data["text"][:120]+"..." if len(data["text"])>120 else data["text"],
                               "sentiment": data["sentiment"],
                               "polarity": round(data["polarity"], 3),
                               "subjectivity": round(data["subjectivity"], 3)})
            session["history"] = history[:5]
            result = data
            return render_template("results.html", form=form, result=result)
        elif request.method == "POST":
            # Form errors
            for field, errs in form.errors.items():
                for e in errs:
                    flash(e, "danger")
        return render_template("index.html", form=form, history=session.get("history", []))

    @app.route("/clear", methods=["POST"])
    @limiter.limit("10/minute")
    def clear():
        session.pop("history", None)
        flash("Cleared analysis history.", "info")
        return redirect(url_for('index'))

    @app.route("/api/analyze", methods=["POST"])
    @limiter.limit("60/minute")
    def api_analyze():
        data = request.get_json(silent=True) or {}
        text = data.get("text", "")
        if not isinstance(text, str) or len(text.strip()) == 0:
            return jsonify({"error": "Text is required."}), 400
        if len(text) > 5000:
            return jsonify({"error": "Text too long. Max 5000 characters."}), 400
        result = analyze_text(text)
        return jsonify(result), 200

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)
