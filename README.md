# 📄 Pegasus Abstractive Text Summarizer

Transform long-form text into concise, meaningful summaries using state-of-the-art transformer models.

**Python • PyTorch • HuggingFace Transformers • NLP**

---

## 🧠 Overview

A deep learning–based abstractive text summarization system powered by Google’s PEGASUS model. This project takes large bodies of text as input and generates human-like summaries that capture the core meaning instead of simply extracting sentences.

Designed with a modular architecture, this project separates model loading, processing logic, and execution flow — making it scalable, maintainable, and production-ready.

---

## ✨ Core Features

- 🧾 **Abstractive Summarization** — Generates concise summaries by understanding context, not just extracting sentences
- ⚡ **Transformer-Based NLP** — Utilizes PEGASUS, a cutting-edge sequence-to-sequence transformer model
- 🧩 **Modular Architecture** — Clean separation between model (model.py), logic (summarize.py), and execution (main.py)
- 🔁 **Reusable Pipeline** — Easily integrate into web apps, APIs, or other NLP systems
- 📉 **Customizable Output** — Control summary length, quality, and generation parameters
- 🐳 **Docker Support** — Containerized deployment with persistent model cache
- ✅ **CI/CD Ready** — GitHub Actions for automated testing and linting
- 🧪 **Full Test Coverage** — Unit tests with mocking to avoid large model downloads

---

## 🛠 Technology Stack

| Category          | Technology                  | Role                              |
|-------------------|-----------------------------|-----------------------------------|
| Language          | Python 3.10+                | Core development                  |
| ML Framework      | PyTorch 2.0+                | Model execution                   |
| NLP Library       | HuggingFace Transformers    | PEGASUS model integration         |
| Tokenization      | SentencePiece               | Text preprocessing                |
| Testing           | pytest + pytest-cov         | Unit testing & coverage           |
| Linting/Formatting| flake8 + black              | Code quality                      |
| Containerization  | Docker + docker-compose     | Deployment                        |
| CI/CD             | GitHub Actions              | Automated testing                 |

---

## 📁 Project Structure

```
pegasus_summarizer/
├── .github/
│   └── workflows/
│       └── ci.yml              # GitHub Actions CI configuration
├── tests/
│   ├── __init__.py
│   ├── conftest.py             # Test fixtures with mocking
│   └── test_summarize.py       # Unit tests for summarize_text
├── main.py                     # Entry point to run summarization
├── model.py                    # Loads PEGASUS model & tokenizer
├── summarize.py                # Core summarization logic
├── requirements.in             # pip-tools source dependencies
├── requirements.txt            # Locked production dependencies
├── requirements-dev.in         # pip-tools source dev dependencies
├── requirements-dev.txt        # Locked development dependencies
├── Makefile                    # Build and development commands
├── .env.example                # Environment variables template
├── .gitignore                  # Git ignore rules
├── .dockerignore               # Docker ignore rules
├── docker-compose.yml          # Docker compose configuration
├── Dockerfile                  # Multi-stage Docker build
└── README.md                   # Project documentation
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or higher
- pip 23.0+
- (Optional) Docker 24.0+ and Docker Compose 2.0+

---

### Option 1: Local Installation

#### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/pegasus-summarizer.git
cd pegasus-summarizer
```

#### 2. Create Virtual Environment

```bash
# Using venv
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows

# OR using conda
conda create -n pegasus python=3.10
conda activate pegasus
```

#### 3. Install Dependencies

```bash
# Production dependencies only
make install

# OR for development (includes pytest, black, flake8, pytest-cov)
make install-dev
```

#### 4. Configure Environment

```bash
cp .env.example .env
# Edit .env to customize model name, cache directory, etc.
```

#### 5. Run the Project

```bash
python main.py
```

> **Note**: First run downloads the PEGASUS model (~2GB) and caches it locally.

---

### Option 2: Docker Installation

#### Build and Run with Docker

