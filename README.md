# Exercise 1
Given a KMS encrypted string, decrypt and write it as a secret in SecretsManager to allow any AWS service to use it.

The first thing that came to my mind when designing this solution, was Lambda functions for two reasons:
  1. Cost optimization: as it is valued positively, a lambda function is the cheapest way to implement this solution that I know.
  This scenario is a quick process that will only run for a few seconds, so a serverless architecture seems to be perfect.
  2. Python: to access both KMS and Secret Manager services though Boto3 SDK.

Once that was defined, I didn't encounter any issues. Hardest part was dealing with the responses and formatting data.

# Exercise 2
Must deploy a service in ECS with a dummy container with a dummy hello world.

