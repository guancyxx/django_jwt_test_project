from functools import wraps
from django.core.cache import cache
from django.http import HttpResponseForbidden

def ip_filter(func):
    """
    IP地址过滤器
    """
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        # 获取ip地址
        ip = request.META.get("REMOTE_ADDR")
        # 从redis中获取ip地址
        ip_count = cache.get(ip)
        # 如果ip地址存在，则返回True
        if ip_count:
            return HttpResponseForbidden("IP地址已经被限制")
        # 如果ip地址不存在，则返回False
        else:
            # 如果ip地址不存在，则将ip地址存入redis中
            cache.set(ip, 1, timeout=10)
            return func(request, *args, **kwargs)

    return wrapper