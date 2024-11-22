
# Sports Analytics Pipeline

This project is a robust sports analytics platform designed to ingest, process, and analyze sports data, culminating in predictive insights into player performance. The architecture is built on Azure Data Factory (ADF) for data orchestration and Databricks for advanced data processing and machine learning.

---

## Technologies Used

- **Azure Data Factory (ADF):** Orchestrates ETL (Extract, Transform, Load) pipelines for seamless data movement.
- **Databricks:** Conducts data processing, feature engineering, and machine learning model training and evaluation.
- **SQL Database:** Stores cleaned and structured data for reporting and analysis.
- **Flask:** Acts as the backend framework for the application API.
- **React:** Provides an interactive frontend for data visualization.

---

## Machine Learning Algorithm

### **Linear Regression for Performance Prediction**
The project uses **Linear Regression** as the predictive model for forecasting player performance metrics. This model was chosen for its simplicity and effectiveness in predicting continuous numerical outcomes.

### Steps in Machine Learning Workflow:
1. **Data Preprocessing:**
   - Historical performance data of players is cleansed and transformed in Databricks.
   - Features such as game statistics, player attributes, and contextual game details are engineered.

2. **Feature Selection:**
   - Important predictors such as historical averages, position-specific metrics, and recent form are selected for the model.
   - Irrelevant or highly correlated features are filtered out.

3. **Model Training:**
   - A Linear Regression model is trained using the cleaned data.
   - Training is executed in Databricks, utilizing its distributed computing capabilities for large datasets.

4. **Model Evaluation:**
   - The model is evaluated using metrics such as Mean Squared Error (MSE) and R-squared (R²) to ensure accuracy and robustness.

5. **Prediction:**
   - The trained model is used to predict future player performance metrics based on incoming data.

---

## Data Pipeline

### Overview:
The data pipeline integrates Azure Data Factory for ETL processes and Databricks for transformation and analytics, enabling a seamless flow of data from raw ingestion to actionable insights.

---

### **ETL Pipeline with ADF and Databricks**

#### **Extract:**
- Data is ingested from multiple sources such as APIs, CSV files, and databases.
- ADF fetches raw data, including match statistics, player data, and historical performance metrics.

#### **Transform:**
1. **Data Cleaning (Databricks):**
   - Missing values are handled using imputation techniques.
   - Outliers are identified and treated.
   
2. **Data Transformation:**
   - Aggregations such as averages, totals, and recent trends are computed.
   - Categorical variables are encoded using techniques like one-hot encoding or label encoding.

3. **Feature Engineering:**
   - Time-based features such as player performance over the last 5 games are created.
   - Contextual game-specific features such as home/away performance are added.

#### **Load:**
- The cleaned and transformed data is loaded into an SQL database for storage.
- This structured data serves as the basis for machine learning and visualization.

---

### **Machine Learning Pipeline (Databricks):**
1. Data from SQL is read into Databricks for model training.
2. The trained model is serialized and deployed as a service to provide predictions.
3. Predictions are stored back in the database for use in the application.

---

### **Data Flow Visualization**

1. **Data Sources → ADF:** Data is ingested into Azure Data Lake.
2. **ADF → Databricks:** Raw data is sent to Databricks for cleaning and transformation.
3. **Databricks → SQL Database:** Transformed data is stored in the SQL database.
4. **Databricks → ML Pipeline:** Machine learning models are trained and used for prediction.
5. **SQL → Flask API:** Predictions and processed data are served via Flask to the React frontend.

---

## Key Features of the Pipeline:
- **Scalability:** Azure and Databricks enable scaling for large datasets.
- **Modularity:** Each stage of the pipeline (extract, transform, load, and analysis) is decoupled for easier maintenance.
- **Automation:** ADF automates data ingestion and transformation, reducing manual intervention.
- **End-to-End Workflow:** The pipeline ensures a seamless flow from raw data ingestion to actionable insights.



## Running the Application

Follow the steps below to set up and run the application, including both the backend and frontend components.

---

### Backend Setup

1. **Navigate to the `webapp` directory:**
   ```bash
   cd webapp
   ```

2. **Start the backend server:**
   ```bash
   python -m backend.app
   ```

---

### Frontend Setup

1. **Navigate to the `frontend` directory:**
   ```bash
   cd webapp/frontend
   ```

2. **Install dependencies (if not already installed):**
   ```bash
   npm install
   ```

3. **Start the frontend development server:**
   ```bash
   npm start
   ```

---

### Access the Application

1. Once both the backend and frontend servers are running, open your web browser and navigate to the following URL:
   ```
   http://localhost:3000
   ```

2. Interact with the application to explore data visualizations and predictive insights into player performance.

---

Ensure that all required dependencies and services (such as the database and Databricks) are properly configured before running the application.

