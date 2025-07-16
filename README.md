# 🌱 Smart Crop Recommender System

This is a **Machine Learning-based web application** that recommends the most suitable crop to grow based on soil and weather conditions.  
It uses a Random Forest model trained on the **Crop Recommendation Dataset** and is deployed with **Streamlit Cloud**.


## 🚀 Live App
👉 [**Smart Crop Recommender**](https://smart-crop-recommender.streamlit.app/)


## ✨ Features
✅ Input N, P, K values of soil  
✅ Input temperature, humidity, pH, and rainfall  
✅ Get an instant **recommended crop**  
✅ User-friendly **Streamlit UI**  
✅ Deployed and accessible online


## 📊 Dataset
- Dataset used: **Crop Recommendation Dataset**
- **Features:**
  - `N` (Nitrogen)
  - `P` (Phosphorus)
  - `K` (Potassium)
  - `temperature` (°C)
  - `humidity` (%)
  - `ph`
  - `rainfall` (mm)
- **Target:** `label` (Crop name)


## 🖥️ Tech Stack
- **Language:** Python  
- **ML Library:** scikit-learn  
- **Framework:** Streamlit  
- **Deployment:** Streamlit Community Cloud  
- **Environment:** Anaconda, Jupyter Notebook
  

## 📂 Project Structure

🌾 smart-crop-recommender
```text
 ├─ app.py                     # Streamlit app script
 ├─ crop_model.pkl             # Saved ML model
 ├─ Crop_recommendation.csv    # Dataset
 ├─ Crop_Recommendation.ipynb  # Jupyter Notebook
 ├─ requirements.txt           # Required libraries
 └─ README.md                  # Project documentation

```
⚙️ How It Works
1. Train a RandomForest model on dataset.
2. Save trained model as crop_model.pkl using pickle.
3. Create app.py with Streamlit sliders for user inputs.
4. Load model and predict crop.
5. Deploy app via Streamlit Cloud.

⚙️ Installation (Run Locally)
If you want to run this project locally:

# Clone this repository
git clone https://github.com/brindashah0128/-smart-crop-recommender.git
cd -smart-crop-recommender

# Install required packages
pip install -r requirements.txt

# Run Streamlit app
streamlit run app.py


🌐 Deployment
- Hosted on Streamlit Community Cloud.
- GitHub repository is connected for auto-deployment.

📧 Contact
If you have any questions, feel free to reach out!
Brinda Shah
✉️ sbrinda102@gmail.com

⭐ If you like this project, don’t forget to star the repo on GitHub!
