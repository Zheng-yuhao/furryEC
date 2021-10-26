from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

class APIResponse(Response):
    def __init__(self, code=100, msg='Success', result=None, status=None,
                 headers=None, content_type=None, **kwargs):
        dic = {
            'code': code,
            'msg': msg,

        }

        if result:
            dic['result'] = result
        dic.update(kwargs)
        super().__init__(data=dic, status=status, headers=headers, content_type=content_type)
# ↑这样写的话, 自己自定义的一些字段作为Response下data字段, 其余都继承了Response
