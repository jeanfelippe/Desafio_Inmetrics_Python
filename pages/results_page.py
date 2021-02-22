

from browser import Browser

class ResultsPage(Browser):


        def clicar_cadastro(self):
            self.driver.find_element_by_xpath('//button[text()="SOLICITAR CADASTRO"]').click()
            #sleep(5)