```bash
# Build the image
make docker-build

# Run with persistent model cache volume
make docker-run
```

#### Docker Compose (Recommended for Development)

```bash
# Start with docker-compose (includes model cache volume)
make docker-dev
```

#### Key Docker Features:

- **Multi-stage build**: Small final image (~1.5GB vs 5GB base)
- **Persistent cache volume**: Model downloaded once, reused across builds
- **Non-root user**: Security best practices
- **Optimized layers**: Dependencies cached separately from application code

---

## 💻 Development Workflow

### Available Commands (via Makefile)

```bash
make help              # Show all available commands
make install           # Install production dependencies
make install-dev       # Install development dependencies
make test              # Run tests
make test-cov          # Run tests with coverage report
make lint              # Run flake8 linter
make format            # Format code with black
make clean             # Clean temporary files
make docker-build      # Build Docker image
make docker-run        # Run Docker container
make docker-dev        # Run with docker-compose
```

### Code Quality

```bash
# Format code
make format

# Lint code
make lint
```

### Running Tests

```bash
# Run all tests
make test

# Run with coverage report
make test-cov
```

> Tests use `unittest.mock` to completely avoid downloading the 2GB model during testing. All model calls are mocked for fast, reliable tests.

---

## ⚙️ Configuration

Create a `.env` file to customize behavior:

```env
# Model Configuration
MODEL_NAME=google/pegasus-xsum
MODEL_CACHE_DIR=./cache

# Generation Settings
MAX_SUMMARY_LENGTH=60
NUM_BEAMS=5

# Optional: HuggingFace API token for private models
# HUGGINGFACE_HUB_TOKEN=your_token_here
```

### Customizing Generation Parameters

Modify parameters in `summarize.py` for different output styles:

```python
model.generate(
    max_length=80,        # Maximum summary length
    min_length=30,        # Minimum summary length
    num_beams=5,          # Beam search width
    length_penalty=2.0,   # Length regularization
    early_stopping=True
)
```

---

## 🔄 CI/CD Pipeline

The project includes a complete GitHub Actions workflow that runs automatically on every PR and push:

1. **Linting** - flake8 for code quality checks
2. **Formatting** - black code style verification
3. **Testing** - pytest with full test suite
4. **Coverage** - Coverage reports uploaded to Codecov

To enable Codecov:
1. Sign up at [codecov.io](https://codecov.io)
2. Add `CODECOV_TOKEN` to your repository secrets

---

## 📌 Example

**Input:**
```
Anusthan Singh is a highly versatile Full-Stack Developer and IoT Innovator who has built a significant professional footprint through his work in civic technology and scalable enterprise solutions. Currently a student at KIIT University with a strong academic standing, he has successfully bridged the gap between hardware and software by securing a patent for an IoT-based water leakage detection and management system and publishing research in IEEE Xplore regarding resource efficiency in smart greenhouses.
```

**Output:**
```
"An Indian student and developer has made significant contributions to civic technology and secured a patent for an IoT-based water leakage detection system."
```

---

## ⚠️ Notes

- **Model Size**: First run downloads ~2GB, subsequent runs use cache
- **Disk Space**: Ensure sufficient space for model cache (Docker or local)
- **Python Version**: 3.10 is the recommended and tested version
- **RAM**: Minimum 8GB RAM recommended for inference

---

## 🚀 Future Enhancements

- 🌐 Web interface using Flask or Streamlit
- 📄 PDF / Word document summarization
- ⚡ REST API using FastAPI
- 📊 Batch summarization support
- 🐳 Kubernetes deployment manifests
- 📈 Performance benchmarking suite

---

## 📜 License

This project is for educational and development purposes.

---

## 👨‍💻 Author

Shantanu Bhise

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Run tests (`make test-cov`)
4. Ensure lint passes (`make lint && make format`)
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Open a Pull Request
7. Wait for CI pipeline to pass ✅
