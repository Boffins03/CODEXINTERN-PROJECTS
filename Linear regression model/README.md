# House Price Prediction using Neural Networks  

## Project Overview  

This project builds and compares **two regression models using TensorFlow/Keras** to predict **house prices** based on multiple features.  
The objective is to evaluate whether adding **activation functions (non-linear transformations)** improves model performance.  

The models are trained on a **House Price dataset**, and their performances are compared using **Mean Absolute Error (MAE)** and **Mean Squared Error (MSE)**.  

---

## Dataset  

- **File:** `house_price_dataset.csv`  

**Features (X):**  
- `Square_Footage`  
- `Num_Bedrooms`  
- `Num_Bathrooms`  
- `Year_Built`  
- `Lot_Size`  
- `Garage_Size`  
- `Neighborhood_Quality`  

**Target (Y):**  
- `House_Price`  

---

## Technologies Used  

- **Python**  
- **TensorFlow/Keras** → Neural network models  
- **Scikit-learn** → Data preprocessing, evaluation metrics  
- **Matplotlib & Seaborn** → Visualizations  

---

## Steps Performed  

### 1. Data Preprocessing  
- Checked missing values & summary statistics  
- Standardized input features using **StandardScaler**  
- Split dataset into **training (80%)** and **test (20%)** sets  

### 2. Model Development  

#### Model 1 (Without Activation Functions)  
- Layers: `Dense(100)` → `Dense(50)` → `Dense(10)` → `Dense(1)`  
- No activation functions in hidden layers  
- **Loss function:** Mean Absolute Error (MAE)  
- **Optimizer:** Adam  

#### Model 2 (With ReLU Activations)  
- Layers: `Dense(100, ReLU)` → `Dense(50, ReLU)` → `Dense(10, ReLU)` → `Dense(1)`  
- Hidden layers include **ReLU activations**  
- Same loss & optimizer as Model 1  

### 3. Model Evaluation  

**Evaluation metrics:**  
- MAE (Mean Absolute Error)  
- MSE (Mean Squared Error)  

---

## Visualizations  

### Predicted vs Actual Prices  
- Scatter plot comparing **actual house prices** vs **predicted values**  
- Red dashed line shows the ideal **perfect prediction (y=x)**  

### Training & Validation Loss Curves  
- Loss curves plotted across epochs for both models  

---

## Results  

| Model   | MAE       | MSE        |  
|---------|-----------|------------|  
| Model 1 | ~9,058    | ~1.21e+08  |  
| Model 2 | ~513,074  | ~3.31e+11  |  

---

## Observations  

- **Model 1 (without activation)** performs much better with low error (**MAE ~9k**).  
- **Model 2 (with ReLU activations)** significantly underperforms, producing **very high errors**.  
- Since house price prediction is often **linear in nature**, the simple linear model fits the data better.  
- Adding non-linear activations (ReLU) **worsened performance** in this case because the dataset likely follows a **linear relationship** between features and price.  

---

## Conclusion  

- **Best Model:** Model 1 (No activation functions)  
- This demonstrates that **simpler models can outperform deeper ones** when the underlying data relationship is mostly linear.  

