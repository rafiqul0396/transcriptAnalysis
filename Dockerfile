FROM python:latest

WORKDIR /app

COPY requirements.txt .

RUN python -m venv /venv && /venv/bin/pip install --no-cache-dir -r requirements.txt

ENV PATH="/app:/venv/bin:$PATH"

COPY . .

CMD ["streamlit", "run", "app.py"]
