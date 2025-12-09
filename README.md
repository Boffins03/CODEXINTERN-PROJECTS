# Internship Projects — Data Analysis, Machine Learning, and NLP  

This repository contains the three major projects completed during my one-month internship.  
The projects cover:

- Exploratory Data Analysis (EDA)
- Machine Learning (Regression using Neural Networks)
- Natural Language Processing (Sentiment Analysis)
- Basic full-stack development using Flask

Each folder represents one complete project.

---

## Project Overview

### Project-1 — Basic Data Analysis on Iris Dataset  
A complete exploratory data analysis workflow using the Iris dataset.

**Key Highlights:**
- Dataset exploration (head, shape, info, missing values)
- Statistical summaries
- Group-wise comparisons
- Visualizations:
  - Bar charts  
  - Scatter plots  
  - Correlation heatmap
- Insights on feature relationships
- Summary and conclusions

**Folder:** `Project-1/`  
Includes the Python notebook, dataset, and generated plots.

---

### Project-2 — House Price Prediction using Neural Networks  
A machine learning project comparing two TensorFlow/Keras regression models:

| Model | Description | Performance |
|-------|-------------|-------------|
| Model 1 | No activation functions (linear hidden layers) | Best performance |
| Model 2 | ReLU activation in hidden layers | High error; underperforms |

**Key Highlights:**
- Preprocessing (scaling, train/test split)
- Building and training two neural networks
- Visualizing predicted vs actual prices
- Understanding why the linear model outperformed the non-linear model
- Observations on data behavior and model selection

**Folder:** `Project-2/`  
Includes the dataset, model notebook, and result visualizations.

---

### Project-3 — SentimentLab (Real-Time Sentiment Analysis App)  
A Flask web application for real-time sentiment analysis using TextBlob.

**Key Highlights:**
- Clean UI built with Bootstrap 5
- Real-time polarity and subjectivity scoring
- REST API: `POST /api/analyze`
- Input validation and sanitization
- CSRF protection (Flask-WTF)
- Basic rate limiting (Flask-Limiter)
- Optional charts (Chart.js)
- Dockerfile and Gunicorn setup for deployment

**Folder:** `Project-3/`  
Includes the Flask application, templates, requirements, and Dockerfile.

---

## Technologies Used

**Programming & ML Libraries**
- Python  
- Pandas, NumPy  
- Matplotlib, Seaborn  
- TensorFlow / Keras  
- Scikit-Learn  
- TextBlob  

**Web and Deployment**
- Flask  
- Jinja2  
- Bootstrap 5  
- Flask-WTF  
- Flask-Limiter  
- Gunicorn  
- Docker (optional)

---

## Learning Outcomes

Throughout these projects, I gained experience in:

- Exploratory data analysis and visualization  
- Statistical understanding of datasets  
- Neural network design and evaluation  
- Linear vs non-linear model behavior  
- Building and structuring a Flask application  
- Creating REST APIs  
- Managing user input securely  
- Preparing ML/NLP applications for deployment  

---

## Repository Structure

```

/Internship-Projects/
│
├── Project-1/      # Iris Dataset EDA
│   ├── IRIS.csv
│   ├── analysis.ipynb
│   └── plots/
│
├── Project-2/      # House Price Prediction (Neural Networks)
│   ├── house_price_dataset.csv
│   ├── model_notebook.ipynb
│   └── results/
│
├── Project-3/      # SentimentLab (Flask App)
│   ├── app.py
│   ├── templates/
│   ├── static/
│   ├── Dockerfile
│   └── requirements.txt
│
└── README.md    # (This file)

````

---

## How to Run Any Project

Each project has its own setup instructions inside its folder.  
General setup:

```bash
cd Task-X
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
````

---

## Contact

Feel free to reach out at "mdhuzaifachauhan@gmail.com" for collaboration, feedback, or discussions about these projects.


Just tell me!
```
