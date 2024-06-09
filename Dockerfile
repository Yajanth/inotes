FROM python:3.10-slim

WORKDIR .

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["uvicorn", "index:app", "--host", "0.0.0.0", "--port", "80"]
