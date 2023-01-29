class SlackNotification:
    def __init__(self, postId, link, title, channelId, totalPrice, webhookUrl):
        self.baseLink = "<https://www.njuskalo.hr"
        self.postId = str(postId)
        self.link = link
        self.title = title
        self.channelId = channelId
        self.totalPrice = totalPrice
        self.webhookUrl = webhookUrl

    def getLink(self):
        return self.baseLink + self.link + self.postId + "|" + self.title + ">"

    def getNotificationBody(self):
        body = {'channel': self.channelId, 'text': 'Novi stan!', 'blocks': [{'type': 'section',
                                                                         'fields': [{'type': 'mrkdwn', 'text': self.getLink()},
                                                                                    {'type': 'mrkdwn',
                                                                                     'text': self.totalPrice}]}, ]}
        return body

    def sendNotification(self):
        import json
        import requests
        dataJson = json.dumps(self.getNotificationBody())
        requests.post(self.webhookUrl, data=dataJson)
        #test if repsonse is ok and return something