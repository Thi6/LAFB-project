FROM python:alpine
RUN pip install flask
COPY app.py .
COPY prizes.txt .
EXPOSE 9000
ENTRYPOINT ["python", "app.py"]
