# PREDICTIVE-MAINTENENCE-SYSTEM-FOR-IOT-DEVICES
The **Predictive Maintenance System for IoT Devices** is a machine-learning–based web application that predicts the probability of machine failure using real-time IoT sensor data.Instead of relying on scheduled or reactive maintenance, this system analyzes sensor signals such as vibration, acoustic levels, temperature, electrical current, and time parameters to predict failures in advance, helping reduce downtime and maintenance costs.

This project is especially useful for manufacturing units, smart factories, IoT engineers, and students exploring industrial AI applications.
## Overview
The system is trained on historical IoT sensor data and uses a supervised machine learning model saved as a .pkl file.
It is deployed as an interactive Streamlit web application, allowing users to simulate machine conditions and instantly receive failure risk predictions.

The application enables users to:

- Select machine ID
- Input sensor readings via sliders
- Predict failure probability
- View risk level (Normal / Warning / Failure Likely)
- Visualize results using an interactive gauge

The focus of this project is early fault detection and decision support rather than reactive troubleshooting.

## Tools and Technologies Used

- **Python:** Core language for data processing and application logic

- **Streamlit:** Interactive web-based UI

- **Scikit-learn:** Machine learning model training and prediction

- **Joblib:** Efficient model serialization and loading

- **NumPy:** Numerical computations

- **Pandas:** Structured data handling

- **Plotly:** Interactive gauge visualization for failure probability
## Why These Tools Were Selected

- Machine learning models can detect failure patterns earlier than manual monitoring
- Streamlit allows rapid deployment without backend complexity
- Plotly provides intuitive visual interpretation of risk levels
- Joblib ensures fast and reliable model loading
- Pandas and NumPy simplify sensor data preprocessing

Together, these tools create a lightweight, fast, and industry-oriented predictive system.
## Features

- Real-time failure risk prediction
- Interactive sensor input sliders
- Failure probability gauge meter
- Color-coded risk levels:

     - 🟢 Normal
  
     - 🟡 Warning
  
     - 🔴 Failure Likely
- Numeric probability display
- Clean and professional UI
- No retraining required during inference
## How It Works

- User selects a Machine ID
- User provides sensor inputs:
     - Vibration
     - Acoustic signal
     - Temperature
     - Current
     - Time (Hour & Minute)
- Input data is converted into a structured DataFrame
- Trained ML model predicts failure probability
- System assigns a risk category based on probability thresholds
- Results are displayed using:
     - Risk indicator panel
     - Interactive probability gauge
     - Percentage metric
     - 
## Advantages
- Prevents unexpected machine breakdowns
- Enables condition-based maintenance
- Reduces operational downtime
- Easy-to-use dashboard for non-technical users
- Lightweight and fast execution
- Suitable for academic and industrial demonstrations
## Limitations

- Accuracy depends on training data quality
- Works best with sensor ranges similar to training data
- Not a replacement for physical inspection
- Simulated inputs may differ from real-world sensor noise
- Requires proper sensor calibration in production use
## Real-Time Applications

- Smart manufacturing systems
- Industrial IoT monitoring
- Factory equipment health analysis
- Predictive maintenance planning
- AI & Data Science academic projects
- Industry 4.0 demonstrations
## Future Enhancements

- Live IoT sensor data integration
- Time-series prediction using LSTM
- Remaining Useful Life (RUL) estimation
- Maintenance recommendation engine
- Cloud deployment (AWS / Azure)
- Role-based dashboards
- Alert system (Email / SMS)
- Model retraining pipeline
## Conclusion

The Predictive Maintenance System for IoT Devices demonstrates how machine learning can be effectively applied to industrial IoT problems.
By combining predictive analytics with an intuitive web interface, the system enables proactive maintenance decisions that save time, cost, and resources.
With future enhancements, this project can evolve into a production-ready Industry 4.0 solution.

## Output
<img width="1707" height="847" alt="Image" src="https://github.com/user-attachments/assets/fd476713-d6f8-43d8-9413-691f10592007" />

<img width="563" height="580" alt="Image" src="https://github.com/user-attachments/assets/a256b5ac-2d8c-4be8-acc5-2c609ce3d276" />

<img width="548" height="582" alt="Image" src="https://github.com/user-attachments/assets/256dcc89-afd9-4f14-8cb4-acc09051688e" />
