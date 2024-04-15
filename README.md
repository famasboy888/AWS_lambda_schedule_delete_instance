# AWS Lambda that will terminate EC2 Instance every night time

## 1) We need to create a test EC2 Instances first
<p align="left">
  <img width="80%" height="80%" src="https://github.com/famasboy888/AWS_lambda_schedule_delete_instance/assets/23441168/2dec5aed-1ea0-46e3-8973-c9964ea3d545">
</p>

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

## 3) Schedule using Amazon EventBridge Scheduler
I set mine to trigger every 6PM Philippine Standard Time.

<p align="left">
  <img width="80%" height="80%" src="https://github.com/famasboy888/AWS_lambda_schedule_delete_instance/assets/23441168/9d9468d7-0d1a-4a46-96b6-32a2ddf9f4f7">
</p>
