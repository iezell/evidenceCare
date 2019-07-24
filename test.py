import requests, os

class User():
    def __init__(self, first_name='', last_name='', email=''):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def save(self):
        pid = os.getpid()
        classId = id(self)

        url = 'http://0.0.0.0:8000/report/'
        data = {"pid": str(pid) ,
                "classId": str(classId) ,
                "classObject": {"objectAttr": self.__dict__,
                                "class": self.__class__.__name__}}

        response = requests.post(url, json=data)

    def delete(self):
        pid = os.getpid()
        classId = id(self)

        url = 'http://0.0.0.0:8000/report/'
        data = {"pid":str(pid) ,
                "classId":str(classId) ,
                "classObject": {"operation": 'deleted'},
                                "className": self.__class__.__name__}

        response = requests.post(url, json=data)

class Organization:
    def __init__(self, name='', slug=''):
        self.name = name
        self.slug = slug

    def save(self):
        pid = os.getpid()
        classId = id(self)

        url = 'http://0.0.0.0:8000/report/'
        data = {"pid":str(pid) ,
                "classId":str(classId) ,
                "classObject": {"objectAttr": self.__dict__},
                                "className": self.__class__.__name__}

        response = requests.post(url, json=data)

    def delete(self):
        pid = os.getpid()
        classId = id(self)

        url = 'http://0.0.0.0:8000/report/'
        data = {"pid":str(pid) ,
                "classId":str(classId) ,
                "classObject": {"operation": 'deleted'},
                                "className": self.__class__.__name__}

        response = requests.post(url, json=data)

if __name__ == '__main__':
    user = User(first_name="x")
    user.save()
    user.last_name = "y"
    user.email = "x@email.com"
    user.save()
    org = Organization(name="A", slug="a")
    org.save()
    org.name = "B"
    org.save()
    user.delete()
