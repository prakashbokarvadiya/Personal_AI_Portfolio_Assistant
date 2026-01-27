# Prakash Bokarvadiya - Data Science Portfolio with AI Chatbot

A professional, one-page portfolio website for a Data Science fresher featuring an intelligent AI chatbot powered by OpenAI's GPT-3.5-turbo.

## 🎯 Features

### Portfolio Website
- **Clean, minimalist design** - Professional and recruiter-friendly
- **Fully responsive** - Works on mobile, tablet, and desktop
- **One-page layout** - All information easily accessible
- **Dark/light color scheme** - Modern gradient backgrounds
- **Fast loading** - No external dependencies, pure HTML/CSS/JS

### AI Chatbot
- **Floating chat button** - 💬 in bottom-right corner
- **Portfolio-specific** - Only answers based on portfolio information
- **Conversation history** - Context-aware responses
- **Secure API integration** - OpenAI API key protected via environment variables
- **Production-ready** - Error handling, CORS, input validation

### Sections Included
1. **About Me** - Career overview, key strengths, career objective
2. **4 Featured Projects**
   - Credit Risk Modeling (Banking)
   - Customer Churn Prediction (Telecom)
   - House Price Prediction (Real Estate)
   - Fraud Detection System (Fintech)
3. **Technical Skills** - Python, SQL, ML, Data Analysis, Deployment
4. **Contact** - Email, LinkedIn, GitHub links

## 🚀 Quick Start

