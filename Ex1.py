#EXERCISE 1

import json
import boto3

def lambda_handler(event, context):

    #Link KMS and SecretsManager Clients
    kms_client = boto3.client('kms')
    sm_client = boto3.client('secretsmanager')
    
    #Get all the Keys
    kms_keys = kms_client.list_keys()
    #Find the right Key, in this example I picked the first one
    first_key = kms_keys.get("Keys")[0]
    key_arn = first_key.get("KeyArn")

    #KeyArn and Ciphertext dummy data
    key_arn = 'arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab'
    ciphertext = 'KMS Encrypted String'

    #Decrypt Ciphertext
    response = kms_client.decrypt(
        CiphertextBlob = ciphertext,
        KeyId = key_arn
    )
    #Save it in plaintext
    plaintext = response['Plaintext']

    #Create a secret using decrypted data
    sm_client.create_secret(
        Name = 'DBProdSecret',
        KmsKeyId = key_arn,
        SecretString = plaintext
    )
