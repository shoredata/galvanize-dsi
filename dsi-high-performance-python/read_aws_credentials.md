## Reading AWS credentials into your python program 

It's best practice not to directly write your aws access key 
and/or secret access key into your python programs. In fact, 
you shouldn't do this with any kind of remotely private 
information (database usernames/passwords, api keys, etc.). 
Two ways around this are the following: 

(1) Store the credentials in a file in a folder called `.aws` in your home directory
(2) Store the relevant credential in a .json, in a 
directory/location where you won't push it up to github.
Then read the credential into a variable from that file.  
(3) Store the relevant credential in your .bashrc/.bash_profile 
(which you shouldn't be pushing up to github as it is) as an 
environment variable, and then access that variable 
from your program. 

#### Storing credentials in a file in `~/.aws/`
Get your access key and secret key from the credentials.csv that you downloaded from AWS. (https://console.aws.amazon.com/iam/home?region=us-east-1#/security_credential)

Create a file called `~/.aws/credentials` (on Linux/Mac) or `%USERPROFILE%\.aws\credentials` (on Windows), and insert the following code into it. Replace `ACCESS_KEY` and `SECRET_KEY` with the S3 keys you got from Amazon.
```
[default]
aws_access_key_id = ACCESS_KEY
aws_secret_access_key = SECRET_KEY
```

#### Storing in a json file. 

Write an `aws_access_keys.json` file that looks something like the following.

Important: Normally, you would store secret keys outside of a Git repo. If you
do create this file in a GitHub repo, *immediately* add it to `.gitignore`.

```
{
	"aws_access_key_id": "XXXX", 
	"aws_secret_access_key": "XXXX"
}
```

Then, in Python: 

```python
import json 

with open('/Users/your_username/.secrets/aws_access_keys.json') as f:
	data = json.load(f)
	access_key = data['access-key'] 
	secret_access_key = data['secret-access-key'] 
```

#### Storing in your .bashrc/.bash_profile. 

Place your AWS access and secret access key into your 
`.bashrc` (Linux) or `.bash_profile` (Mac).

```
export AWS_ACCESS_KEY_ID=XXXX
export AWS_SECRET_ACCESS_KEY=XXXX
```

The next time you open a new shell, these environment variables
will be available. Try `env | grep AWS` at the bash prompt.

Then, in Python: 

```python
import os
aws_access_key_id = os.environ['AWS_ACCESS_KEY_ID']
aws_secret_access_key = os.environ['AWS_SECRET_ACCESS_KEY']
```

Note that you will either need to restart your terminal session (close
and reopen the terminal window) for the changes to take effect. Another
option is to type ```source .bash_profile``` (Mac) or ```source .bashrc``` (Linux).




