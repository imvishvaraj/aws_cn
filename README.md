# aws_cn
This repository is created to track microservice about aws cloud native applications management.

Before you start running project.
You need to setup `aws configure` and provide AWS Access Key ID, AWS Secret Access Key.

Then you need to update config file path and it's values as below format.

aws_config.json

`
{
  "USERNAME": "myname",
  "PASSWORD": "pass",
  "ACCESS_KEY_ID": "12345678",
  "SECRET_ACCESS_KEY": "12345678",
  "CONSOLE_LOGIN_LINK": "example.com"
}
`

Please insert required value and store it as `file_name.json`


To run server you can just execute `run.sh` file.

