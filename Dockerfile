FROM python:3.8-slim

WORKDIR /app

COPY app/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8501

ENV NAME AI-Malaria-Detection

# Run the application
CMD ["python", "app/main.py"]

# TODO: Add any additional dependencies
# TODO: Configure the container to run tests 