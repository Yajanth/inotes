FROM python:3.10-slim

WORKDIR .

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 80

CMD [ "source" ,"env/bin/activate" ]
CMD ["uvicorn", "index:app", "--host", "0.0.0.0", "--port", "80"]
