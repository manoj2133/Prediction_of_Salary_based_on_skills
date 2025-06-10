
# 💼 Prediction of Salary Based on Skills

## 📌 Objective
This project aims to predict the **salary** of professionals based on their **skills** and other job-related features. By leveraging regression models and real-world job market data, the goal is to understand which skills are most influential and build a robust salary prediction system.

## 📊 Dataset
The dataset contains features such as:
- `job_title`
- `company_name`
- `location`
- `industry`
- `years_of_experience`
- `education_level`
- `skills` (list or string format)
- `employment_type`
- `salary` (target variable)

## 🔍 Exploratory Data Analysis (EDA)
- Distribution of job roles and skills
- Correlation heatmaps
- Salary trends by location, experience, and skill set
- Handling of missing/null values

## 🧹 Data Preprocessing
- String parsing using `ast.literal_eval` for structured skill data
- Feature engineering for categorical and text data
- Null value treatment
- One-hot encoding or vectorization of skills (if necessary)

## 🤖 Machine Learning Models
Several regression models were tested:
- **Linear Regression**
- **Lasso / Ridge / ElasticNet**
- **Decision Tree Regressor**
- **Random Forest**
- **Gradient Boosting**
- **XGBoost**
- **Support Vector Regressor**
- **K-Nearest Neighbors**

Models were evaluated using:
- **R² Score**
- **RMSE** (Root Mean Squared Error)
- **Cross-validation scores**

## 📈 Best Performing Model
(You can fill this in after evaluation)

Example:
> Gradient Boosting Regressor with an R² score of 0.82 on the test set and lowest RMSE among all models.

## 📁 Folder Structure
```
job-market-salary-prediction/
├── job market_ 2.ipynb         # Main Jupyter Notebook
├── data/                       # Dataset files (CSV/Excel)
├── models/                     # Saved model files (optional)
└── README.md                   # Project documentation
```

## ✅ Future Enhancements
- Use NLP techniques to better extract features from unstructured skill text
- Deploy as a web app using Streamlit
- Integrate with real-time job posting APIs for live predictions

## 🙌 Acknowledgments
- Dataset curated from job portals or scraped from public repositories
- Libraries used: `pandas`, `sklearn`, `xgboost`, `matplotlib`, `seaborn`

## Live link
-https://predictionofsalarybasedonskills-nztexnmfqzoaet4eu9qv3b.streamlit.app
