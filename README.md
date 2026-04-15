# 📄 Pegasus Abstractive Text Summarizer

Transform long-form text into concise, meaningful summaries using state-of-the-art transformer models.

![Python](https://img.shields.io/badge/Python-3.10-blue.svg)
![PyTorch](https://img.shields.io/badge/PyTorch-2.0-orange.svg)
![Transformers](https://img.shields.io/badge/Transformers-4.30-yellow.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

---

## 🧠 Overview

A deep learning–based abstractive text summarization system powered by Google's PEGASUS model. This project takes large bodies of text as input and generates human-like summaries that capture the core meaning instead of simply extracting sentences.

Designed with a modular architecture, this project separates model loading, processing logic, and execution flow — making it scalable, maintainable, and production-ready.

---

## ✨ Core Features

- 🧾 **Abstractive Summarization** — Generates concise summaries by understanding context, not just extracting sentences
- ⚡ **Transformer-Based NLP** — Utilizes PEGASUS, a cutting-edge sequence-to-sequence transformer model
- 🧩 **Modular Architecture** — Clean separation between model (`model.py`), logic (`summarize.py`), and execution (`main.py`)
- 🔁 **Reusable Pipeline** — Easily integrate into web apps, APIs, or other NLP systems
- 📉 **Customizable Output** — Control summary length, quality, and generation parameters
- 🐳 **Docker Support** — Containerized deployment with optimized multi-stage builds
- ✅ **Automated Testing** — Complete test suite with pytest and coverage reporting

---

## 🛠 Technology Stack

| Category | Technology | Role |
|----------|------------|------|
| Language | Python 3.10+ | Core development |
| ML Framework | PyTorch | Model execution |
| NLP Library | HuggingFace Transformers | PEGASUS model integration |
| Tokenization | SentencePiece | Text preprocessing |
| Testing | pytest, pytest-cov | Unit testing & coverage |
| Code Quality | black, flake8 | Formatting & linting |
| Container | Docker, Docker Compose | Deployment & development |

---

## 🧬 How It Works

```
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
```

---

## 📁 Project Structure

```
pegasus_summarizer/
├── .github/
│   └── workflows/
│       └── ci.yml           # GitHub Actions CI/CD
├── tests/
│   ├── __init__.py
│   └── test_summarize.py    # Unit tests
├── .dockerignore            # Docker ignore rules
├── .env.example             # Environment variables template
├── .gitignore               # Git ignore rules
├── Dockerfile               # Multi-stage Docker build
├── docker-compose.yml       # Docker Compose configuration
├── main.py                  # Entry point to run summarization
├── Makefile                 # Build automation
├── model.py                 # Loads PEGASUS model & tokenizer
├── requirements.in          # Production dependencies (source)
├── requirements.txt         # Production dependencies (locked)
├── requirements-dev.in      # Development dependencies (source)
├── requirements-dev.txt     # Development dependencies (locked)
├── summarize.py             # Core summarization logic
├── LICENSE                  # License file
└── README.md                # Project documentation
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or higher
- pip (Python package manager)
- Git
- Docker (optional, for containerized deployment)

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/pegasus-summarizer.git
cd pegasus-summarizer
```

### 2. Create Environment (Recommended)

```bash
# Using conda
conda create -n pegasus python=3.10
conda activate pegasus

# Or using venv
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
# Install production dependencies
make install

# Or install development dependencies (includes production)
make install-dev
```

### 4. Configure Environment Variables

```bash
# Copy the example environment file
cp .env.example .env

# Edit .env with your preferred settings
```

### 5. Run the Project

```bash
python main.py
```

---

## 🐳 Docker Usage

### Build and Run with Docker

```bash
# Build the Docker image
docker build -t pegasus-summarizer .

# Run the container
docker run --rm -v $(pwd)/.cache:/app/.cache pegasus-summarizer
```

### Docker Compose (Recommended for Development)

```bash
# Start the service with Docker Compose
docker-compose up

# Run in detached mode
docker-compose up -d

# Stop the service
docker-compose down

# Rebuild after changes
docker-compose up --build
```

### Docker Volume for Model Caching

The Docker setup uses a volume mount to cache downloaded models:
- Local: `./.cache/huggingface`
- Container: `/app/.cache/huggingface`

This prevents re-downloading the ~2GB model on every container restart.

---

## 🧪 Development

### Running Tests

```bash
# Run all tests with coverage
make test

# Or directly with pytest
pytest tests/ -v --cov=. --cov-report=term-missing --cov-report=html
```

### Code Quality

```bash
# Format code with black
make format

# Run linting with flake8
make lint

# Clean cache files
make clean
```

### Dependency Management

We use `pip-tools` for dependency locking:

```bash
# Compile dependencies (after updating .in files)
make compile-deps

# Upgrade all dependencies
make upgrade-deps
```

---

## 📌 Example

### Input

```
Anusthan Singh is a highly versatile Full-Stack Developer and IoT Innovator
who has built a significant professional footprint through his work in civic
technology and scalable enterprise solutions...
```

### Output

```
Anusthan Singh is a highly versatile Full-Stack Developer and IoT Innovator
who has built a significant professional footprint through his work in civic
technology and scalable enterprise solutions.
```

---

## ⚙️ Configuration

Modify parameters in `summarize.py` or via environment variables:

```python
model.generate(
    max_length=60,      # Maximum summary length
    num_beams=5,        # Beam search width
    early_stopping=True # Stop when model is confident
)
```

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `HF_HOME` | HuggingFace cache directory | `./.cache/huggingface` |
| `MODEL_NAME` | Model identifier | `google/pegasus-xsum` |
| `MAX_LENGTH` | Maximum summary length | `60` |
| `NUM_BEAMS` | Number of beams for search | `5` |
| `LOG_LEVEL` | Logging level | `INFO` |

---

## ⚠️ Notes

- **First run downloads the PEGASUS model (~2GB)** — ensure stable internet and sufficient disk space
- **Recommended Python version: 3.10+**
- **GPU acceleration** — Install `torch` with CUDA support for faster inference
- **Model caching** — Models are cached in `~/.cache/huggingface` by default

---

## 🚀 Future Enhancements

- 🌐 Web interface using Flask or Streamlit
- 📄 PDF / document summarization
- ⚡ REST API using FastAPI
- 📊 Batch summarization support
- 🔄 Model fine-tuning capabilities

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run tests (`make test`)
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Shantanu Bhise**

---

## 🙏 Acknowledgments

- [HuggingFace Transformers](https://huggingface.co/docs/transformers) for the PEGASUS model
- [Google Research](https://github.com/google-research/pegasus) for the original PEGASUS implementation
