import requests,os
from secrets import GITHUB_TOKEN, REPO_PATH
from time import sleep
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--name", "-n", type=str, dest="name", required=True)
parser.add_argument("--private", "-p", dest="is_private", action="store_true")
args = parser.parse_args()
repo_name = args.name
is_private = args.is_private
API_URL = "https://api.github.com"


#gets username
headers = {
    "Authorization": "token " + GITHUB_TOKEN,
    "Accept": "application/vnd.github.v3+json"
}

r= requests.get(API_URL+"/user/repos", headers=headers)
Response = r.json()
for obj in Response :
    user_name = obj['owner']['login']

#makes a new repo
if is_private:
    payload = '{"name": "' + repo_name + '", "private": true }'
else:
    payload = '{"name": "' + repo_name + '", "private": false }'

try:
    r= requests.post(API_URL+"/user/repos", data=payload, headers=headers)
    r.raise_for_status()


except requests.exceptions.RequestException as err:
    raise SystemExit(err)

#makes readme.md with project name, commits and pushes to master
try:
    os.chdir(REPO_PATH)
    os.system("mkdir " + repo_name)
    os.chdir(REPO_PATH + "\\" + repo_name)
    os.system("git init")
    os.system("git remote add origin "+ r"https://github.com/" +user_name+ r"/" + repo_name + ".git")
    os.system("echo # " + repo_name + ">> README.md")
    sleep(2)
    os.system("git add .")
    sleep(2)
    os.system('git commit -m "initial commit"')
    sleep(2)
    os.system("git push -u origin master")
except FileExistsError as err:
    raise SystemExit(err)
