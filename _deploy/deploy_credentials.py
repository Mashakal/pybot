from azure.common.credentials import UserPassCredentials

CREDENTIALS = UserPassCredentials(
    "alex.neuenkirk@alexneuenkirkoutlook.onmicrosoft.com",
    "aZ36454627$"
)

SUBSCRIPTION_ID = "91cd8148-679a-49b6-bb4d-c263bc6a11c3"

CLIENT_ID = "ac1267d4-fd2a-4786-a359-bfb3951adfd3"

KEY = "cpLnCTuqsPinwa78bhJJjiGt4YO+ScKVYWG7AjI9iIc="

TENANT_ID = "273585e8-62e4-48e6-88cd-019fcd28e283"

import adal
context = adal.AuthenticationContext('https://login.microsoftonline.com/' + TENANT_ID)
RESOURCE = CLIENT_ID
token = context.acquire_token_with_client_credentials(
    RESOURCE,
    "http://PythonSDK",
    KEY)