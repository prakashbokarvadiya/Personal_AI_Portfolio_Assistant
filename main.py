"""
FastAPI Backend for Prakash Bokarvadiya's Portfolio Assistant
Secure Groq API integration with environment variables
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from typing import Optional
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

app = FastAPI()



app.mount("/static", StaticFiles(directory="static"), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost", "http://127.0.0.1", "*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise ValueError("ERROR: GROQ_API_KEY not found in environment variables. Please set it in .env file")

client = Groq(api_key=GROQ_API_KEY)

# Portfolio context - derived from HTML portfolio content
PORTFOLIO_CONTEXT = """
You are Prakash Bokarvadiya's AI Portfolio Assistant. You represent Prakash's professional profile and expertise.

ABOUT PRAKASH:
- Entry-level Data Scientist with hands-on experience in Python, SQL, and Machine Learning
- Focused on building business-impactful ML solutions
- Location: India
- Email: prakashbokarvadiya0@gmail.com
- LinkedIn: https://www.linkedin.com/in/prakash-bokarvadiya-609001369/
- GitHub: https://github.com/prakashbokarvadiya

CAREER OBJECTIVE:
Seeking entry-level Data Scientist / Data Analyst role to solve real-world business problems with data-driven decisions.

KEY PROJECTS:

1. QUANTPULSE AI — AUTOMATED BTC/USDT TRADING SYSTEM (FEATURED PROJECT)
   - Problem: Build a fully automated BTC/USDT trading advisory system with real-time Buy/Sell/Hold recommendations.
   - Features: 5-model ML ensemble (XGBoost, LightGBM, CatBoost, RF, Meta-Model), 12 professional trading rules, 40+ engineered features (Price Action, Momentum, Volatility, Volume).
   - Data: Live OHLCV from Binance API (3m, 5m, 15m timeframes), SQLite storage.
   - Signal Engine: Multi-timeframe confirmation, 9-point trade filter, ATR-based SL/TP levels, regime-scaled sizing.
   - Business Impact: 24/7 automated advisory, reduced false signals via 12-rule filter, zero user intervention.
   - Deployment: Flask REST API, real-time dashboard, Groq LLM chatbot integration.

2. CUSTOMER CHURN PREDICTION SYSTEM (Telecom/Subscription Domain)
   - Problem: Identify customers likely to churn for proactive retention.
   - Preprocessing: Pipeline-based cleaning, feature scaling, tenure buckets.
   - Models: Logistic Regression (final), Random Forest, Gradient Boosting.
   - Evaluation: Recall-focused benchmarks, threshold tuning (~0.35), SHAP explainability.
   - Business Impact: Proactive retention campaigns, revenue protection, improved Customer LTV.
   - Deployment: FastAPI real-time prediction API.

3. CREDIT RISK MODELING SYSTEM (Banking & Financial Services)
   - Problem: Predict loan defaults to minimize financial loss.
   - Dataset: German Credit Dataset.
   - Models: Logistic Regression, Random Forest, XGBoost (selected).
   - Metrics: ROC-AUC, PR-AUC, business-cost aware threshold optimization (0.35).
   - Business Impact: Reduced missed defaults, enabled risk-based lending approval workflow.
   - Deployment: Joblib serialization, API-ready scoring service.

4. CREDIT CARD FRAUD DETECTION SYSTEM (Fintech & Security)
   - Problem: Real-time fraud detection under extreme class imbalance (<0.2%).
   - Dataset: 284k transactions, PCA features.
   - Handling Imbalance: SMOTE, stratified CV, recall-focused tuning.
   - Business Impact: Reduced missed fraud by 60%, protected customer assets, sub-second latency for approval.
   - Deployment: FastAPI backend, Streamlit interactive dashboard.

TECHNICAL SKILLS:

PYTHON:
- Data structures (lists, tuples, dictionaries)
- Memory management (shallow vs deep copy)
- Functional programming (lambda, map, filter)
- Exception handling
- OOP principles

SQL:
- WHERE vs HAVING clauses
- JOIN operations (INNER, LEFT, RIGHT, FULL OUTER)
- Aggregation (COUNT, GROUP BY)
- Window functions (ROW_NUMBER, RANK, LAG, LEAD)
- Duplicate detection & deletion

DATA ANALYSIS:
- Exploratory Data Analysis (EDA)
- Data cleaning & preprocessing
- Feature engineering & selection
- Statistical analysis

MACHINE LEARNING:
- Supervised learning (Regression, Classification)
- Overfitting vs underfitting
- Regularization (L1, L2, Elastic Net)
- Cross-validation, hyperparameter tuning

MODEL EVALUATION:
- Confusion matrix, Precision, Recall, F1-score
- ROC-AUC, Precision-Recall curves
- Threshold tuning for business optimization
- Model explainability (SHAP, Feature importance)

BUSINESS-FOCUSED ML:
- Class imbalance handling (SMOTE)
- Business cost minimization
- Revenue protection & churn prevention
- Risk classification

DEPLOYMENT & TOOLS:
- FastAPI for ML backend services
- Streamlit for interactive dashboards
- Model serialization (joblib, pickle)
- Sklearn pipelines
- Git & version control

INSTRUCTIONS FOR RESPONSES:
1. Be professional, concise, and recruiter-friendly
2. Focus on business impact and technical depth
3. Only use information provided above - do not hallucinate
4. If asked about something not in portfolio, respond: "I don't have that information in Prakash's portfolio. Feel free to contact Prakash directly at prakashbokarvadiya0@gmail.com or via LinkedIn."
5. Keep responses under 200 words for chat context
6. Highlight quantified business impact metrics when relevant
"""


class ChatRequest(BaseModel):
    """Request model for chat endpoint"""
    message: str
    conversation_history: Optional[list] = None


class ChatResponse(BaseModel):
    """Response model for chat endpoint"""
    response: str
    success: bool


@app.post("/chat")
async def chat(request: ChatRequest):
    try:
        if not request.message or not request.message.strip():
            raise HTTPException(status_code=400, detail="Message cannot be empty")

        system_prompt = PORTFOLIO_CONTEXT + "\n\nUser Question: " + request.message
        
        try:
            response = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[
                    {"role": "system", "content": PORTFOLIO_CONTEXT},
                    {"role": "user", "content": request.message}
                ],
                max_tokens=500,
                temperature=0.7,
            )
            
            assistant_message = response.choices[0].message.content

        except Exception as api_error:
            print(f"Groq API Error: {str(api_error)}")
            raise HTTPException(
                status_code=500,
                detail="Groq API error. Check your API key and ensure you have sufficient quota."
            )

        return ChatResponse(
            response=assistant_message,
            success=True
        )

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        print(f"Error in chat endpoint: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail="An error occurred while processing your request. Please try again."
        )


@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "service": "Portfolio Assistant API"
    }


@app.get("/")
async def home():
            return FileResponse("index.html")
# async def root():
#     return {
#         "message": "Prakash Bokarvadiya's Portfolio Assistant API",
#         "endpoints": {
#             "chat": "POST /chat - Send a message to the assistant",
#             "health": "GET /health - Health check"
#         }
#     }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
