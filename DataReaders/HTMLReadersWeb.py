from urllib.request import urlopen


class WebReader(object):

    # Path = 'http://pythonscraping.com/blog'

    def __init__(self, path):

        self.html = None
        self.path = path

    def open(self):

        self.html = urlopen(self.path)
        print(self.html.read())

    def __len__(self):
        print(len(self.path))

    def main(self):
        self.open()
        self.__len__()


if __name__ == "__main__":
    wObj = WebReader('https://data.gov.in/catalog/data-pertaining-scheduled-tribes-india')
    wObj.main()
