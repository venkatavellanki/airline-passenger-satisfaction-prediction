# ✈️ Airline Passenger Satisfaction Prediction

This project applies **Decision Tree** and **Naive Bayes** machine learning algorithms to predict airline passenger satisfaction.  
It was developed as a **mini-project for the DMA (Data Mining and Analytics) course** during **Semester 7** at **SRM Institute of Science and Technology**.

---

## 📁 Project Structure

airline-passenger-satisfaction-prediction/
├── data/
│ └── Airline_Passenger_Satisfaction.csv
├── src/
│ └── airline_satisfaction.py
├── output/
│ ├── decision_tree_results.txt
│ └── naive_bayes_results.txt
├── docs/
│ ├── DMA_Project_Report.pdf
│ └── DMA_Project_Presentation.pdf
└── README.md

yaml
Copy
Edit

---

## 🧠 Techniques Used

- Data Preprocessing (Null handling, Encoding)
- Feature Selection
- Train-Test Split
- Decision Tree Classifier
- Naive Bayes Classifier
- Evaluation Metrics: Accuracy, Precision, Recall, F1 Score
- Visualization using Matplotlib and Seaborn

---

## 🛠 How to Run

### 🧱 Requirements

- Python 3.8 or higher
- Required Python Libraries:
  - `pandas`
  - `numpy`
  - `scikit-learn`
  - `matplotlib`
  - `seaborn`

Install dependencies using:

```bash
pip install pandas numpy scikit-learn matplotlib seaborn
💻 Run the Program
Open terminal or command prompt

Navigate to the src/ directory:

bash
Copy
Edit
cd src
Run the script:

bash
Copy
Edit
python airline_satisfaction.py
✅ Ensure the dataset file Airline_Passenger_Satisfaction.csv is placed inside the data/ directory.

📊 Sample Results
Decision Tree Classifier:
Accuracy: 95%

F1 Score: 0.95

Naive Bayes Classifier:
Accuracy: 84%

F1 Score: 0.82

🔍 Key Insights
The Decision Tree model outperformed Naive Bayes in this dataset.

Top Features Influencing Satisfaction:

In-flight Service

Seat Comfort

Online Boarding

Departure Delay

📄 Disclaimer
This project was developed by Venkat Aditya Vellanki (RA2111003011799)
as part of Semester 7 DMA coursework at SRM Institute of Science and Technology.

This project is strictly for academic and educational use only.
It is not optimized for commercial or production deployment without further testing, validation, and improvements.

© 2024 **Venkat Aditya Vellanki**. All rights reserved.
