#  Solar Power Forecasting System  
**Spark Internship Project — AI UNIT, King Khalid University**

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![LightGBM](https://img.shields.io/badge/LightGBM-Forecasting-green)
![XGBoost](https://img.shields.io/badge/XGBoost-Predictive-orange)
![Flask](https://img.shields.io/badge/Flask-WebApp-black?logo=flask)
![AI](https://img.shields.io/badge/AI%20Unit-KKU-red)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

##  Overview

This project presents a **machine learning–based solar power forecasting system** trained on real solar panel sensor data collected over a full year with minute-level resolution.  
The system predicts **active power output (W)** based on irradiance, temperature, and environmental features.  
Two models were developed and compared:
- **LightGBM Forecasting Model (15-minute aggregation)**
- **XGBoost Predictive Model (1-hour aggregation)**

The **15-minute LightGBM** model achieved higher accuracy and better short-term forecasting stability.

---

##  Objectives
- Predict **real-time solar power output** with high accuracy.  
- Handle **seasonal and non-linear variations** in irradiance and temperature.  
- Deploy a **Flask web app** for real-time prediction and visualization.  
- Compare forecasting intervals (hourly vs. 15-min).  
- Provide clear visual analysis and system explainability.

---

##  Models Implemented

| Model Type | Algorithm | Interval | Target | R² (Test) | RMSE (W) |
|-------------|------------|-----------|----------|------------|------------|
| Forecasting | LightGBM | 15 min | Active Power | 0.996 | 6,450 |
| Predictive | XGBoost | 1 hour | Active Power | 0.993 | 8,034 |

---

##  Features Used

| Category | Feature | Description |
|-----------|----------|-------------|
| **Irradiance** | `avg_poa_combined`, `avg_ghi_w_m2` | Plane-of-array and global horizontal irradiance |
| **Temperature** | `avg_moduletemp_combined`, `avg_ambienttemp_c` | Module & ambient temperature |
| **Humidity** | `avg_humidity_pct` | Air humidity percentage |
| **Temporal** | `hour`, `day_of_year`, `month` | Time indicators |
| **Cyclical Encoding** | `sin_hour`, `cos_hour`, `sin_day`, `cos_day` | Smooth encoding of time cycles |
| **Autoregressive** | `lag_1`, `lag_2`, `lag_4`, `lag_8`, `lag_16` | Historical lagged active power |
| **Rolling Stats** | `roll_mean_4`, `roll_std_4` | Local mean and variation in recent intervals |

---

##  Hyperparameters (Optimized via GridSearchCV)

| Parameter | Value |
|------------|--------|
| `learning_rate` | 0.05 |
| `num_leaves` | 63 |
| `max_depth` | 8 |
| `min_child_samples` | 20 |
| `n_estimators` | 300 |
| `subsample` | 0.9 |
| `colsample_bytree` | 0.9 |
| `random_state` | 42 |

**Validation Strategy:**  
TimeSeriesSplit with `n_splits=5` to ensure temporal consistency.

---

##  Mathematical Representation

Cyclical encoding ensures smooth time transitions:
\[
\sin_{hour} = \sin\left(\frac{2 \pi \times hour}{24}\right), \quad
\cos_{hour} = \cos\left(\frac{2 \pi \times hour}{24}\right)
\]

\[
\sin_{day} = \sin\left(\frac{2 \pi \times day\_of\_year}{365}\right), \quad
\cos_{day} = \cos\left(\frac{2 \pi \times day\_of\_year}{365}\right)
\]

---

##  Visual Results

| Visualization | Description |
|----------------|-------------|
| ![corr](solar_studio/corr.png) | Correlation heatmap between major features |
| ![relationship_features](solar_studio/relationship_features.png) | Relationship between features and target |
| ![distribution_of_active_power_during_hours](solar_studio/distribution_of_active_power_during_hours.png) | Distribution of active power by time of day |
| ![visula_part_of_day_power](solar_studio/visula_part_of_day_power.png) | Power production pattern throughout the day |
| ![peak](solar_studio/peak.png) | Predicted vs. Actual during peak hours |
| ![actual_vs_predict](solar_studio/actual_vs_predict.png) | Full-day prediction comparison |
| ![xgboot](solar_studio/xgboot.png) | XGBoost model result comparison |
| ![night](solar_studio/night.png) | Night vs daytime irradiance data |
| ![used_web](solar_studio/used_web.gif) | Flask web interface demo |

---

##  Flask Web Deployment

A **Flask-based interactive web app** allows users to:
- Input real solar data manually or use automatic time detection.
- Generate instant predictions from the trained model.
- Automatically reset the page after refresh for a clean interface.

---

##  Acknowledgment

> We would like to express our sincere gratitude to our supervisor  
> **[Eng. Mohammed Mohana ](https://[[(https://www.linkedin.com/in/mohdmohana/)]([https://www.linkedin.com/in/njoud-abdulaziz-26a47b208/](https://www.linkedin.com/in/mohdmohana/))])**,  
> for his constant support, patience, and motivation throughout this project.  
> Despite his busy schedule, he always found time to provide guidance, share insights, and encourage us to dive deeper into new technical areas.  
> His mentorship not only made this project possible but also inspired us to pursue excellence in the field of **AI and renewable energy**.

---

##  Author

 **Nejood A. Bin Eshaq**  
MSc in Computer Science — King Khalid University  
🔗 [LinkedIn Profile](https://[[www.linkedin.com/in/nejood-bin-eshaq](https://www.linkedin.com/in/njoud-abdulaziz-26a47b208/)])
🔗 [Eng. Mohammed Mohana ](https://[[www.linkedin.com/in/nejood-bin-eshaq](https://www.linkedin.com/in/mohdmohana/)])

---

##  Technologies

`Python` • `LightGBM` • `XGBoost` • `Pandas` • `NumPy` • `Matplotlib` • `Flask` • `Scikit-Learn`

---

 **If you find this project useful, please give it a star!**
