from rest_framework.throttling import SimpleRateThrottle


class SMSThrotting(SimpleRateThrottle):
    scope = 'sms'

    def get_cache_key(self, request, view):
        telephone = request.query_params.get('telephone')
        return self.cache_format % {'scope': self.scope, 'ident': telephone}

