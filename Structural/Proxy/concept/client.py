from service_cache_proxy import ServiceCacheProxy
from service_protection_proxy import ServiceProtectionProxy

cache_service = ServiceCacheProxy()
print(cache_service.request())
print(cache_service.request())

proxy_service = ServiceProtectionProxy()
print(proxy_service.request())
print(proxy_service.request())
print(proxy_service.request())
print(proxy_service.request())
