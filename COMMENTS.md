CONFIG SYSTEM:
  Linux everton 5.10.0-10-amd64 #1 SMP Debian 5.10.84-1 (2021-12-08) x86_64
  Intel(R) Celeron(R) CPU B815 @ 1.60GHz
  MB mem :   3783,8 total
  MB swap:    974,0 total
  harddisk:   320,0 total


  Como eu já utilizei alguns pacotes necessário no processo nos estudos a parte que estou fazendo não precisei instalar eles pois já estavam instalados 
  #os pacotes que eu utilizei vai está no arquivo: requirements.txt
  Agora vamos aos comandos dados:
  
  $ mkdir API && cd API #mkdir cria um diretorio e o cd abri o diretorio
  $ virtualenv venv --python=/usr/bin/python3.9 #Cria um ambiente virtual no python 3.9
  $ source venv/bin/activate #fazer a ativaçao da virtualizacao
  $ pip install django djangorestframework #instalar o django e djangorest na virtualizacao
  $ python3 manage.py startapp api #criar uma nova API
  $ python3 manage.py makemigrations #gerar o arquivo de Migrações para atualizar o banco de dados
  $ python3 manage.py migrate #criar uma estrutura inicial do banco de dados
  $ python3 manage.py runserver #rodar o servidor
  
 Apos, com sorte, o servidor roudou tudo certo eu fui para a segunda parte que é a modelagem, essa parte eu deixo o detalhes no código.
 
A terceira parte que seria a Serialização:Criei um diretorio /api no /API, na pasta /api eu criei dois python file um chamado serializers.py e o outro viewsets.py (A explicação de cada linha está no código)
Na quarta parte do routers no arquivo api/urls.py eu criei uma routa

Com tudo terminado eu percebi que estava com um problema no Django.db, eu tenho ele instalado no sistema mas estã indetificando, eu passei o dinheiro procurando uma solução em grupos do facebook, discord, em sites de foruns como o stackoverflow e reddit e em alguns blogs. Como o prazo é até o dia 05/01 às 12:00 eu ainda estou procurando um solução.

Coisas que eu queria fazer se tivesse mais tempo:
  Tem um conhecido meu que desenvolveu uma API para consulta de CNPJ com o banco de dados da Policia Federal, se pudesse eu iria colocar essa API para consultar os 	dados ligado com a outra api do conhecido para mantê-los sempre atualizados (https://github.com/gabzin/cnpj.git)
  Organizava melhor o código e melhorava ele
