from alipay import AliPay
from . import setting

alipay = AliPay(
    appid=setting.APPID,
    app_notify_url=None,  # the default notify path
    app_private_key_string=setting.APP_PRIVATE_KEY_STRING,
    # alipay public key, do not use your own public key!
    alipay_public_key_string=setting.ALIPAY_PUBLIC_KEY_STRING,
    sign_type=setting.SIGN_TYPE,  # RSA or RSA2
    debug=setting.DEBUG  # False by default
)

gateway = setting.GATEWAY
