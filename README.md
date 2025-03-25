# chat_summary
# Chat Transcript Summarization API

## 📌 Project Overview
This project provides a FastAPI-based solution to summarize chat transcripts. The API extracts insights such as:
- The **possible article link** discussed.
- The **number of messages** sent by each agent.
- The **overall sentiment distribution** for each agent.

Additionally, **Exploratory Data Analysis (EDA) and Data Ingestion** scripts are included to process and visualize the dataset.

## 🚀 Features
- **Dynamic Input Support** – Users can input chat data via terminal or API.
- **Sentiment Analysis** – Summarizes positive, neutral, and negative sentiments.
- **FastAPI Framework** – Provides a lightweight and scalable API.
- **Interactive API Documentation** – Accessible via Swagger UI (`/docs`).
- **EDA & Data Ingestion** – Analyzes dataset before API processing.

## 📂 Project Structure
```
📁 Project Folder
│-- chat_summary_api.py  # FastAPI application
│-- eda.ipynb            # Jupyter Notebook for data exploration
│-- data_ingestion.py    # Script to load and preprocess data
│-- requirements.txt     # Dependencies
│-- README.md            # Project documentation
```

## ⚙️ Installation
1️⃣ **Clone the repository**
```bash
 git clone <repository-url>
 cd <project-folder>
```

2️⃣ **Create a virtual environment** (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate  # For macOS/Linux
venv\Scripts\activate    # For Windows
```

3️⃣ **Install dependencies**
```bash
pip install -r requirements.txt
```

## 📊 Exploratory Data Analysis (EDA)
The `eda.ipynb` notebook provides a detailed analysis of the dataset, including:
- **Data Summary** – Overview of dataset columns and types.
- **Missing Value Analysis** – Identifies gaps in the data.
- **Sentiment Distribution** – Plots showing sentiment trends.
- **Agent-wise Analysis** – Message count and sentiment distribution per agent.
- **Turn Rating Insights** – Evaluates the correlation between sentiment and ratings.

📌 **To run the EDA notebook:**
1. Open `eda.ipynb` in **Jupyter Notebook**
2. Run the cells sequentially to analyze the dataset

## 📥 Data Ingestion
The `data_ingestion.py` script is responsible for:
- **Loading raw JSON data**
- **Extracting relevant features (chat ID, messages, agent, sentiment, etc.)**
- **Saving processed data as a structured DataFrame**

📌 **To run data ingestion:**
```bash
python data_ingestion.py
```
This will output a cleaned dataset for analysis and API processing.

## ▶️ Running the API
### **Method 1: Dynamic User Input from Terminal**
```bash
python chat_summary_api.py
```
📌 **Follow the prompts** to enter chat details, and the API will generate a summary.

### **Method 2: Running as a FastAPI Server**
```bash
uvicorn chat_summary_api:app --reload
```
📌 API will be available at:
- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- Redoc UI: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## 🔄 How the API Works
### **1️⃣ GET Request** – `http://127.0.0.1:8000/`
Returns a simple welcome message:
```json
{"message": "Welcome to the Chat Summary API! Go to /docs to test."}
```

### **2️⃣ POST Request** – `http://127.0.0.1:8000/summarize_chat`
Accepts a **chat transcript** as input and returns a summary.

### **📌 Example JSON Input**
```json
{
  "chat_id": "chat123",
  "content": [
    {"message": "Check out this article: http://example.com", "agent": "Agent 1", "sentiment": "positive"},
    {"message": "I think it's great!", "agent": "Agent 2", "sentiment": "positive"}
  ]
}
```

### **📌 Expected API Response**
```json
{
  "chat_id": "chat123",
  "possible_article_link": "Check out this article: http://example.com",
  "messages_by_agent_1": 1,
  "messages_by_agent_2": 1,
  "overall_sentiment_agent_1": {"positive": 1},
  "overall_sentiment_agent_2": {"positive": 1}
}
```

## 🛠️ Deployment (Optional)
To deploy the API on **Render** or **Railway**, follow their documentation:
- Render: [https://render.com/docs/deploy-fastapi](https://render.com/docs/deploy-fastapi)
- Railway: [https://railway.app](https://railway.app)

## 📌 Summary
This API efficiently summarizes chat transcripts by extracting key insights. It can be run **locally** for testing or **deployed** for broader access.

🚀 **Now, try running the API and generate chat insights dynamically!** 🎯

