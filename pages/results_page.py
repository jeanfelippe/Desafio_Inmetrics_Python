

from browser import Browser

class ResultsPage(Browser):
    def assercao_mensagem(self):
        return self.driver.find_element_by_css_selector('.success').text


    def assercao_email(self):
        return self.driver.find_element_by_css_selector('.errorlist').text
