# Basic Data Analysis on Iris Dataset  

## Project Overview  

This project demonstrates **basic data analysis and visualization techniques** using the famous **Iris dataset**.  
The goal is to explore the dataset, calculate key statistics, and generate insights through **visualizations**.  

The project covers:  
- Loading and exploring the dataset  
- Descriptive statistics  
- Basic analysis (mean, group-wise analysis)  
- Data visualizations (bar charts, scatter plots, heatmaps)  
- Generating insights from results  

---

## Dataset  

- **Name:** Iris Dataset  
- **File:** `IRIS.csv`  

**Features:**  
- `sepal_length`  
- `sepal_width`  
- `petal_length`  
- `petal_width`  
- `species` *(Setosa, Versicolor, Virginica)*  

---

## Technologies Used  

- **Python**  
- **Pandas** → Data manipulation & analysis  
- **Matplotlib & Seaborn** → Visualizations  

---

## Steps Performed  

###  1. Data Exploration  
- Displayed first 5 rows  
- Checked dataset info, shape, column names, and data types  
- Checked for missing values  

###  2. Descriptive Statistics  
- Generated summary statistics  
- Count of species distribution  

###  3. Basic Data Analysis  
- Calculated **average sepal length**  
- Grouped by species → average sepal length for each species  

###  4. Visualizations  
- **Bar Chart** → Average sepal length by species  
- **Scatter Plot** → Sepal length vs sepal width  
- **Heatmap** → Correlation between numerical features  

---

## Visualizations  

### Average Sepal Length by Species  
Bar chart showing average values grouped by species.  

### Sepal Length vs Sepal Width  
Scatter plot showing correlation between two key features.  

### Correlation Heatmap  
Heatmap highlighting strong correlations between **petal length** and **petal width**.  

---

## Insights  

1. Average sepal length is around **5.84**.  
2. **Virginica species** has the largest average sepal length.  
3. Scatter plot shows a **positive correlation** between sepal length and sepal width.  
4. Heatmap indicates a **strong correlation** between petal length and petal width.  

---

## Conclusion  

This project demonstrates how **basic data analysis** can uncover meaningful patterns in a dataset using Python libraries.  
The Iris dataset, though simple, highlights the importance of **EDA (Exploratory Data Analysis)** in understanding data before applying advanced techniques.  
