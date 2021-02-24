
# [Desafio_Globo_01]
Desafio Automação de Testes Utilizando  Python e BDD em um formulário, entregando no final um relatório detalhado de cada passo dentro do cenário proposto.


# [Frameworks]:
_PyCharm 2020.3.3

_Selenium

_Behave

_Allure

# [Conceitos/Metodologia]:
_PageObjects;

_CleanCode;

_BDD;

_Reports;

# Para executar o Teste, Utilize no Terminal:

behave --tags=@cadastro



# [Atualizações em desenvolvimento:]
-Arquitetura que irá executar os testes em 3 navegadores paralelamente







#[Comandos necessários para instalação e execução do teste]

pip install selenium

pip install behave

pip install nose

pip install allure-behave

#Para que o relatorio allure seja instalado
npm install -g allure-commandline --save-dev

#executar no terminal e criar reports
behave --tags=@cadastro -f allure_behave.formatter:AllureFormatter -o %allure_result_folder% ./features

#Para exibir o relatório com os casos de testes em questão, execute:
allure serve %allure_result_folder%



