# GitHubAPIProjectInitAutomation

### Get project
```bash
git clone "https://github.com/tkacha201/GitHubAPIProjectInitAutomation.git"
cd GitHubAPIProjectInitAutomation
```


### Modules used, may need to install with pip
```python
pip install <modulo_name>

import requests,os
from secrets import GITHUB_TOKEN, REPO_PATH
from time import sleep
import argparse
```


### SETUP 
```python
In secrets.py provide a github generated token.
In secrets.py provide a path to your projects folder.
```

### Usage:
```python
To run the script from cmd add folder to environment variables for windows.
In cmd, create_repo_api.py --name <your_project_name> --priavate (if you want a private repo)
Alternatively, run the script from PyCharm or VisualStudio code.
```
