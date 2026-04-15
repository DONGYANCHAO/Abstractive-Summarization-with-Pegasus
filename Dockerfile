FROM python:3.10-slim as builder

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir --user -r requirements.txt

FROM python:3.10-slim as runtime

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

COPY --from=builder /root/.local /root/.local
ENV PATH=/root/.local/bin:$PATH

ENV TRANSFORMERS_CACHE=/app/model_cache
ENV HF_HOME=/app/model_cache

COPY model.py .
COPY summarize.py .
COPY main.py .

RUN python -c "from model import tokenizer, model; print('Model cached successfully')"

CMD ["python", "main.py"]
