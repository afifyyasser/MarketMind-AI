FROM python:3.11-slim

WORKDIR /app

# Install requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the code
COPY src ./src
COPY main.py .
COPY .env .

# Create a reports folder
RUN mkdir -p /app/reports

# Run the program
CMD ["python", "main.py"]