### Prerequisites
- Python 3.8+ (or Node.js 14+)
- OpenAI API key from [platform.openai.com/api-keys](https://platform.openai.com/api-keys)

### Step 1: Clone or Download
```bash
# Download or clone this repository
cd "e:\1 Month\project 5"
```

### Step 2: Set Up Environment
```bash
# Create .env file
cp .env.example .env

# Add your OpenAI API key
# Edit .env and replace sk-your-api-key-here with your actual key
```

### Step 3: Install Dependencies
```bash
# Python (FastAPI - Recommended)
pip install -r requirements.txt

# OR Node.js (Express - Alternative)
npm install
```

### Step 4: Run Backend
```bash
# Python
python backend.py

# OR Node.js
npm start
```

### Step 5: Open Portfolio
- Open `index.html` in your browser
- Click the 💬 button to test the chatbot

## 📁 Project Structure

```
e:\1 Month\project 5\
├── index.html                    # Main portfolio website + chatbot UI
├── backend.py                    # FastAPI backend
├── backend-express.js            # Express.js alternative
├── requirements.txt              # Python dependencies
├── package.json                  # Node.js dependencies
├── .env                          # Your API key (CREATE THIS)
├── .env.example                  # Environment template
├── .gitignore                    # Git ignore file
├── profile.jpg                   # Your profile photo
├── credit_risk_chart.jpg         # Project visualizations
├── churn_prediction_chart.jpg
├── house_price_chart.jpg
├── fraud_detection_chart.jpg
├── README.md                     # This file
├── COMPLETE_SETUP.md             # Detailed setup guide
├── CHATBOT_SETUP.md              # Chatbot-specific guide
├── QUICK_REFERENCE.md            # Quick command reference
├── IMPLEMENTATION_SUMMARY.md     # Technical overview
└── ARCHITECTURE_DIAGRAMS.md      # System architecture
```

## 🔧 Configuration

### Change Chatbot Responses
Edit `PORTFOLIO_CONTEXT` in `backend.py` to customize what the chatbot knows about you.

### Change Backend URL
If deploying backend elsewhere, update in `index.html`:
```javascript
const BACKEND_URL = 'https://your-production-backend.com/chat';
```

### Change AI Model
In `backend.py`, update:
```python
model="gpt-3.5-turbo"  # Change to "gpt-4" for more advanced responses
```

## 🔐 Security

- ✅ API key stored in `.env` (never exposed to frontend)
- ✅ `.env` added to `.gitignore` (not committed to Git)
- ✅ CORS configured for safe cross-origin requests
- ✅ Error handling without exposing sensitive data
- ✅ Input validation on backend
- ✅ HTTPS recommended for production

## 📊 API Reference

### POST /chat
Send a message to the portfolio assistant.

**Request:**
```json
{
  "message": "Tell me about your projects",
  "conversation_history": [
    {"role": "user", "content": "Hi"},
    {"role": "assistant", "content": "Hello!"}
  ]
}
```

**Response:**
```json
{
  "response": "I have 4 main projects: Credit Risk Modeling...",
  "success": true
}
```

### GET /health
Health check endpoint.

**Response:**
```json
{
  "status": "healthy",
  "service": "Portfolio Assistant API"
}
```

## 💰 Costs

- **GPT-3.5-turbo**: ~$0.0005 per message (very affordable)
- **Free tier**: $5 credit for 3 months
- **Typical usage**: 1,000 messages = ~$0.50

Monitor usage at: [platform.openai.com/account/usage](https://platform.openai.com/account/usage)

## 🚢 Deployment

### Heroku (Recommended)
```bash
heroku login
heroku create your-bot-name
git push heroku main
heroku config:set OPENAI_API_KEY=sk-your-key
```

### AWS Lambda
```bash
pip install zappa
zappa init
zappa deploy dev
```

### PythonAnywhere
1. Create account at [pythonanywhere.com](https://www.pythonanywhere.com)
2. Upload files
3. Configure web app
4. Set environment variables

## 🎓 Technologies Used

- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Backend**: FastAPI (Python) or Express.js (Node.js)
- **AI**: OpenAI GPT-3.5-turbo API
- **Deployment**: Heroku, AWS, PythonAnywhere, or custom VPS

## 📝 Documentation

- **COMPLETE_SETUP.md** - Full setup instructions with troubleshooting
- **CHATBOT_SETUP.md** - Detailed chatbot integration guide
- **QUICK_REFERENCE.md** - Command quick reference
- **IMPLEMENTATION_SUMMARY.md** - Technical implementation details
- **ARCHITECTURE_DIAGRAMS.md** - System architecture and data flow

## 🐛 Troubleshooting

| Problem | Solution |
|---------|----------|
| `ModuleNotFoundError` | `pip install -r requirements.txt` |
| `OPENAI_API_KEY not found` | Create `.env` file with your API key |
| Chatbot not responding | Ensure backend is running: `python backend.py` |
| CORS error | Check `BACKEND_URL` in `index.html` |
| 401 API error | Verify API key is valid at https://platform.openai.com/account |

For more troubleshooting, see **CHATBOT_SETUP.md**.

## 📞 Support

- **OpenAI API Docs**: https://platform.openai.com/docs
- **FastAPI**: https://fastapi.tiangolo.com
- **Express.js**: https://expressjs.com

## ✨ Features Highlight

- ✅ Production-ready code
- ✅ Full-stack implementation
- ✅ Secure API integration
- ✅ Professional UI/UX
- ✅ Responsive design
- ✅ Zero external dependencies (portfolio)
- ✅ Comprehensive documentation
- ✅ Deployment-ready

## 📄 License

This project is open source and available under the MIT License.

## 👨‍💼 About

**Prakash Bokarvadiya** - Data Science & Machine Learning enthusiast

- 📧 Email: prakashbokarvadiya0@gmail.com
- 🔗 LinkedIn: https://www.linkedin.com/in/prakash-bokarvadiya-609001369/
- 💻 GitHub: https://github.com/prakashbokarvadiya

## 🎉 Getting Started

1. Get OpenAI API key from [platform.openai.com/api-keys](https://platform.openai.com/api-keys)
2. Create `.env` file with your API key
3. Install dependencies: `pip install -r requirements.txt`
4. Run backend: `python backend.py`
5. Open `index.html` in browser
6. Click 💬 to start chatting!

---

**Ready to impress recruiters? Deploy your portfolio with AI! 🚀**
