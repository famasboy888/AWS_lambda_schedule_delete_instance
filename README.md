# AWS Lambda that will terminate EC2 Instance every night time

## 1) We need to create a test EC2 Instances first

## 2) We need to create Role and attach Policies

Permission defined under Policy:

- TerminateInstances (To terminate instances)
- DescribeInstances (To list instances)

<p align="left">
  <img width="80%" height="80%" src="https://github.com/famasboy888/AWS_lambda_schedule_delete_instance/assets/23441168/5b40e692-647d-4c70-80dc-214cc6926073">
</p>

## 3) Create Lambda function

[lambda_function.py](https://raw.githubusercontent.com/famasboy888/AWS_lambda_schedule_delete_instance/main/lambda_function.py)

<p align="left">
  <img width="80%" height="80%" src="https://github.com/famasboy888/AWS_lambda_schedule_delete_instance/assets/23441168/fa5086ca-7ca4-4584-8c9a-210342dea640">
</p>
