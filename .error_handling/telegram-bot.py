import json 
import requests
import os
import pprint

pp = pprint.PrettyPrinter(indent=4)
TOKEN = os.environ['TELEGRAM_TOKEN']
URL = 'https://api.telegram.org/bot{0}/'.format(TOKEN)
chat_id = os.environ['DEFUALT_CHAT_ID']

def get_url(url):
	response = requests.get(url)
	content = response.content.decode("utf8")
	return content
def get_json_from_url(url):
	content = get_url(url)
	js = json.loads(content)
	return js
def get_updates():
	url = URL + "getUpdates"
	js = get_json_from_url(url)
	return js
def send_message(text, chat_id):
	url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
	get_url(url)
def latest_commit_name():
	out = os.popen('git ls-remote git://github.com/jszakmeister/trac-backlog.git |' \
		'grep refs/heads/master | cut -f 1')
	return out.read().strip('\n')[:7]

#pp.pprint(get_updates())
print(latest_commit_name())
send_message(os.environ, chat_id)