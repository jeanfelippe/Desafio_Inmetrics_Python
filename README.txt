#instalar
pip install selenium
pip install behave
pip install nose
pip install allure-behave

behave --tags=@cadastro


#executar no terminal para criar reports
behave --tags=@cadastro -f allure_behave.formatter:AllureFormatter -o %allure_result_folder% ./features

#Para que o relatorio seja exibido, instale via
npm install -g allure-commandline --save-dev

#Para exibir o relatório com os casos de testes em questão, execute:
allure serve %allure_result_folder%


