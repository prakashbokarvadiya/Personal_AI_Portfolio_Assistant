/**
 * Express.js Backend for Portfolio Assistant (Alternative to FastAPI)
 * Use this if you prefer Node.js instead of Python
 * 
 * Setup:
 * 1. npm init -y
 * 2. npm install express cors dotenv openai
 * 3. Create .env file with OPENAI_API_KEY
 * 4. node backend-express.js
 */

const express = require('express');
const cors = require('cors');
const dotenv = require('dotenv');
const { Configuration, OpenAIApi } = require('openai');

// Load environment variables
dotenv.config();

const app = express();
const PORT = process.env.BACKEND_PORT || 8000;
const OPENAI_API_KEY = process.env.OPENAI_API_KEY;

// Validate API key
if (!OPENAI_API_KEY) {
    console.error('ERROR: OPENAI_API_KEY not found in .env file');
    process.exit(1);
}

// Initialize OpenAI
const configuration = new Configuration({
    apiKey: OPENAI_API_KEY,
});
const openai = new OpenAIApi(configuration);

// Middleware
app.use(cors());
app.use(express.json());

// Portfolio context (same as Python backend)
const PORTFOLIO_CONTEXT = `You are Prakash Bokarvadiya's AI Portfolio Assistant. You represent Prakash's professional profile and expertise.

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

1. CREDIT RISK MODELING SYSTEM (Banking Domain)
   - Problem: Predict customers likely to default on loans
   - Dataset: German Credit Dataset (~1000 records)
   - Features: Credit per month, job/housing stability, account flags
   - Models: Logistic Regression, Random Forest, XGBoost (selected)
   - Metrics: ROC-AUC (0.78), PR-AUC, threshold optimization (0.35)
   - Business Impact: Reduced missed defaults, minimized financial loss, risk-based lending decisions
   - Deployment: Joblib model, API-ready

2. CUSTOMER CHURN PREDICTION SYSTEM (Telecom/Subscription)
   - Problem: Identify customers likely to churn
   - Preprocessing: Pipeline-based, one-hot encoding, scaling, tenure buckets
   - Models: Logistic Regression (final), Random Forest, Gradient Boosting
   - Metrics: Recall-focused, Precision-Recall, threshold tuning (~0.35)
   - Explainability: SHAP for global & local insights
   - Business Impact: Proactive retention, revenue protection
   - Deployment: FastAPI API for predictions

3. HOUSE PRICE PREDICTION (Real Estate / Regression)
   - Dataset: Kaggle House Prices (79 features, ~1460 records)
   - Features: Log transforms, interactions, total area calculations
   - Models: Linear, Ridge, Lasso, XGBoost (selected)
   - Performance: MAE 0.88%, tail-risk analysis
   - Key Achievement: Fixed 26% underprediction error in tail (expensive homes)
   - Deployment: FastAPI inference service, partial input handling
   - Business Insight: Tail-risk-aware regression improves deployment reliability

4. CREDIT CARD FRAUD DETECTION SYSTEM (Fintech/Security)
   - Problem: Real-time fraud detection under extreme class imbalance (<0.2%)
   - Dataset: Credit Card transactions (~284k), PCA features
   - Features: Log_amount, time-of-day, transaction velocity, interactions
   - Models: Logistic Regression, Random Forest, XGBoost (selected)
   - Metrics: Recall ~91%, threshold tuned for business cost
   - Business Impact: Reduced missed fraud 60%, protects assets, minimizes chargebacks
   - Deployment: FastAPI backend, Streamlit frontend for real-time prediction

TECHNICAL SKILLS:

PYTHON:
- Data structures (lists, tuples, dictionaries)
- Memory management (shallow vs deep copy)
- Functional programming (lambda, map, filter)
- Exception handling

SQL:
- WHERE vs HAVING clauses
- JOIN operations (INNER, LEFT, RIGHT, FULL OUTER)
- Aggregation (COUNT, GROUP BY)
- Window functions (ROW_NUMBER, RANK, LAG, LEAD)

DATA ANALYSIS:
- Exploratory Data Analysis (EDA)
- Data cleaning & preprocessing
- Feature engineering & selection

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
6. Highlight quantified business impact metrics when relevant`;

// Health check endpoint
app.get('/health', (req, res) => {
    res.json({
        status: 'healthy',
        service: 'Portfolio Assistant API (Express)'
    });
});

// Root endpoint
app.get('/', (req, res) => {
    res.json({
        message: 'Prakash Bokarvadiya Portfolio Assistant API',
        endpoints: {
            chat: 'POST /chat - Send a message to the assistant',
            health: 'GET /health - Health check'
        }
    });
});

// Chat endpoint
app.post('/chat', async (req, res) => {
    try {
        const { message, conversation_history } = req.body;

        // Validate input
        if (!message || !message.trim()) {
            return res.status(400).json({
                success: false,
                error: 'Message cannot be empty'
            });
        }

        // Build messages array
        const messages = [
            {
                role: 'system',
                content: PORTFOLIO_CONTEXT
            }
        ];

        // Add conversation history if provided
        if (Array.isArray(conversation_history)) {
            messages.push(...conversation_history);
        }

        // Add current message
        messages.push({
            role: 'user',
            content: message
        });

        // Call OpenAI API
        const response = await openai.createChatCompletion({
            model: 'gpt-3.5-turbo',
            messages: messages,
            max_tokens: 500,
            temperature: 0.7,
            top_p: 0.9,
        });

        const assistantMessage = response.data.choices[0].message.content.trim();

        res.json({
            response: assistantMessage,
            success: true
        });

    } catch (error) {
        console.error('Error in chat endpoint:', error.message);
        
        // Don't expose sensitive error details to frontend
        res.status(500).json({
            success: false,
            error: 'An error occurred while processing your request. Please try again.'
        });
    }
});

// Error handling middleware
app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).json({
        success: false,
        error: 'Internal server error'
    });
});

// Start server
app.listen(PORT, () => {
    console.log(`\n✅ Portfolio Assistant API running on http://localhost:${PORT}`);
    console.log(`📧 Chat endpoint: POST http://localhost:${PORT}/chat`);
    console.log(`🏥 Health check: GET http://localhost:${PORT}/health`);
    console.log(`\nPress CTRL+C to stop\n`);
});

module.exports = app;
