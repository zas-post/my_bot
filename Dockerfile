FROM python:3.10-alpine3.20
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["/bin/sh", "-c", "python main.py"]
