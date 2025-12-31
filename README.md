##MLFLOW Library used in all record on project wllbe recorded and compare to each other and visulize in all graps.
# MLflow – Experiment Tracking & Model Management 

This repository demonstrates **hands-on usage of MLflow** for tracking machine learning experiments, logging models, metrics, parameters, and managing the complete ML lifecycle in an **industry-style workflow**.

---

##  Project Overview

MLflow is used in this project to:

- Track multiple ML experiments
- Compare different model runs
- Log parameters, metrics & artifacts
- Store trained models
- Visualize experiment performance using MLflow UI

This project is designed to reflect **real-world MLOps practices** used in production ML systems.

---

##  What is MLflow?

**MLflow** is an open-source platform to manage the ML lifecycle, including:

- Experiment tracking
- Model packaging
- Model registry
- Deployment support

---

##  Project Structure
MLFLOW/
│
├── mlflow.db # Local MLflow tracking database
├── app.py # Model training & logging logic
├── requirements.txt # Dependencies
├── README.md # Project documentation
└── artifacts/ # Logged artifacts (models, metrics)


---

## ⚙️ Tech Stack Used

- **Python**
- **Scikit-learn**
- **MLflow**
- **SQLite** (for MLflow backend store)
- **Git & GitHub**

---

## 🔄 Workflow

1. Load dataset
2. Train ML model(s)
3. Log:
   - Parameters
   - Metrics
   - Models
4. Compare runs using MLflow UI
5. Select best performing model

---

##  MLflow UI

Start MLflow UI:
```bash
mlflow ui







