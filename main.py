import requests

r = requests.post('https://hooks.slack.com/services/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', data=open('message.json', 'rb'))
