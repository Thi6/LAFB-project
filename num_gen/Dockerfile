FROM python
ARG VERSION=8
COPY . .
COPY num_gen_${VERSION}.py app.py
RUN pip install flask
RUN pip install requests
ENTRYPOINT ["python", "app.py"]
