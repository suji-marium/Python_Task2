"""
import base64
import hmac
import hashlib
import json

class BearerToken:
    def __init__(self, __header, __payload, __signature):
        self.__header = __header
        self.__payload = __payload
        self.__signature = __signature

    def decode_header(self):
        header_bytes = base64.urlsafe_b64decode(self.__header + '==')  # Padding
        decoded_header = header_bytes.decode("utf-8")
        print(f"Decoded header: {decoded_header}")

    def decode_payload(self):
        while len(self.__payload) % 4 != 0:
            self.__payload += '='  # Padding

        payload_bytes = base64.urlsafe_b64decode(self.__payload)
        decoded_payload = payload_bytes.decode("utf-8")
        payload_dict = json.loads(decoded_payload)  # Convert to dictionary

        if 'name' in payload_dict:
            print(f"Name: {payload_dict['name']}")
        else:
            print("Name field not found in payload.")
        print(f"Decoded payload: {payload_dict}")

    def verify_signature(self):
        secret_key = input("Enter the secret key: ")

        message = f"{self.__header}.{self.__payload}"
        res = message.encode('utf-8')

        sign = hmac.new(secret_key.encode('utf-8'), res, hashlib.sha256).digest()
        verification_code = base64.urlsafe_b64encode(sign).decode('utf-8').rstrip('=')

        if self.__signature == verification_code:
            print("Verified Successfully")
            self.decode_header()
            self.decode_payload()
        else:
            print("Verification failed")



__header, __payload, __signature = input("Enter the token: ").split('.')

b = BearerToken(__header, __payload, __signature)
b.verify_signature()

"""

import base64
import hmac
import hashlib
import json


class BearerToken:
    def __init__(self, __header, __payload, __signature):
        self.__header = __header
        self.__payload = __payload
        self.__signature = __signature

    def decode_header(self):
        header_bytes = base64.urlsafe_b64decode(self.__header + '==')  # Padding
        decoded_header = header_bytes.decode("utf-8")
        return decoded_header

    def decode_payload(self):
        while len(self.__payload) % 4 != 0:
            self.__payload += '='  # Padding

        payload_bytes = base64.urlsafe_b64decode(self.__payload)
        decoded_payload = payload_bytes.decode("utf-8")
        payload_dict = json.loads(decoded_payload)  # Convert to dictionary
        return payload_dict

    def verify_signature(self):
        secret_key = input("Enter the secret key: ")

        message = f"{self.__header}.{self.__payload}"
        res = message.encode('utf-8')

        sign = hmac.new(secret_key.encode('utf-8'), res, hashlib.sha256).digest()
        verification_code = base64.urlsafe_b64encode(sign).decode('utf-8').rstrip('=')

        return self.__signature == verification_code





