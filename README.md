# Student Performance Prediction

This project predicts student performance based on study habits, attendance, previous grades, internet access, and parental education. It features a machine learning backend and a simple web frontend.

## Project Structure

- **backend/**  
  Flask API and model training scripts.
  - `app.py`: Flask server serving predictions and frontend.
  - `train_model.py`: Script to train and save the ML model and preprocessors.
- **frontend/**  
  Web interface for user input and displaying predictions.
  - `index.html`: Main web page.
  - `script.js`: Handles form submission and API calls.
  - `style.css`: Page styling.
- **data/**  
  - `student_data.csv`: Dataset used for training.
- **models/**  
  Saved model and preprocessing objects (`model.pkl`, `scaler.pkl`, `encoder.pkl`).
- **notebooks/**  
  - `EDA.ipynb`: Exploratory data analysis notebook.
- **visualizations/**  
  Folder for generated plots and charts.

## How to Run

1. **Install dependencies**  
   In the `backend/` directory:
   ```sh
   pip install flask pandas scikit-learn joblib