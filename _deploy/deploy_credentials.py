from azure.common.credentials import UserPassCredentials

CREDENTIALS = UserPassCredentials(
    "alex.neuenkirk@alexneuenkirkoutlook.onmicrosoft.com",
    "aZ36454627$"
)

# alex.neuenkirk@alexneuenkirkoutlook.onmicrosoft.com
#OBJECT_ID = 'a7d404a5-e812-4357-899b-2a924d2ed9c8'
#ORG_ROLE = 'Global Admin'

'''
OLD PORTAL
  Active Directory
    Default Directory
      Applications
        ProjectTyto
          Enable Users to Sign On:
            App Id URI:  http://www.contoso.com/ProjectTyto

projecttyto:
  Configure:
    Application is multi-tenant:  NO
    Sign on url:  http://projecttyto.azurewebsites.net
    App Id uri: http://projecttyto.azurewebsites.net
'''

# Project Tyto
SUBSCRIPTION_ID = "91cd8148-679a-49b6-bb4d-c263bc6a11c3"
CLIENT_ID = "ac1267d4-fd2a-4786-a359-bfb3951adfd3"
KEY = "cpLnCTuqsPinwa78bhJJjiGt4YO+ScKVYWG7AjI9iIc="
TENANT_ID = "273585e8-62e4-48e6-88cd-019fcd28e283"
RESOURCE_ID = "/subscriptions/91cd8148-679a-49b6-bb4d-c263bc6a11c3/resourceGroups/Default-Web-WestUS/providers/Microsoft.Web/sites/ProjectTyto"

#import adal
#context = adal.AuthenticationContext('https://login.microsoftonline.com/' + TENANT_ID)
#RESOURCE = "https://management.core.windows.net/"
#auth_token = context.acquire_token_with_client_credentials(
#    RESOURCE,
#    CLIENT_ID,
#    KEY)

#auth_token['access_token'] = auth_token['accessToken']

#from msrest.authentication import BasicTokenAuthentication
#CREDENTIALS = BasicTokenAuthentication(
#    token = {
#        'access_token': auth_token
#    }
#)
