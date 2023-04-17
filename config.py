import os

from dotenv import load_dotenv


def get_config():

    load_dotenv()

    bucket_name = os.getenv("BUCKET_NAME")
    json_svc_account = os.getenv("SERVICE_ACCOUNT_JSON_MINI")
    port = int(os.getenv("PORT"))

    assert json_svc_account.strip() != "" and json_svc_account is not None
    assert bucket_name != ""

    return {
        "bucket_name": bucket_name,
        "json_svc_account": json_svc_account,
        "port": port
    }
