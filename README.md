# aws_cn
This repository is created to track microservice about aws cloud native applications management.

### Setup
 - Clone repo and create virtual environment using `pipenv` or `virtualenv`
 - Install python packages `pip install -r requirements.txt`
 - Configure aws command line tool using `aws configure`
   - for this you need AWS Console Access Key ID and Secrete Access Key
 - Create config file as mentioned below and provide correct path
 - Run the server in terminal using `uvicorn fapi:app --reload` or excecute `run.sh`


### aws_config.json

    {
      "USERNAME": "myname",
      "PASSWORD": "pass",
      "ACCESS_KEY_ID": "12345678",
      "SECRET_ACCESS_KEY": "12345678",
      "CONSOLE_LOGIN_LINK": "example.com"
    }


Please insert required value and store it as `file_name.json`


### Docker Commands
- Build docker image `sudo docker build -t fapi_aws .`
- To run docker image `sudo docker run -itd -p 8181:8181 <image_id>`

