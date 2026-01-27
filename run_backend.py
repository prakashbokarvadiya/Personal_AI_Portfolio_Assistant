#!/usr/bin/env python3
"""
Startup Script for Portfolio Assistant Backend
Run this file to start the backend server

Usage:
    python backend.py
    
Or if you want more verbose output:
    python -u backend.py
"""

import os
import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

# Banner
print("""
╔════════════════════════════════════════════════════════════════╗
║   Prakash Bokarvadiya - Portfolio Assistant Backend           ║
║                                                                ║
║   Starting FastAPI Server...                                  ║
╚════════════════════════════════════════════════════════════════╝
""")

# Check for .env file
env_path = project_root / ".env"
if not env_path.exists():
    print("⚠️  WARNING: .env file not found!")
    print("   Please create .env file with your OpenAI API key.")
    print("   Example:")
    print("     OPENAI_API_KEY=sk-your-api-key-here")
    print()
    sys.exit(1)

# Check for API key
from dotenv import load_dotenv
load_dotenv(env_path)
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("❌ ERROR: OPENAI_API_KEY not found in .env file!")
    print("   Please add: OPENAI_API_KEY=sk-your-api-key-here")
    sys.exit(1)

if api_key == "sk-your-api-key-here":
    print("❌ ERROR: OPENAI_API_KEY is still the placeholder!")
    print("   Please replace with your actual API key from:")
    print("   https://platform.openai.com/api-keys")
    sys.exit(1)

print("✅ Configuration loaded successfully!")
print(f"✅ OpenAI API Key found (length: {len(api_key)} chars)")
print()

# Import and start backend
try:
    import uvicorn
    from backend import app
    
    print("🚀 Starting FastAPI server...")
    print()
    print("📍 API running at: http://localhost:8000")
    print("🏥 Health check:    http://localhost:8000/health")
    print("💬 Chat endpoint:   POST http://localhost:8000/chat")
    print()
    print("📖 Documentation:   http://localhost:8000/docs")
    print()
    print("🌐 To test in browser:")
    print("   1. Open index.html in your browser")
    print("   2. Click the 💬 button (bottom-right)")
    print("   3. Ask any question about the portfolio!")
    print()
    print("⏹️  Press CTRL+C to stop the server")
    print()
    print("─" * 64)
    print()
    
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        log_level="info"
    )
    
except ModuleNotFoundError as e:
    print(f"❌ ERROR: Required module not found: {e}")
    print()
    print("Install dependencies with:")
    print("  pip install -r requirements.txt")
    sys.exit(1)
    
except Exception as e:
    print(f"❌ ERROR: {e}")
    sys.exit(1)
