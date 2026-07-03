# 🛍️ Customer Segmentation using K-Means Clustering

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-KMeans-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-Deployed-red)
![License](https://img.shields.io/badge/License-MIT-green)

🚀 **Live Demo:** https://customer-segmentation-dhruvbihani.streamlit.app

## 📌 Project Overview

This project focuses on segmenting mall customers into distinct groups based on their purchasing behavior and demographic attributes. The goal is to understand customer patterns and design more effective marketing strategies using data-driven insights.

Using **K-Means Clustering (Unsupervised Machine Learning)**, customers are grouped based on similarities in **Age, Annual Income, and Spending Score**.

---

## 🎯 Objective

To identify meaningful customer segments by analyzing behavioral and demographic data and enabling better business decision-making for targeted marketing.

---

## 📊 Dataset

The dataset contains information about mall customers:

- Customer ID  
- Gender  
- Age  
- Annual Income (k$)  
- Spending Score (1–100)  

---

## ⚙️ Key Features Used for Clustering

- Age  
- Annual Income  
- Spending Score  

---

## 🧠 Methodology

- Data Loading & Inspection  
- Data Cleaning (checked for missing values)  
- Exploratory Data Analysis (EDA)  
- Feature Selection  
- Feature Scaling (if applied)  
- Elbow Method (Optimal K selection)  
- Silhouette Score Evaluation  
- K-Means Clustering  
- Cluster Visualization  
- Cluster Profiling & Interpretation  

---

## 📈 Optimal Number of Clusters

- Determined using **Elbow Method**  
- Validated using **Silhouette Score**  
- Final selected clusters: **5**

---

## 📊 Cluster Insights

| Cluster | Age | Annual Income | Spending Score | Customers |
|----------|------|----------------|------------------|------------|
| 0 | 42.72 | 55.30 | 49.52 | 81 |
| 1 | 32.69 | 86.54 | 82.13 | 39 |
| 2 | 25.27 | 25.73 | 79.36 | 22 |
| 3 | 41.11 | 88.20 | 17.11 | 35 |
| 4 | 45.22 | 26.30 | 20.91 | 23 |

---

## 📌 Key Business Insights

- High income + high spending → premium customers  
- Low income + high spending → impulsive buyers  
- High income + low spending → potential target segment  
- Younger customers show higher engagement  
- Clear and well-separated customer groups exist  

---

## 📦 Tech Stack

- Python  
- Pandas  
- NumPy  
- Matplotlib  
- Seaborn  
- Scikit-learn  
- Jupyter Notebook  

---

## 📁 Project Structure
Customer-Segmentation/
│
├── data/
├── notebooks/
├── images/
├── models/
└── README.md


---

## 🚀 Future Improvements

- Apply DBSCAN and Hierarchical Clustering for comparison  
- Build interactive dashboard using Streamlit / Power BI  
- Deploy clustering model as an API  
- Enable real-time customer segmentation  

---

## 🧠 Skills Demonstrated

- Data Cleaning & Preprocessing  
- Exploratory Data Analysis (EDA)  
- Unsupervised Machine Learning  
- K-Means Clustering  
- Cluster Evaluation Techniques  
- Data Visualization  
- Business Insight Generation  

---

## 👨‍💻 Author

**Dhruv Bihani**  
Aspiring Software Engineer | Machine Learning Enthusiast  

GitHub: https://github.com/yourusername  
LinkedIn: https://www.linkedin.com/in/dhruv-bihani-551611327/
