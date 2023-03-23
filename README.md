# individual-project3
In this project, I build a 24 points calculator as a lamda function and deploy it on aws.

Through a Api Gateway, I can trigger the lamda function only when the function is needed.

https://j9qkifw79j.execute-api.us-east-1.amazonaws.com/default/proj3

# Usage
you can pass in the parameter through queryStringParameters.
eg:https://j9qkifw79j.execute-api.us-east-1.amazonaws.com/default/proj3?nums=2,4,6,8
The answer should be yes and 2*6+4+8

# Reference
My friend Kate Feng came up with the idea and taught me how to trigger a Lamda function with api gateway.

