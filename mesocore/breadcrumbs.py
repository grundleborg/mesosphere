class Breadcrumb:
    def __init__(self, name, url=""):
        self.name=name
        if url:
            self.url=url

    def __str__(self):
        return self.name


