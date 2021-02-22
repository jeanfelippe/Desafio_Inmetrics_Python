from time import sleep

from browser import Browser

class FormPage(Browser):
    def preenche_nome(self,nome):
        self.driver.find_element_by_id('id_first_name').send_keys(nome)

        #sobrenome
    def preenche_sobrenome(self, sobrenome):
        self.driver.find_element_by_id('id_last_name').send_keys(sobrenome)
        sleep(1)

        # apelido
    def preenche_apelido(self, apelido):
        self.driver.find_element_by_id('id_como_gostaria_de_ser_chamado').send_keys(apelido)
        sleep(1)

        # sexo
    def preenche_sexo(self, sexo):
        self.driver.find_element_by_id('id_sexo').send_keys(sexo)
        sleep(1)

        # email
    def preenche_email(self, email):
        self.driver.find_element_by_id('id_username').send_keys(email)
        sleep(1)

        # cargo
    def preenche_idCargo(self, idCargo):
        self.driver.find_element_by_id('id_cargo').send_keys(idCargo)
        sleep(1)

        # editoria
    def preenche_editoria(self, editoria):
        self.driver.find_element_by_id('id_editoria').send_keys(editoria)
        sleep(1)

        # veículo
    def preenche_idVeiculo(self, idVeiculo):
        self.driver.find_element_by_id('id_veiculo').send_keys(idVeiculo)
        sleep(1)

        # país
    def preenche_idPais(self, idPais):
        self.driver.find_element_by_id('id_pais').send_keys(idPais)
        sleep(1)

        # estado
    def preenche_idEstado(self, idEstado):
        self.driver.find_element_by_id('id_estado').send_keys(idEstado)
        sleep(1)

        # cidade
    def preenche_idCidade(self, idCidade):
        self.driver.find_element_by_id('id_cidade').send_keys(idCidade)

        sleep(1)

        # ddd
    def preenche_telefoneDDD(self, telefoneDDD):
        self.driver.find_element_by_id('id_telefone_ddd').send_keys(telefoneDDD)
        sleep(1)

        # telefone
    def preenche_telefone(self, telefone):
        self.driver.find_element_by_id('id_telefone_numero').send_keys(telefone)
        sleep(1)

        # ddd
    def preenche_celularDDD(self, celularDDD):
        self.driver.find_element_by_id('id_celular_ddd').send_keys(celularDDD)
        sleep(1)

        # celular
    def preenche_celular(self, celular):
        self.driver.find_element_by_id('id_celular_numero').send_keys(celular)
        sleep(1)

        # twitter
    def preenche_twitter(self, twitter):
        self.driver.find_element_by_id('id_twitter').send_keys(twitter)
        sleep(1)

        # intagram
    def preenche_instagram(self, instagram):
        self.driver.find_element_by_id('id_instagram').send_keys(instagram)
        sleep(1)

        # senha
    def preenche_senha(self, senha):
        self.driver.find_element_by_id('id_password1').send_keys(senha)
        sleep(1)

        # confsenha
    def preenche_confSenha(self, confSenha):
        self.driver.find_element_by_id('id_password2').send_keys(confSenha)
        sleep(1)

        # termos
    def aceitar_termos(self):
        self.driver.find_element_by_id('id_termos').click()
        sleep(1)

        # releases
    def aceitar_releases(self):
        self.driver.find_element_by_id('id_deseja_receber_releases').click()
        sleep(1)

        # solicitar
    def clicar_cadastro(self):
        self.driver.find_element_by_xpath('//button[text()="SOLICITAR CADASTRO"]').click()
        sleep(5)


    def assercao_mensagem(self):
        self.driver.findElement_by_xpath("//div[@class='success']")
        sleep(5)
        # driver.close()



