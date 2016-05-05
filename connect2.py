

import time
import os
from slackclient import SlackClient

''' change token below to activate'''

class Connection:
    dict = {}
    sc  =  None
    summ = None
    names = {}
    def read(self,token):
        self.sc = SlackClient(token)
        if self.sc.rtm_connect():
            start = time.time()
            while True:
                try:
                    str = self.sc.rtm_read()
                    if str and ('text' in str[0]) and  ('reply_to' not in str[0]): # if str is not null
                        key = str[0].get('text')
                        user = str[0].get('user')
                        info = self.sc.api_call('users.info', user= user)
                        if user not in self.dict:
                            user_name = info.get('user').get('name')
                            self.names[user_name] = user
                            self.dict[user] = []
                            self.dict[user].append(float(key))
                            self.dict[user].append(1)
                            self.dict[user].append(float(key))
                            print(float(key))
                        else:
                            self.dict[user][0] += float(key)
                            self.dict[user][1] += 1
                            print(float(self.dict[user][0])/self.dict[user][1])
                            self.dict[user][2] = self.dict[user][0]/self.dict[user][1]
                        count , avg = 0,0
                        for key, value in self.dict.items():
                            avg += float(self.dict[key][0])
                            count += self.dict[key][1]
                        self.summ = avg/count
                        time.sleep(1)
                        end = time.time()
                        if(end - start >= 60):
                            start = time.time()
                            for key, value in self.dict.items():
                                avg += float(self.dict[key][0])
                                count += self.dict[key][1]
                            str = "{:.9f}".format(avg/count)
                            self.sc.rtm_send_message("general", str)
                            count , avg = 0,0
                    else:
                        time.sleep(1)
                except Exception as e:
                    print("Exception: ", e.message)


myapp = Connection()
token = "xoxb-39523974961-TdITiQnxagO1vBcLmfZ47VjC"
myapp.read(token)








                        
        
        
    
    







