from flask import Flask, request, render_template, redirect, url_for
import numpy as np
import pandas as pd
from joblib import load
from datetime import datetime
import lightgbm as lgb

app = Flask(__name__)


#model = lgb.Booster(model_file="best_lgbm_forecast_15min.joblib")
#model = load("best_lgbm_forecast_15min.txt")

model = lgb.Booster(model_file="best_lgbm_forecast_15min.txt")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["GET", "POST"])

#@app.route("/predict", methods=["POST"])
def predict():
    try:
        use_auto_time = request.form.get("autoTime")

        # Read numeric inputs
        ghi = float(request.form["GHI"])
        poa = float(request.form["POA1"])
        module_temp = float(request.form["ModuleTemp1"])
        ambient_temp = float(request.form["AmbientTemp"])
        humidity = float(request.form["Humidity"])

        # Determine time
        if use_auto_time:
            now = datetime.now()
            hour = now.hour
            day_of_year = now.timetuple().tm_yday
            month = now.month
        else:
            hour = int(request.form.get("Hour", 0))
            day_of_year = int(request.form.get("DayOfYear", 0))
            month = datetime.now().month  # fallback to current month

        # Trigonometric encodings
        sin_hour = np.sin(2 * np.pi * hour / 24)
        cos_hour = np.cos(2 * np.pi * hour / 24)
        sin_day = np.sin(2 * np.pi * day_of_year / 365)
        cos_day = np.cos(2 * np.pi * day_of_year / 365)

        # Dummy lag/rolling features (for live prediction)
        lag_1 = lag_2 = lag_4 = lag_8 = lag_16 = 0
        roll_mean_4 = roll_std_4 = 0

        # Construct input DataFrame (exact 19 features)
        features = pd.DataFrame([{
            "avg_poa_combined": poa,
            "avg_ghi_w_m2": ghi,
            "avg_moduletemp_combined": module_temp,
            "avg_ambienttemp_c": ambient_temp,
            "avg_humidity_pct": humidity,
            "hour": hour,
            "day_of_year": day_of_year,
            "month": month,
            "sin_hour": sin_hour,
            "cos_hour": cos_hour,
            "sin_day": sin_day,
            "cos_day": cos_day,
            "lag_1": lag_1,
            "lag_2": lag_2,
            "lag_4": lag_4,
            "lag_8": lag_8,
            "lag_16": lag_16,
            "roll_mean_4": roll_mean_4,
            "roll_std_4": roll_std_4
        }])

        # ✅ Prediction
        prediction = model.predict(features)[0]

        return render_template("index.html", prediction_text=f"Predicted Power: {prediction:.2f} W")

    except Exception as e:
        return render_template("index.html", prediction_text=f" Error occurred: {e}")

@app.route("/reset")
def reset():
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
