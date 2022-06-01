FROM python:3.9
WORKDIR /code
COPY . /code
#COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
CMD ["uvicorn", "fapi:app", "--host", "0.0.0.0", "--port", "81"]