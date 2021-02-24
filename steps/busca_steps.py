from behave import given, when, then
from selenium.webdriver.android import webdriver
from utils import Utils
from pages.form_page import FormPage
from pages.results_page import ResultsPage
from selenium import webdriver
from nose.tools import assert_equal
from browser import Browser
from allure_behave.hooks import allure_report
from nose.tools import assert_equal
from selenium.webdriver.common.keys import Keys

utils=Utils()

form_page= FormPage()
results_page=ResultsPage()

#from browser import Browser

#browser= Browser()

@given(u'que acesso o site da Globo')
def step_impl(context):
    utils.navegar('https://homologacao.imprensa.globo.com')


@given(u'clico no botão Novo Cadastro')
def step_impl(context):
    Browser.driver.find_element_by_link_text('Novo Cadastro').click()

@when(u'Preencho o Formulario')
def step_impl(context):
    form_page.preenche_nome('Boomer')
    form_page.preenche_sobrenome('Falkner')
    form_page.preenche_apelido('Boom')
    form_page.preenche_sexo('Masculino')
    form_page.preenche_email('jeanfelippe57@gmail.com')
    form_page.preenche_idCargo('Outros')
    form_page.preenche_editoria('Humor')
    form_page.preenche_idVeiculo('TV')
    form_page.preenche_idPais('Brasil')
    form_page.preenche_idEstado('RJ - Rio de Janeiro')
    form_page.preenche_idCidade('Rio de Janeiro')
    form_page.preenche_telefoneDDD('21')
    form_page.preenche_telefone('39856585')
    form_page.preenche_celularDDD('21')
    form_page.preenche_celular('986380544')
    form_page.preenche_twitter('jean_10')
    form_page.preenche_instagram('jeanfeijan')
    form_page.preenche_senha('31081992@JEANjean')
    form_page.preenche_confSenha('31081992@JEANjean')
    form_page.aceitar_termos()
    form_page.aceitar_releases()

@when(u'Preencho o Formulario com um email existente')
def step_impl(context):
    form_page.preenche_nome('Boomer')
    form_page.preenche_sobrenome('Falkner')
    form_page.preenche_apelido('Boom')
    form_page.preenche_sexo('Masculino')
    form_page.preenche_email('jeanfelippe54@gmail.com')
    form_page.preenche_idCargo('Outros')
    form_page.preenche_editoria('Humor')
    form_page.preenche_idVeiculo('TV')
    form_page.preenche_idPais('Brasil')
    form_page.preenche_idEstado('RJ - Rio de Janeiro')
    form_page.preenche_idCidade('Rio de Janeiro')
    form_page.preenche_telefoneDDD('21')
    form_page.preenche_telefone('39856585')
    form_page.preenche_celularDDD('21')
    form_page.preenche_celular('986380544')
    form_page.preenche_twitter('jean_10')
    form_page.preenche_instagram('jeanfeijan')
    form_page.preenche_senha('31081992@JEANjean')
    form_page.preenche_confSenha('31081992@JEANjean')
    form_page.aceitar_termos()
    form_page.aceitar_releases()

@when(u'Preencho o Formulário com o País como Russia e Estado como Rio de Janeiro')
def step_impl(context):
    form_page.preenche_nome('Boomer')
    form_page.preenche_sobrenome('Falkner')
    form_page.preenche_apelido('Boom')
    form_page.preenche_sexo('Masculino')
    form_page.preenche_email('jeanfelippe80@gmail.com')
    form_page.preenche_idCargo('Outros')
    form_page.preenche_editoria('Humor')
    form_page.preenche_idVeiculo('TV')
    form_page.preenche_idPais('Rússia')
    form_page.preenche_idEstado('RJ - Rio de Janeiro')
    form_page.preenche_idCidade('Rio de Janeiro')
    form_page.preenche_telefoneDDD('21')
    form_page.preenche_telefone('39856585')
    form_page.preenche_celularDDD('21')
    form_page.preenche_celular('986380544')
    form_page.preenche_twitter('jean_10')
    form_page.preenche_instagram('jeanfeijan')
    form_page.preenche_senha('31081992@JEANjean')
    form_page.preenche_confSenha('31081992@JEANjean')
    form_page.aceitar_termos()
    form_page.aceitar_releases()

@then(u'Exibe uma mensagem de erro de cadastro existente')
def step_impl(context):
    assert(results_page.assercao_email(), 'Já existe um cadastro com este e - mail.')



@when(u'Clico no botao solicitar cadastro')
def step_impl(context):
    form_page.clicar_cadastro()


@then(u'Exibe uma nova pagina com uma mensagem de cadastro realizado com sucesso')
def step_impl(context):
    assert(results_page.assercao_mensagem(), 'Seu cadastro foi realizado. Aguarde a revisão e aprovação da sua conta.')



    '''
           coments
    '''