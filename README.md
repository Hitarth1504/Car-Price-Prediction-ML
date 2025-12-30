# 🚗 Car Price Prediction using Machine Learning

This project predicts the selling price of a used car based on features such as **kilometers driven** and **manufacturing year** using Machine Learning techniques in Python.

The project follows a complete ML pipeline including:
- Data cleaning
- Encoding
- Feature scaling
- Dataset merging
- Model training and evaluation

---

## 📂 Project Structure

Car-Price-Prediction-ML/
│
├── dataset.csv # Original dataset
├── clean_data.py # Data cleaning script
├── encoding_data.py # Encoding categorical features
├── scaldata.csv # Scaled data
├── marge.py # Merge cleaned & scaled data
├── final.csv # Final dataset for training
├── spliting.py # Train-test split & model training
└── README.md # Project documentation



---

## 🧠 Machine Learning Models Used

- **Linear Regression**
- **Random Forest Regressor**

---

## ⚙️ Technologies & Libraries

- Python
- Pandas
- NumPy
- Scikit-learn

---

## 📊 Features Used

- `kmdriven`
- `year`

**Target Variable**
- `sellingprice`

---

## 🚀 How to Run the Project

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/Car-Price-Prediction-ML.git
cd Car-Price-Prediction-ML

2️⃣Install Dependencies
pip install pandas scikit-learn

3️⃣ Run the Scripts (in order)
python clean_data.py
python encoding_data.py
python marge.py
python spliting.py
