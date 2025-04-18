FROM python:3.10

WORKDIR /app

COPY app.py model.joblib requirements.txt ./
RUN pip install -r requirements.txt

EXPOSE 5000
CMD ["python", "app.py"]