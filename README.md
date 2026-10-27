**Deep Learning-Based Login Anomaly Detection Using ANN**

**Overview**

This project uses an Artificial Neural Network (ANN) built with TensorFlow to classify login activity as Normal or Suspicious based on failed login attempts and unfamiliar login locations.

**Objectives**

- Identify potentially suspicious login activity using deep learning.
- Explore neural network training and binary classification.
- Demonstrate how machine learning can support cybersecurity monitoring.

**Technologies Used**

- Python
- TensorFlow / Keras
- NumPy
- Scikit-learn

**Dataset**

A small, manually created sample dataset containing 10 login records.

**Features:**

- "Failed Login Attempts": Number of unsuccessful login attempts.
- "Unfamiliar Location": "0" = No, "1" = Yes.

**Labels:**

- "0" = Normal
- "1" = Suspicious

**Model Architecture**

The ANN consists of:

- Input layer: 2 features
- Hidden layer 1: 8 neurons with ReLU activation
- Hidden layer 2: 4 neurons with ReLU activation
- Output layer: 1 neuron with sigmoid activation

**Implementation**

1. Prepare the login activity dataset.
2. Split the data into training and testing sets (70:30).
3. Scale the input features using StandardScaler.
4. Train the ANN for 50 epochs.
5. Evaluate the model on test data.
6. Predict whether a new login is normal or suspicious.

**Example Prediction**

Input:

- Failed login attempts: 8
- Unfamiliar location: Yes ("1")

Output: The model predicts a suspicious-login score and classifies the activity using a threshold of "0.5".

Note: The predicted result depends on the model's training and is not guaranteed.

**How to Run**

1. Install dependencies

pip install numpy tensorflow scikit-learn

2. Run the Python script

python login_anomaly_detection.py

**Limitations**

- Uses only 10 manually created sample records.
- The model's accuracy and predictions are not reliable enough for real-world security decisions.
- An unfamiliar location or multiple failed logins alone does not prove malicious activity.

**Future Improvements**

- Use a larger, realistic login dataset.
- Include IP reputation, login time, device information, and geolocation changes.
- Compare ANN performance with Random Forest and other classification models.
- Add evaluation metrics such as precision, recall, F1-score, and a confusion matrix.

**Author**

ANMOL BHONSLE 
