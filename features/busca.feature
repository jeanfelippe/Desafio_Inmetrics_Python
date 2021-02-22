#language: pt

   Funcionalidade: fluxo de busca

     @cadastro
     Cenário: realizar busca
       Dado que acesso o site da Globo
       E clico no botão Novo Cadastro
       Quando Preencho o Formulario
       E Clico no botao solicitar cadastro
       Então Exibe uma nova pagina com uma mensagem de cadastro realizado com sucesso
