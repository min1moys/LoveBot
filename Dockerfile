FROM python:3.11-slim

# ustawiamy katalog roboczy
WORKDIR /app

# kopiujemy requirements i instalujemy paczki
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# kopiujemy cały projekt
COPY . .

# uruchamiamy bota
CMD ["python", "bot.py"]