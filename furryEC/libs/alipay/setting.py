
APPID = "2021000118646471"

APP_PRIVATE_KEY_STRING = """-----BEGIN RSA PRIVATE KEY-----
MIIEogIBAAKCAQEAmn7DaP7cJg/8LJJ+jNTJkR0pidMoD3z/nlGky5AlmVnblceU0O+Z7iYITfowy3OlWTevvb3dP2t7RQ7Q48FkW5zaCLubR0b5myM/uaq/oJwZUqWYO34sMiV1Q6G+zdwIgh1c0pO0YanEWrt5+X+TaziXprlih9pD6KPSiDvHGVBewFqS+Q/N/qfPTk4YoiCxtzEjxo5sv4Vi2D37866527AQ4LKTs41h9fKrC8cE4mJafBOnyzcl7lpHi1kjC7uF7Uvofx7wkzNKL5ng2W5QsQzzEQHtysIktzVcBOmH7imITYh15NOa2Oi6/HWJE/Jn0CjhqBmbsakPpp+SIKqJ3QIDAQABAoIBAG/ftV81lnNVhfU8y7jtaVzUsjyklFDK4kthsaTap+9pG1JVqNS3fE7waXkV3/mjr6twYKlUcH85NJVoSily5FpWtag3OhUeNyd5Ge83zvXds5SeZyNFlXlmmIi1+nYVjG+0FYBDBw7loVNWiNf74uN0opRPkCLyEdTHtG+EYgNYhtwALwzwJdEQi1JJvQ0EbLPyPtWDQ6CX9FUVXcewiZY8/f2VFbIFBHeTb/lwWs67IIbpA+pVISlYBsy+1t184ZrRT+hw7cm0yGTgPHJIzUTVd4ZYKoFQKYDMKAcUUDupM2LpofY2WJhYw68e9E4i9ZiSvrb7ROyJQ2Mm6lK3LsECgYEA3aoV2wAlH0H8EErcAdv6uEX9CKpvYtCZF6si0gee7IHPU6UlURncLH1IGf1HB3i2TF9MEUXPinkQfpFtK0Qwdq1iHJb/d5ipuQEwgNePgQfWvSjwfUa4uuECWXUIjH5P4+1AXdkAa5pcCsGVH+/tJYsas0yKGTiEMKQCzUIHAI0CgYEAsm0jkIy596rk//DbO+N1beupPtwL6kDEufh/HzbJvR7kksajtcDNiDItwSG+yMYw6U54Mz3SRGgoR6n5U5AMJADdTf4z8sTfCOZtCTsaZ7EuPx8AIp5hE/8cpVzJe5BWiZIoYZU5Ev7pD6rl1GmS7qune1TKbseLaxPtN8hCopECgYBmimDz31xM2mxtaQPfhFC2YAIOuTEvyAmaDlvcRxQ4mlA7hID/xHO6zPXGuAjcpvXF3KvGrcG1cA22TzXuNuwoakqhqSRiwed5otg6Mf27ldG7za16dnXMVXyNv3sF6wSwDreg8lqkbFK50xVWIdpVbMUcPoL/6coU6jo1k57DnQKBgFLhE0YPuEps3VZtoMhezaszbjg+qmIzl63y2cm7/1WTxgTPtDe2yUHcXRh6/k3wkcOtqXPT4ZnY7+zp7WB9ZsZKiIGz9JluDVPrBPbmt0s3KA417jAmdV1+gOXnBcgZsbjRZWR+ljZWphebAIr8Rz4KCg/lwOpYUlB4vxXMNfehAoGAAMT7XwO+SJ3Vlljvx9WzHFCzq3En5PFJOKJ9jsZFvj4IhL+5r/pQzZRW8V1EPE4/DUHXc5RdtMDtR5dVYP5+PoSFwUQnXl+jYd5gHxFFq/Q8asvqN+ZpwqbB6yZkpq+t4rS90Xp/IfPHv6ypJP6JMMfNm3em6l7gvcxzDgN8EP4=
-----END RSA PRIVATE KEY-----
"""

ALIPAY_PUBLIC_KEY_STRING = """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAtjzKomhkKhwqn7BvBZEs33vbitq8c5CwGtQyxHJCNCqU9upedMA/KLlN9YaqGyY0Trcl+gnL/3MFWHyXUsnu+a29vgvvVOfuGt5KtIMjiEQdileaqwdVMzoL7jJAJHQ+6lyd+9M1v96egAsc3QLADBt8bg59r9BKFBFNWh5wBVoFFl3gtPQ7VtWyJ0OmhVKWh2rkUGNpHNTUuuJQNx5MeQ/cBRrh38bbg4PfWGBhaZnkjaIW7cokf0ZlS2a9I4lf1sA5YcKsKRergz6Ix5u83bCnH7Gt/8cxQ/GDgp6c95EChoQA6wjNhvv3hqNalwNlnT+HHgN6G084zVQe+ehYpwIDAQAB
-----END PUBLIC KEY-----
"""

SIGN_TYPE = "RSA2"

DEBUG = True

GATEWAY = 'https://openapi.alipaydev.com/gateway.do?' if DEBUG else 'https://openapi.alipay.com/gateway.do?'