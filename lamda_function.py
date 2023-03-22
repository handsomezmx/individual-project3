import json
import math

def lambda_handler(event, context):
    # Check if there are query string parameters
    if 'queryStringParameters' not in event or event['queryStringParameters'] is None:
        # Return welcome message in an HTTP response
        response = {
            "statusCode": 200,
            "headers": {
                "Content-Type": "text/plain"
            },
            "body": "you can type in a queryStringParameters to check whether this is a prime number"
        }
    else:
        # Get the number from the URL parameter
        number = int(event['queryStringParameters']['number'])

        # Calculate the prime factors
        answer = is_prime(number)
        if answer:
            response = {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": "this is a prime number"
            }
        else:
            response = {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": "this is not a prime number"
            }
            
        # Return the factors in an HTTP response
        

    return response


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True