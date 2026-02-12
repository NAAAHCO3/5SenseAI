FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Comando para rodar o Dashboard de vitrine
CMD ["streamlit", "run", "frontend_demo.py", "--server.port=8501", "--server.address=0.0.0.0"]