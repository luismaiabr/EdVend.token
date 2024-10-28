import requests  
import json  
import hashlib  
import hmac  
from datetime import datetime  
import time  

import requests  

import requests  
TOKEN ='eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6ImEwMTQ5ODU3YmE1NGRlYmVlNDAzODQxMDVmOTUyNzc3NGUyZjA0YWFmYjQxZGYxYzNhZGVmNjhiZDI1YTY5NjJmMGQ0ZDg5YmFmMDJiZWE4In0.eyJhdWQiOiI1ZDc4MDlhOS02Mzc4LTQ2NzMtOTdjZS04MmM3MGRkYWJmZTQiLCJqdGkiOiJhMDE0OTg1N2JhNTRkZWJlZTQwMzg0MTA1Zjk1Mjc3NzRlMmYwNGFhZmI0MWRmMWMzYWRlZjY4YmQyNWE2OTYyZjBkNGQ4OWJhZjAyYmVhOCIsImlhdCI6MTczMDA3MzgzOCwibmJmIjoxNzMwMDczODM4LCJleHAiOjE4NDM0MzA0MDAsInN1YiI6IjExNTA2Mjk1IiwiZ3JhbnRfdHlwZSI6IiIsImFjY291bnRfaWQiOjMzMDg4NDAzLCJiYXNlX2RvbWFpbiI6ImtvbW1vLmNvbSIsInZlcnNpb24iOjIsInNjb3BlcyI6WyJjcm0iLCJmaWxlcyIsImZpbGVzX2RlbGV0ZSIsIm5vdGlmaWNhdGlvbnMiLCJwdXNoX25vdGlmaWNhdGlvbnMiXSwiaGFzaF91dWlkIjoiYjgzNDFhM2QtMjg4NS00ODY2LWI0NjktMGNjMmU2ZjdhMTZlIiwiYXBpX2RvbWFpbiI6ImFwaS1jLmtvbW1vLmNvbSJ9.C2MV9d4i1XO6L0G98V7BgC5Xv5inzzvAXl_tsiNTw_4REjlTmTbvkOXtyqfAT9jjRmwrwjvuQLlLfYs7KRllVRrdasYpNojD2dMLlx1F67OqNrc-dkD5n7S8LL3I34iXi1TQR1ApHEca51BDWwqu1qOrV_5xm8XNXKDFGQmggAMRx48uB2Q2h8Z56Wq4BGDkaN5tOXnjiEdlDOy_cQpg23FrDyhYnSSsGo60lyQPt-z_6PmJQKbvgGLuLbzxA-x7hADqthHKmKMjLuXMc-jAI-Uhvkrg3M8RrXhemd21IsS5SdyTenCxEXRpRHccUP0JuV_YrRdl2TwI_mP2F21-fw'
def send_message(access_token, message_text, recipient_id):  
    """  
    Sends a message to a user using the provided access token, message text, and recipient ID.  
    
    Args:  
        access_token (str): The access token for the messaging platform.  
        message_text (str): The text of the message to be sent.  
        recipient_id (str): The ID of the recipient user.  
    Returns:  
        requests.Response: The response from the messaging platform's API.  
    """  
    url = f"https://api.example.com/v1/messages"  
    headers = {  
        "Authorization": f"Bearer {access_token}",  
        "Content-Type": "application/json"  
    }  
    data = {  
        "recipient": {  
            "id": recipient_id  
        },  
        "message": {  
            "text": message_text  
        }  
    }  
    
    response = requests.post(url, headers=headers, json=data)  
    return response  
if __name__ == "__main__":  
    # Replace these with your actual values  
    response = send_message(TOKEN,'Esta mensagem é um teste feito pelos desenvolvedores do projeto de automação com inteligência artificial','bd6016e5-08a0-4292-b38e-f4c5a5786d0e')
    
    print("Response:", response)  
