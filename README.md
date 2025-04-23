# An Adaptive Machine Learning Framework for DDoS Attack Detection 

This project demonstrates the use of machine learning techniques to detect Distributed Denial of Service (DDoS) attacks. By analyzing network traffic data, the system identifies malicious activities, providing a foundation for future mitigation strategies.
## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Dataset](#dataset)
- [Implemented Algorithms](#implemented-algorithms)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

## Introduction
DDoS attacks disrupt network services by overwhelming the target system with excessive traffic. This project leverages machine learning algorithms to analyze patterns in network traffic, detect malicious activities, and lay the groundwork for automated mitigation mechanisms. The system ensures real-time detection against evolving threats, contributing to a secure network environment.

## Features
- Preprocessing and analysis of network traffic data.
- Implementation of machine learning algorithms for DDoS detection.
- Automated routing table updates to mitigate DDoS threats.
- Evaluation metrics for model performance such as accuracy, precision, and recall.
- Visualization of target class distribution and feature correlations.

## Dataset
The dataset used in this project was generated using the Mininet emulator and includes both benign and malicious traffic. It features 23 attributes, such as packet counts, flow duration, source/destination IPs, and protocol types. Malicious traffic includes TCP SYN, UDP flood, and ICMP attacks.

## Implemented Algorithms
The following machine learning algorithms were implemented and evaluated in this project:
- K-Nearest Neighbors (KNN)
- Stochastic Gradient Descent (SGD)
- Logistic Regression
- Naïve Bayes Classifier
- Support Vector Machine (SVM)
- XGBoost Classifier
- Decision Tree
- Quadratic Discriminant Analysis
- Deep Neural Networks (DNN)

Each algorithm was evaluated based on detection accuracy, false-positive rate, and scalability.

## Results
- **Detection Accuracy**: Achieved up to 98.9% accuracy with advanced models like XGBoost and Deep Neural Networks.
- **Visualizations**:
  - Bar plots for class distribution.
  - Correlation heatmaps for feature relationships.
  - Model performance graphs (accuracy vs. epochs, loss vs. epochs).

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your proposed changes.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


