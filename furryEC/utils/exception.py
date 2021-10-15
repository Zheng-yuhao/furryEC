from rest_framework.views import exception_handler
from furryEC.utils.response import APIResponse
from .logger import log


def common_exception_handler(exc, context):
    print('我是exception下的', context)
    # 可以捕获view的异常 -> 具体看看context里面有什么, 可以取出来的不一定只有view
    log.error(msg=f'view:{context["view"].__class__.__name__}, has error: {str(exc)}')
    ret = exception_handler(exc, context)
    # ↓ 如果drf处理不了的结果都在下面自定
    if not ret:
        if isinstance(exc, KeyError):
            return APIResponse(code=0, msg='error', result=str(exc))
        return APIResponse(code=0, msg='error', result=str(exc))
    else:
        # ↓ 如果drf能够自己处理就返回以下ret.data源码中因为实例化了Response所以能够调用data属性
        return APIResponse(code=0, msg='error', result=ret.data)
