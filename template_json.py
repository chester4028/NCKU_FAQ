#coding:utf-8
class Template_json :
    def __init__(self, sender_id, template_type, text, payload_yes, payload_no):
        self.text= text
        self.payload_yes = payload_yes
        self.payload_no = payload_no
        if template_type == 1 :
            self.template = {
                        "recipient": {
                        "id": sender_id
                        },
                        "message":{
                            "attachment":{
                                    "type":"template",
                                    "payload":{
                                                "template_type":"generic",
                                                "elements":[
                                                        ]
                                                }
                                        }
                                    }
                    }

        if template_type == 2:
            self.template ={
                "recipient":
                {
                    "id": sender_id
                },
                "message":
                {
                    "text": self.text,
                    "quick_replies": [
                        {
                            "content_type": "text",
                            "title": "是",
                            "payload": self.payload_yes
                        },
                        {
                            "content_type": "text",
                            "title": "否",
                            "payload": self.payload_no
                        }
                    ]
                }
            }
        if template_type == 3:
            self.template ={
                "recipient":
                {
                    "id": sender_id
                },
                "message":
                {
                    "text": self.text,
                    "quick_replies": [
                        {
                            "content_type": "text",
                            "title": "好喔",
                            "payload": self.payload_yes
                        },
                        {
                            "content_type": "text",
                            "title": "我剛剛按錯了",
                            "payload": self.payload_no
                        }
                    ]
                }
            }


    def addItem(self, title, image_url, item_url, address):
        bobble={
        "title":title,
        "image_url":image_url,
        "subtitle":address,
        "buttons":[
                    {
                        "type":"web_url",
                        "url":item_url,
                        "title":"View Website"
                    }
            ]
        }

        self.template["message"]["attachment"]["payload"]["elements"].append(bobble)
        return self.template
