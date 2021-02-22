from browser import Browser

#extend(herança) de browser
class Utils(Browser):
    def navegar(self,url):
        self.driver.get(url)