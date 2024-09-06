import base64
import hmac
import hashlib

class BearerToken:
    def __init__(self,__header,__payload,__signature):
        self.__header=__header
        self.__payload=__payload
        self.__signature=__signature

    def decode_header(self):
        header_bytes = base64.b64decode(self.__header)
        decoded_header = header_bytes.decode("utf-8")

        print(f"Decoded header: {decoded_header}")

    def decode_payload(self):
        print(type(self.__payload))
        print(len(self.__payload))
        
        while len(self.__payload)%4!=0:
            self.__payload+='='

        
        payload_string_bytes = base64.b64decode(self.__payload)
        decoded_payload = payload_string_bytes.decode("utf-8")

        print(f"Decoded payload: {decoded_payload}")

    def verify_signature(self):
        secret_key=input("Enter the secret key: ")

        message=self.__header +'.'+self.__payload
        res=message.encode('ascii')

        sign=hmac.new(secret_key.encode('utf-8'),res,hashlib.sha256).digest()
        verification_code = base64.urlsafe_b64encode(sign).decode('utf-8').rstrip('=')

        if self.__signature==verification_code:
            print("Verified Successfully")
            BearerToken.decode_header(self)
            BearerToken.decode_payload(self)
        else: 
            print("Verification failed")
            
        

__header,__payload,__signature=input("Enter the token: ").split('.')

b=BearerToken(__header,__payload,__signature)
b.verify_signature()

