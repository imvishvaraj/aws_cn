FROM python:3.9
WORKDIR /code
COPY fapi.py /code
COPY requirements.txt /code/requirements.txt
COPY aws_opcito.json /code/aws_opcito.json
COPY credentials /root/.aws/credentials
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
ENTRYPOINT  ["uvicorn", "fapi:app", "--host", "0.0.0.0", "--port", "8181"]
#CMD ["uvicorn", "demofapi:app", "--host", "0.0.0.0", "--port", "8181"]
