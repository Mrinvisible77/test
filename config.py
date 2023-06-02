import os

API_ID = int(os.environ.get("API_ID", 8006372))

API_HASH = os.environ.get("API_HASH", "f878ef2fd1044167b7d8ab23320e1eda")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "5536158812:AAGV8OznAyDTfw0OYLGJXU_T3B0CneU9QKk")

PASS_DB = int(os.environ.get("PASS_DB", "100"))

OWNER = int(os.environ.get("OWNER", 5604657476))

try:

    ADMINS=[]

    for x in (os.environ.get("ADMINS", "5604657476 5626605198 6230767081").split()):

        ADMINS.append(int(x))

except ValueError:

        raise Exception("Your Admins list does not contain valid integers.")

ADMINS.append(OWNER)
