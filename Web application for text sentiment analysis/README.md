# Sentiment Analysis Web Application

## Project Overview
This project is a **Flask web application** that performs sentiment analysis on user-entered text using the **TextBlob** library.  

The app classifies text as **Positive**, **Negative**, or **Neutral** and displays both:  
- **Polarity Score** → Range from `-1` (negative) to `+1` (positive)  
- **Subjectivity Score** → Range from `0` (objective) to `1` (subjective)  

---

## Technologies Used
- **Python**
- **Flask** → Web framework  
- **TextBlob** → Sentiment analysis (NLP)  
- **HTML + CSS** → Frontend (user interface)  

---

## How It Works
1. User enters text in the input box.  
2. The app analyzes the text using **TextBlob**.  
3. Output is displayed:  
   -  Sentiment: Positive / Negative / Neutral  
   -  Polarity score  
   -  Subjectivity score  

---

## User Interface
- A simple, clean **web form**  
- User types a sentence/paragraph  
- App displays:  
  -  **Sentiment (Positive / Negative / Neutral)**  
  -  **Polarity score**  
  -  **Subjectivity score**  

---

## Conclusion
- Built a **user-friendly Flask app** for real-time sentiment analysis.  
- Demonstrates the power of **TextBlob** for quick NLP tasks.  
- Can be extended with advanced models (e.g., Hugging Face Transformers) for **more accurate analysis**.  
