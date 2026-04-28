FROM python:3.10-slim
RUN apt-get update && apt-get install -y wget gnupg unzip chromium chromium-driver && rm -rf /var/lib/apt/lists/*
ENV CHROME_BIN=/usr/bin/chromium 
ENV CHROMEDRIVER_PATH=/usr/bin/chromedriver
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY api.py DataBase.py hw5.py results.json ./
CMD ["python", "api.py"]