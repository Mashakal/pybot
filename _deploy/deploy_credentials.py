#from azure.common.credentials import UserPassCredentials

#CREDENTIALS = UserPassCredentials(
#    "alex.neuenkirk@alexneuenkirkoutlook.onmicrosoft.com",
#    "aZ36454627$"
#)


# Project Tyto
SUBSCRIPTION_ID = "91cd8148-679a-49b6-bb4d-c263bc6a11c3"
CLIENT_ID = "ac1267d4-fd2a-4786-a359-bfb3951adfd3"
KEY = "cpLnCTuqsPinwa78bhJJjiGt4YO+ScKVYWG7AjI9iIc="
TENANT_ID = "273585e8-62e4-48e6-88cd-019fcd28e283"  # Is this correct?
RESOURCE_ID = "/subscriptions/91cd8148-679a-49b6-bb4d-c263bc6a11c3/resourceGroups/Default-Web-WestUS/providers/Microsoft.Web/sites/ProjectTyto"

import adal
context = adal.AuthenticationContext('https://login.microsoftonline.com/' + TENANT_ID)
RESOURCE = "https://management.core.windows.net/"
auth_token = context.acquire_token_with_client_credentials(
    RESOURCE,
    CLIENT_ID,
    KEY)

#auth_token['access_token'] = auth_token['accessToken']

from msrest.authentication import BasicTokenAuthentication
CREDENTIALS = BasicTokenAuthentication(
    token = {
        'access_token': auth_token
    }
)

#for k, v in auth_token.items():
#    print("%s - %s" % (k, v))