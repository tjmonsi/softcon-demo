from locust import HttpLocust, TaskSet

token = 'Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjhhNjNmZTcxZTUzMDY3NTI0Y2JiYzZhM2E1ODQ2M2IzODY0YzA3ODciLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL2FjY291bnRzLmdvb2dsZS5jb20iLCJhenAiOiIzMjU1NTk0MDU1OS5hcHBzLmdvb2dsZXVzZXJjb250ZW50LmNvbSIsImF1ZCI6IjMyNTU1OTQwNTU5LmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwic3ViIjoiMTExNTYxNTg2MzY3NzQ0MDI2NDYxIiwiaGQiOiJzZW50aS5jb20ucGgiLCJlbWFpbCI6InRqa3Btb25zZXJyYXRAc2VudGkuY29tLnBoIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsImF0X2hhc2giOiJncXptY1p2MFpYVFZsb2NxWGx5VC1nIiwiaWF0IjoxNTcxNzE4MzY3LCJleHAiOjE1NzE3MjE5Njd9.sI27Zyg4ntlH9c4HYaEkWax0xHmsjkw2l_U7SD55QesRmm2Hpbz04D8KpBt5s0Ef5huQqeb9HHGfjL14AsM-J05Qvsd1mR4jOarJOaNs8LLQraaa0EfFyftbnkJSuiZ0IM6_IQd7iYxZEd6FDd4LbUcIj0_VykPbO1poudN368odzjiLqF5BEZal_CNqK8Nm9lupwEZ3zaqZiAJxbI0vvSFfSeH2QfH5hYHVo6teLQ_mXnmUxBa-cHWPRGv5ldiZXT7eWjdFD7zgEHsm7XFpaF592_pDaVPWD9W8EU8MS1FbDSAcXIx1seDGO14TXUPnFMREsgVTRsFGpkeJxuSRZg'

def get_analyze(l):
    l.client.get("random", headers={'Authorization': token})

class UserBehavior(TaskSet):
    tasks = {get_analyze: 1}

    def on_start(self):
        get_analyze(self)

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000
