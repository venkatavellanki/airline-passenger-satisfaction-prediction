# ✈️ Airline Passenger Satisfaction Prediction

This project focuses on predicting airline passenger satisfaction using machine learning techniques such as **Decision Tree** and **Naive Bayes** classifiers.  
It was developed as part of the **Data Mining and Analytics (DMA)** coursework during **Semester 7** at **SRM Institute of Science and Technology**.

The project explores factors that influence passenger satisfaction and attempts to classify whether a passenger is "Satisfied" or "Dissatisfied" based on input features.

---

## 🧠 Project Highlights

- 📊 Exploratory Data Analysis (EDA)
- 🧼 Data Preprocessing (null values, encoding)
- 🔍 Feature Selection & Engineering
- 🌲 Decision Tree Classification
- 📈 Naive Bayes Classification
- 📉 Evaluation: Accuracy, Precision, Recall, F1-Score
- 📊 Data Visualization using **Matplotlib** and **Seaborn**

---

## 📁 Project Structure


```
airline-passenger-satisfaction-prediction/
├── data/
│   └── Airline_Passenger_Satisfaction.csv
├── src/
│   └── Airline_Passenger_Satisfaction.py
├── output/
│   ├── decision_tree_results.txt
│   └── naive_bayes_results.txt
├── docs/
│   ├── Airline_Passenger_Satisfaction__Report.pdf
│   ├── Airline_Passenger_Satisfaction_Presentation.pdf
│   └── Airline_Passenger_Satisfaction_Colab.ipynb
└── README.md
```

---


## 🧠 Techniques Used

- Data Preprocessing (Null handling, Encoding)

- Feature Selection

- Train-Test Split

- Decision Tree Classifier

- Naive Bayes Classifier

- Evaluation Metrics: Accuracy, Precision, Recall, F1 Score

- Visualisation using Matplotlib and Seaborn


---

## 🛠 How to Run the Project

### 🧱 Requirements

- Python 3.8 or higher  
- Required Python Libraries:
  - `pandas`
  - `numpy`
  - `scikit-learn`
  - `matplotlib`
  - `seaborn`

### 📦 Install Dependencies

```bash
pip install pandas numpy scikit-learn matplotlib seaborn
```

### 💻 Steps to Execute

1. **Navigate to the project directory:**

```bash
cd src
```

2. **Run the main script:**

```bash
python airline_satisfaction.py
```

> ✅ Make sure the file `Airline_Passenger_Satisfaction.csv` is placed in the `data/` folder before executing the script.

3. **Check the results** in the `output/` directory for performance metrics of both classifiers.

---

## 📊 Sample Results

### 🔹 Decision Tree Classifier

- Accuracy: **95%**  
- F1 Score: **0.95**

### 🔸 Naive Bayes Classifier

- Accuracy: **84%**  
- F1 Score: **0.82**

---

## 🔍 Key Observations

- The **Decision Tree** model consistently outperforms Naive Bayes across all evaluation metrics.
- Top features influencing customer satisfaction include:
  - **In-flight Service**
  - **Seat Comfort**
  - **Online Boarding**
  - **Departure Delay**

---

## 📄 Disclaimer

This project was developed by **Venkat Aditya Vellanki (RA2111003011799)** for the **DMA** course in **Semester 7** at **SRM Institute of Science and Technology**.

The repository and its contents are meant strictly for **academic and educational** purposes.  
The code, models, and dataset are not optimized for production-level deployment and require further validation.

© 2024 **Venkat Aditya Vellanki**. All rights reserved.

---
