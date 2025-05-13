# users/middleware.py
from django.http import HttpResponseForbidden
from ipaddress import ip_address, ip_network

class IPWhitelistMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.allowed_ips = os.getenv("IP_WHITELIST", "192.168.1.0/24").split(",")

    def __call__(self, request):
        ip = request.META.get('REMOTE_ADDR')
        for network in self.allowed_ips:
            if ip_address(ip) in ip_network(network.strip()):
                return self.get_response(request)
        return HttpResponseForbidden("Access Denied")
