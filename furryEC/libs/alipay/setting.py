
APPID = "2021000118646471"

APP_PRIVATE_KEY_STRING = open('pem.txt').read()

ALIPAY_PUBLIC_KEY_STRING = """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAtjzKomhkKhwqn7BvBZEs33vbitq8c5CwGtQyxHJCNCqU9upedMA/KLlN9YaqGyY0Trcl+gnL/3MFWHyXUsnu+a29vgvvVOfuGt5KtIMjiEQdileaqwdVMzoL7jJAJHQ+6lyd+9M1v96egAsc3QLADBt8bg59r9BKFBFNWh5wBVoFFl3gtPQ7VtWyJ0OmhVKWh2rkUGNpHNTUuuJQNx5MeQ/cBRrh38bbg4PfWGBhaZnkjaIW7cokf0ZlS2a9I4lf1sA5YcKsKRergz6Ix5u83bCnH7Gt/8cxQ/GDgp6c95EChoQA6wjNhvv3hqNalwNlnT+HHgN6G084zVQe+ehYpwIDAQAB
-----END PUBLIC KEY-----
"""

SIGN_TYPE = "RSA2"

DEBUG = True

GATEWAY = 'https://openapi.alipaydev.com/gateway.do?' if DEBUG else 'https://openapi.alipay.com/gateway.do?'