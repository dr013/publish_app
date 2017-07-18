# Publish application service

## Variables

|Field name|Description|Required|
|----------|-----------|---------|
|project |Jira code of project in lowercase| True|
|product |System name of product in lowercase|True|
|module_name |Product part - module_name|True|
|version|Git tag for stable releases, Release number for night/test releases|True|
|build_type| One of value from list: [stable,night,test|True|
|custom|Custom folder for different versions (such as os type, same application servers, etc)|False|
artifact |File for save - begin with @, for example artifact=@D:\test.txt |False|

### CURL example:
```
curl -X POST -F "project=core" -F "product=sv" -F "module_name=svweb" -F "version=1.0" -F "build_type=stable" -F "custom=sso_support" -F "artifact=@D:\file" http://127.0.0.1:5000 
```