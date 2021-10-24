import boto3

"""
Using AWS SES to send the confirmation Email.(Custom template)

"""


def get_credential_info():
    with open('C:/Users/ugowu/Desktop/rob.txt', 'r') as f:
        return f.read().split('***')


def send(ToAddresses, Sub_Data, code):
    info_list = get_credential_info()
    print(info_list)
    aws_access_key_id = info_list[0]
    aws_secret_access_key = info_list[1]
    source_mail = info_list[2]
    print(aws_secret_access_key, type(aws_secret_access_key))

    client = boto3.client('ses',
                          aws_access_key_id=aws_access_key_id,
                          aws_secret_access_key=aws_secret_access_key,
                          region_name='ap-northeast-1'
                          )

    return client.send_email(
        Source=source_mail,
        Destination={
            'ToAddresses': [
                ToAddresses,
            ]
        },
        Message={
            'Subject': {
                'Data': Sub_Data,
                'Charset': 'UTF-8'
            },
            'Body': {
                'Text': {
                    'Data': f'Your confirmation code is {code}',
                    'Charset': 'UTF-8'
                }
            }
        }
    )


def get_code():
    import random
    s_code = ''
    for i in range(4):
        s_code += str(random.randint(0, 9))
    return s_code
