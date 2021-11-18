# Exercise 1
# Given a KMS encrypted string, decrypt and write it as a secret in SecretsManager to allow any AWS service to use it.

The first thing that came to my mind when designing this solution, was Lambda functions for two reasons:
  1. Cost optimization: as it is valued positively, a lambda function is the cheapest way to implement this solution that I know.
  This scenario is a quick process that will only run for a few seconds, so a serverless architecture seems to be perfect.
  2. Python: to access both KMS and Secret Manager services though Boto3 SDK.

Once that was defined, I didn't encounter any issues. Hardest part was dealing with the responses and formatting data.

# Exercise 2
# Must deploy a service in ECS with a dummy container with a dummy hello world.

I'm familiar with CloudFormation templates but I've never deployed a service in ECS, so I looked for an example and
I found something really close to what I'm asked to do. Based on that, I modified the code to fullfil the exercise requirements.
Another thing I've never done before is working with containers, but I found a basic Nginx dockerfile to use as a dummy "hello-world".

CLI Command to create the stack: 

aws cloudformation create-stack --stack-name example-deployment --template-body file://./ex2.yml --capabilities CAPABILITY_NAMED_IAM --parameters 'ParameterKey=SubnetID,ParameterValue=subnet-xxxxxxxx'

Regarding to plus points: 

Cost optimization: This item goes a bit against "deployment without outage" as high-availability is more expensive. 
The example uses Fargate and its cost depends on usage, so for this exercise Fargate would be cheaper than an EC2 instance with an EBS volume.

Deployment without outage: What I would change if I want to avoid outages is Clusters DesiredCount to 2 or more.

HTTPS: What I would change if I want a secure connection are SecurityGroup and Container Ports to 443, but that probably implies using an SSL Certificate.
