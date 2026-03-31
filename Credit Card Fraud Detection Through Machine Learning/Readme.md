# Credit Card Fraud Detection

Welcome to the **Credit Card Fraud Detection** project — a machine learning initiative designed to accurately identify fraudulent credit card transactions. This project focuses on data preprocessing, visualization, handling severe class imbalance, and training effective ML models.

---

## 📘 Project Overview

Credit card fraud is a major challenge in financial security. Since fraudulent transactions are extremely rare compared to legitimate ones, the dataset is **highly imbalanced**. This project demonstrates:

* Understanding and preparing the dataset
* Applying resampling techniques to fix imbalance
* Training multiple ML models
* Evaluating with metrics suited for imbalanced classification

---

## 🔧 Key Features

### **1. Data Preprocessing**

* Handling missing values
* Feature scaling (standardization / normalization)
* Feature selection for improved model performance

### **2. Exploratory Data Analysis (EDA)**

* Class distribution visualization
* Correlation between features
* Trend and pattern analysis using Seaborn & Matplotlib

### **3. Handling Imbalanced Data**

* **Random undersampling**
* **Class weight adjustments** in ML algorithms

### **4. Machine Learning Models Implemented**

* Logistic Regression


### **5. Evaluation Metrics**

Because accuracy is misleading for imbalanced data, we emphasize:

* Precision & Recall
* F1-score
* Confusion Matrix
* ROC-AUC score

---

## 🎥 Reference Video

Here is a helpful video explaining credit card fraud detection using machine learning:

🔗 **[https://youtu.be/vDH9xqDkQ58](https://youtu.be/vDH9xqDkQ58)**

---

## 🛠️ Technologies Used

* **Python**
* **NumPy & Pandas** (data handling)
* **Matplotlib & Seaborn** (visualization)
* **Scikit-Learn** (ML modeling)
* **Imbalanced-learn** (resampling)

---

## 🚀 How to Run This Project

1. Clone the repository:

   ```bash
   git clone https://github.com/Jaidhuria/Credit Card Fraud Detection
   ```
2. Install required packages:

   ```bash
   pip install -r requirements.txt
   ```
3. Open Jupyter Notebook:

   ```bash
   jupyter notebook
   ```
4. Run the notebooks step-by-step for preprocessing, model training, and evaluation.

---

## 📊✨ Results Summary

Below are the model performance metrics obtained during testing:

### **📄 Classification Report**

```
precision    recall  f1-score   support

0       1.00      0.95      0.97   1906322
1       0.02      0.95      0.04      2464

accuracy                           0.95   1908786
macro avg      0.51      0.95      0.51   1908786
weighted avg   1.00      0.95      0.97   1908786
```

### **🧮 Confusion Matrix**

```
[[1805158  101164]
 [     129    2335]]
```

### **📈 Model Accuracy**

```
94.69%
```


## 🌟 Future Enhancements 🚀

* Implement deep learning (Autoencoders, Neural Networks)
* Deploy model using Flask/FastAPI
* Add real-time fraud detection pipeline
* Build an interactive dashboard for visualization

---

## ✨ Project Goal

This project aims to develop a robust fraud detection system that minimizes false negatives and strengthens financial security through machine learning.

Feel free to explore, contribute, or suggest improvements!
