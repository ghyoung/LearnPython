#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : ShiMeng
# @File    : send_sms_with_twilio.py
# @Software: PyCharm

from twilio.rest import Client

def send_msm(msg):
    # Your Account SID from twilio.com/console
    account_sid = "ACb8ae32d700520f68c12786c7857b8a6c"
    # Your Auth Token from twilio.com/console
    auth_token  = "00d986ed00a706230cc385d238191c45"

    client = Client(account_sid, auth_token)

    message = client.messages.create(
    to="+8615195879763",
    from_="+19802724919 ",
    body=str(msg))
    message.sid

test = '速度好像不错啊。时效性!'
send_msm(test)
