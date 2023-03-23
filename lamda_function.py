
import json
import math
import itertools

def lambda_handler(event, context):
    # Check if there are query string parameters
    if 'queryStringParameters' not in event or event['queryStringParameters'] is None :
        # Return welcome message in an HTTP response
        response = {
            "statusCode": 200,
            "headers": {
                "Content-Type": "text/plain"
            },
            "body": "Welcome to 24 points calculator! Be careful, this will destroy the fun of the game"
        }
    else:
        # Get the query string parameters
        query_params = event.get('queryStringParameters', {})
    
        # Get the list of numbers from the query string parameter 'nums'
        nums_str = query_params.get('nums', '')
        nums = [int(num) for num in nums_str.split(',')]
        if nums.len() == 4:
            answer, calculation = is_24_possible(nums)
            # Return the factors in an HTTP response
            
            if answer:
                response = {
                "statusCode": 200,
                "headers": {
                    "Content-Type": "application/json"
                },
                "body": json.dumps({"calculation": calculation})
                }
           else:
                response = {
                "statusCode": 200,
                "headers": {
                    "Content-Type": "text/plain"
                },
                "body": "Welcome to 24 points calculator! Be careful, this will destroy the fun of the game"
                }
                    
    return response                
                    
def is_24_possible(nums):
    # check if list contains 4 integers
    if len(nums) != 4 or not all(isinstance(num, int) for num in nums):
        return False

    # check if 24 can be obtained
    for a, b, c, d in itertools.permutations(nums):
        for op1, op2, op3 in itertools.product(['+', '-', '*', '/'], repeat=3):
            try:
                expr = f'(({a} {op1} {b}) {op2} {c}) {op3} {d}'
                if eval(expr) == 24:
                    return True, expr
            except ZeroDivisionError:
                pass
    return False, None
