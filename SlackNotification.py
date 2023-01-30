import json
import requests

class SlackNotification:
    def __init__(self, postId, link, title, totalPrice, webhookUrl):
        self.baseLink = "<https://www.njuskalo.hr"
        self.postId = str(postId)
        self.link = link
        self.title = title
        self.totalPrice = totalPrice
        self.webhookUrl = webhookUrl

    def getLink(self):
        return self.baseLink + self.link + self.postId + "|" + self.title + ">"

    def getNotificationBody(self):
        body = {'text': 'Novi stan!', 'blocks': [{'type': 'section',
                                                  'fields': [{'type': 'mrkdwn',
                                                              'text': self.getLink()},
                                                             {'type': 'mrkdwn',
                                                              'text': self.totalPrice + '€'}]}, ]}
        return body

    def sendNotification(self):

        dataJson = json.dumps(self.getNotificationBody())
        return requests.post(self.webhookUrl, data=dataJson)