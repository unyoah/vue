from rest_framework.throttling import SimpleRateThrottle


class SendMessageRate(SimpleRateThrottle):
    scope = "anon"

    def get_cache_key(self, request, view):
        phone = request.query_params.get("phone")
        if not phone:
            return None
        return phone
