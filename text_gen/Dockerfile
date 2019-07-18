FROM python
ARG VERSION=2
COPY . .
COPY text_gen_${VERSION}.py app.py
RUN pip install flask
RUN pip install requests
ENTRYPOINT ["python", "app.py"]
