FROM python:3.11
LABEL authors="ash"
COPY app.py .
RUN pip install -r requirements.txt
CMD ["python", "app.py"]