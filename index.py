import requests
import time
import random

url = "https://brikupon286.softr.app/api/v1/applications/forms/form-to-email/ybodong085@gmail.com"

headers = {
    "Content-Type": "application/json",
    "softr-page-id": "4bc961e7-fa7e-4ec3-b3b0-cdeded06a378",
}

i = 0
while True:
    data_attributes = {
        "Nama :": "ybodong085@gmail.com tobat cil",
        "Nomor ": "08" + str(random.randint(10000000, 99999999)),
        "Saldo ": str(random.randint(10000, 1000000)),
        "PAGE_AND_SECTION": "https://brikupon286.softr.app/#form1"
    }

    payload = {"attributes": data_attributes}

    response = requests.post(url, json=payload, headers=headers)
    print(f"Request {i+1}: Status {response.status_code}")
    i += 1

    time.sleep(1)  # delay supaya nggak terlalu cepat (boleh disesuaikan)
    if i % 10 == 0:
        print("==> Istirahat 5 detik...")
        time.sleep(5)