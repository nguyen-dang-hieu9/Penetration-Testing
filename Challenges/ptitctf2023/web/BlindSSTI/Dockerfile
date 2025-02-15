FROM python:3.9

WORKDIR /src
COPY requirements.txt .

RUN pip install -r requirements.txt

COPY src /src

EXPOSE 5555

ENTRYPOINT ["python"]
CMD ["main.py"]
