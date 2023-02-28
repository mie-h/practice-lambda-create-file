import json

def lambda_handler(event, context):
    with open('/tmp/output.txt', 'w') as f:
        f.write("Hello World")

    with open('/tmp/output.txt', 'r') as f:
        print(f.read())