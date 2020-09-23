FROM python:latest

WORKDIR /usr/local/bin

COPY requirements.txt ./requirements.txt
COPY src/* ./src/
COPY bot/* ./bot/


RUN pip install -r requirements.txt
CMD ["python", "src/FTP_Del.py"]
CMD ["python", "src/FTP_Upload.py"]
