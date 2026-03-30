# AI-Based-Student-Performance-Predictor-Study-Recommendation-System
This project predicts a student's chances of passing or failing based on factors like study time, attendance, completed assignments, and previous grades. The system looks at input data and makes predictions using a supervised learning method known as logistic regression. It also provides simple study tips to help students improve their grades

# AI-Based Student Performance Predictor

## Short Description

The AI-Based Student Performance Predictor is a Machine Learning project that predicts whether a student will pass or fail based on factors such as study hours, attendance, assignments completed, and previous marks. The system uses a supervised learning algorithm (Logistic Regression) to analyze the input data and generate predictions. It also provides simple recommendations to help students improve their academic performance.

## Features

* Pass/Fail prediction
* Machine learning-based model
* Simple command-line interface
* Study recommendations
* Easy to run and modify

## Technologies Used

* Python
* NumPy
* Pandas
* Scikit-learn
* Machine Learning (Logistic Regression)

## Project Structure

```
student-ai-project/
│
├── dataset.csv
├── train_model.py
├── predictor.py
├── main.py
├── requirements.txt
├── README.md
└── Project_Report.md
```

## Installation

Install required libraries:

```
python -m pip install -r requirements.txt
```

## How to Run

### Step 1: Train the model

```
python train_model.py
```

### Step 2: Run the predictor

```
python main.py
```

## Example Input

```
Hours studied per day: 4
Attendance (%): 75
Assignments completed: 5
Previous marks: 60
```

## Example Output

```
Prediction: Pass
Good performance! Keep it up.
```

## Future Improvements

* Add GUI interface
* Add performance graphs
* Use larger dataset
* Deploy as web application


