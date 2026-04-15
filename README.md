📄 Pegasus Abstractive Text Summarizer

Transform long-form text into concise, meaningful summaries using state-of-the-art transformer models.

Python • PyTorch • HuggingFace Transformers • NLP

🧠 Overview

A deep learning–based abstractive text summarization system powered by Google's PEGASUS model. This project takes large bodies of text as input and generates human-like summaries that capture the core meaning instead of simply extracting sentences.

Designed with a modular architecture, this project separates model loading, processing logic, and execution flow — making it scalable, maintainable, and production-ready.

✨ Core Features

🧾 Abstractive Summarization — Generates concise summaries by understanding context, not just extracting sentences

⚡ Transformer-Based NLP — Utilizes PEGASUS, a cutting-edge sequence-to-sequence transformer model

🧩 Modular Architecture — Clean separation between model (model.py), logic (summarize.py), and execution (main.py)

🔁 Reusable Pipeline — Easily integrate into web apps, APIs, or other NLP systems

📉 Customizable Output — Control summary length, quality, and generation parameters

🛠 Technology Stack
Category	Technology	Role
Language	Python	Core development
ML Framework	PyTorch	Model execution
NLP Library	HuggingFace Transformers	PEGASUS model integration
Tokenization	SentencePiece	Text preprocessing

🧬 How It Works
Input Text
   │
   ▼
Tokenizer (PEGASUS)
   │
   ▼
Transformer Model (PEGASUS)
   │
   ▼
Generated Token IDs
   │
   ▼
Decoded Summary Output

📁 Project Structure
pegasus_summarizer/
├── main.py                 # Entry point to run summarization
├── model.py                # Loads PEGASUS model & tokenizer
├── summarize.py            # Core summarization logic
├── requirements.txt        # Production dependencies
├── requirements-dev.txt    # Development dependencies
├── requirements.in         # pip-tools source file
├── requirements-dev.in     # pip-tools dev source file
├── Makefile                # Build and development commands
├── Dockerfile              # Multi-stage Docker build
├── docker-compose.yml      # Docker Compose configuration
├── .dockerignore           # Docker ignore patterns
├── .env.example            # Environment variables template
├── setup.cfg               # Project configuration
├── pytest.ini              # Pytest configuration
├── tests/                  # Test suite
│   ├── __init__.py
│   ├── test_summarize.py
│   ├── test_model.py
│   └── test_main.py
├── .github/
│   └── workflows/
│       └── ci.yml          # GitHub Actions CI/CD
└── README.md               # Project documentation

🚀 Getting Started

Prerequisites
- Python 3.10 or higher
- pip package manager
- (Optional) Docker for containerized deployment

1. Clone the Repository
git clone https://github.com/YOUR_USERNAME/pegasus-summarizer.git
cd pegasus-summarizer

2. Create Virtual Environment
python -m venv venv

On Windows:
venv\Scripts\activate

On Linux/macOS:
source venv/bin/activate

3. Install Dependencies

Production only:
pip install -r requirements.txt

With development tools:
pip install -r requirements-dev.txt

Or using Makefile:
make install-dev

4. Configure Environment (Optional)
cp .env.example .env

Edit .env to customize:
MODEL_NAME=google/pegasus-xsum
MODEL_CACHE_DIR=./model_cache
MAX_LENGTH=60
NUM_BEAMS=5

5. Run the Project
python main.py

📌 Example
Input

A long paragraph about Python programming...

Output

"Python is a high-level programming language known for its readability and widespread use."

⚙️ Configuration

Modify parameters in summarize.py:

model.generate(
    max_length=80,
    min_length=30,
    num_beams=5,
    length_penalty=2.0
)

🐳 Docker Support

Build Docker Image
docker build -t pegasus-summarizer .

Run Container
docker run --rm pegasus-summarizer

Using Docker Compose
docker-compose up

The Docker image uses multi-stage builds to minimize size and caches the model during build to avoid re-downloading ~2GB on each run.

Volume Mounts (docker-compose.yml)
- model_cache: Persists downloaded models
- ./input: Mount input files (read-only)
- ./output: Mount output directory

🔧 Development Commands

Using Makefile:
make help          # Show available commands
make install       # Install production dependencies
make install-dev   # Install development dependencies
make test          # Run tests with coverage
make lint          # Run flake8 linter
make format        # Format code with black
make clean         # Clean cache files
make docker-build  # Build Docker image
make docker-run    # Run Docker container

🧪 Testing

Run Tests
pytest tests/ -v

Run with Coverage
pytest tests/ -v --cov=. --cov-report=term-missing --cov-report=html

Coverage Report
After running tests with coverage, open htmlcov/index.html in your browser for a detailed coverage report.

Test Structure
- test_summarize.py: Tests for summarize_text function
- test_model.py: Tests for model loading
- test_main.py: Tests for main entry point

All tests use unittest.mock to avoid downloading the large model during testing.

🔄 CI/CD Pipeline

GitHub Actions workflow automatically runs on:
- Push to main or develop branches
- Pull requests to main or develop branches

Pipeline includes:
1. Linting with flake8
2. Format checking with black
3. Running tests with pytest
4. Coverage reporting to Codecov
5. Docker image build verification

📦 Dependency Management

Using pip-tools (Optional)

Install pip-tools:
pip install pip-tools

Compile requirements:
pip-compile requirements.in -o requirements.txt
pip-compile requirements-dev.in -o requirements-dev.txt

Sync dependencies:
pip-sync requirements.txt requirements-dev.txt

⚠️ Notes
- First run downloads the PEGASUS model (~2GB)
- Requires stable internet and sufficient disk space
- Recommended Python version: 3.10+
- Tests use mocks to avoid downloading models

🚀 Future Enhancements
- 🌐 Web interface using Flask or Streamlit
- 📄 PDF / document summarization
- ⚡ REST API using FastAPI
- 📊 Batch summarization support
- 🔐 API key authentication

📜 License

This project is for educational and development purposes.

👨‍💻 Author

Shantanu Bhise

🤝 Contributing

1. Fork the repository
2. Create a feature branch (git checkout -b feature/amazing-feature)
3. Commit your changes (git commit -m 'Add amazing feature')
4. Push to the branch (git push origin feature/amazing-feature)
5. Open a Pull Request

Please ensure all tests pass and code is formatted with black before submitting.
