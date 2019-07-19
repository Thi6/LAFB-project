FROM python
ARG VERSION=6
COPY . .
COPY num_gen_${VERSION}.py app.py
RUN pip install flask
RUN pip install requests
EXPOSE 9017
ENTRYPOINT ["python", "app.py"]
