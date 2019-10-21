from locust import HttpLocust, TaskSet

def get_analyze(l):
    l.client.get("random")

class UserBehavior(TaskSet):
    tasks = {get_analyze: 1}

    def on_start(self):
        get_analyze(self)

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000
