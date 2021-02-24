#language: pt

   Funcionalidade: fluxo de busca

     @cadastro
     Cenário: realizar cadastro
       Dado que acesso o site da Globo
       E clico no botão Novo Cadastro
       Quando Preencho o Formulario
       E Clico no botao solicitar cadastro
       Então Exibe uma nova pagina com uma mensagem de cadastro realizado com sucesso


       @email
       Cenário: realizar cadastro c/ email existente
         Dado que acesso o site da Globo
         E clico no botão Novo Cadastro
         Quando Preencho o Formulario com um email existente
         E Clico no botao solicitar cadastro
         Então Exibe uma mensagem de erro de cadastro existente



      @paisincorreto
       Cenário: realizar cadastro com um País que não corresponde com o Estado
         Dado que acesso o site da Globo
         E clico no botão Novo Cadastro
         Quando Preencho o Formulário com o País como Russia e Estado como Rio de Janeiro
         E Clico no botao solicitar cadastro
         Então Exibe uma nova pagina com uma mensagem de cadastro realizado com sucesso


