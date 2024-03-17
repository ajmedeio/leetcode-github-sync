import os


def get_lc_session():
    return os.environ.get("LEETCODE_SESSION", "")


def github_access_token():
    return os.environ.get("GITHUB_ACCESS_TOKEN", "")


def github_app_client_id():
    return os.environ.get("LEETCODE_GITHUB_SYNC_APP_CLIENT_ID", "")