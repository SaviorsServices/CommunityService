
<p align="center"><a href="image" target="_blank"><img width="600"src="https://github.com/SaviorsServices/CommunityService/blob/master/images/logo/comunity.jpg"></a></p>

[![Build Status](https://travis-ci.org/SaviorsServices/CommunityService.svg?branch=master)](https://travis-ci.org/SaviorsServices/CommunityService)
  
<br>
  
## ℹ️ Sobre o projeto

Projeto desenvolvido durante a disciplina de Desenvolvimento de Software da Universidade de Brasília, campus Gama. Com o objetivo de divulgar pontos de atendimentos médicos gratuitos. <br>

## ℹ️ Tecnologias

<a href='https://github.com/SaviorsServices/CommunityService/blob/master/images/tecnologias/TravisCI-Mascot-1.png'><img width="130" src='https://github.com/SaviorsServices/CommunityService/blob/master/images/tecnologias/TravisCI-Mascot-1.png' alt='python' /></a>
<a href='https://github.com/SaviorsServices/CommunityService/blob/master/images/tecnologias/codeclimate.jpg'><img width="130" src='https://github.com/SaviorsServices/CommunityService/blob/master/images/tecnologias/codeclimate.jpg' alt='python' /></a>
<a href='https://github.com/SaviorsServices/CommunityService/blob/master/images/tecnologias/css-logo-400x400.png'><img width="130" src='https://github.com/SaviorsServices/CommunityService/blob/master/images/tecnologias/css-logo-400x400.png' alt='python' /></a>
<a href='https://github.com/SaviorsServices/CommunityService/blob/master/images/tecnologias/docker.gif'><img width="130" src='https://github.com/SaviorsServices/CommunityService/blob/master/images/tecnologias/docker.gif' alt='python' /></a>
<a href='https://github.com/SaviorsServices/CommunityService/blob/master/images/tecnologias/github.gif'><img width="130" src='https://github.com/SaviorsServices/CommunityService/blob/master/images/tecnologias/github.gif' alt='python' /></a>
<a href='https://github.com/SaviorsServices/CommunityService/blob/master/images/tecnologias/heroku.svg'><img width="80" src='https://github.com/SaviorsServices/CommunityService/blob/master/images/tecnologias/heroku.svg' alt='python' /></a>
<a href='https://github.com/SaviorsServices/CommunityService/blob/master/images/tecnologias/html.png'><img width="130" src='https://github.com/SaviorsServices/CommunityService/blob/master/images/tecnologias/html.png' alt='python' /></a>
<a href='https://github.com/SaviorsServices/CommunityService/blob/master/images/tecnologias/js3.png'><img width="140" src='https://github.com/SaviorsServices/CommunityService/blob/master/images/tecnologias/js3.png' alt='python' /></a>
<a href='https://github.com/SaviorsServices/CommunityService/blob/master/images/tecnologias/python-django.png'><img width="130" src='https://github.com/SaviorsServices/CommunityService/blob/master/images/tecnologias/python-django.png' alt='python' /></a>
<a href='https://github.com/SaviorsServices/CommunityService/blob/master/images/tecnologias/zenhub.jpg'><img width="130" src='https://github.com/SaviorsServices/CommunityService/blob/master/images/tecnologias/zenhub.jpg' alt='python' /></a>
<a href='https://github.com/SaviorsServices/CommunityService/blob/master/images/tecnologias/coveralls-logo.png'><img width="130" src='https://github.com/SaviorsServices/CommunityService/blob/master/images/tecnologias/coveralls-logo.png' alt='python' /></a> <br>

 ## ℹ️ Guia de Uso do Docker

* ### Instalação

Primeiramente é necessário ter o docker instalado, caso não tenha acesse o [Instalação docker](https://docs.docker.com/engine/installation/linux/docker-ce/). Após feito isso, instale o [Docker-compose](https://docs.docker.com/compose/install/).

* ### Comandos básicos 

 &emsp;&emsp; Para a utilização do ambiente em background, basta dar o comando abaixo e ele irá ligar o container:
 
 ```terminal
  docker-compose up -d
 ```
 &emsp;&emsp; Caso queira utilizar o ambiente com logs:

 ```terminal
  docker-compose up 
 ```
 &emsp;&emsp; Para a visualização dos logs quando em modo de execução background, use o comando abaixo:

 ```terminal
  docker-compose logs -f
 ```

 &emsp;&emsp; Para pausar o container:

  ```terminal
  docker-compose stop
 ```
 &emsp;&emsp; E para religar um container parado use o comando: 
 
 ```terminal
  docker-compose start 
 ```

 &emsp;&emsp; Para listar os containers que estão em execução:
 
 ```terminal
  docker ps
 ```
 &emsp;&emsp; Para listar todos os containers já executados na sua máquina:
 
 ```terminal
  docker ps -a
 ```
 &emsp;&emsp; Para executar comandos dentro do container:
 
 ```terminal
  docker-compose exec -it  "id do container"  "comandos"
 ```
 Para acessar o [bash](https://www.gnu.org/software/bash/) do container, substitua "comandos" por "bash".

* ## Rodando a aplicação

Para rodar a aplicação, entre na pasta do projeto em que está localizado o __docker-compose__ e digite no terminal:

```
  docker-compose up -d
```
Espere até que todos os serviços estejam disponíveis, acesse a página inicial do projeto com o seguinte endereço: https://localhost:8000  <br>

## ℹ️ Deploy

<p align="justify">O deploy da aplicação é feito de forma automatizada por meio da integração contínua (Travis CI) que é responsável por verificar a cobertura de teste  e realizar o deploy junto ao servidor de hospedagem Heroku.</p> <br>

## ℹ️ Testes

Para conferir a cobertura de testes, siga os passos abaixo:

__1º No terminal digite:__
```Terminal
  coverage run -m django test --settings=tests.settings 
```
Isso fará com que os testes sejam executados.

obs: Para funcionar, é necessário estar na raiz do projeto.

__2º No terminal digite:__
```Terminal
  coverage report
```
Esse comando irá gerar um relatório contendo as porcentagens da cobertura de testes em cada módulo e a cobertura total.

Obs: Para funcionar, é necessário ter realizado o passo anterior.

__3º No terminal digite (opcional):__
```Terminal
  coverage html
```
Esse comando irá gerar uma pasta contendo um arquivo html(index.html) que apresenta a cobertura de testes.  <br>

## 👤 Equipe de Desenvolvimento

<a href='https://github.com/SaviorsServices/CommunityService/blob/master/images/equipe/eduardo'><img width="130" src='https://github.com/SaviorsServices/CommunityService/blob/master/images/equipe/eduardo' alt='python' /></a>
<a href='https://github.com/SaviorsServices/CommunityService/blob/master/images/equipe/Vinicius.png'><img width="130" src='https://github.com/SaviorsServices/CommunityService/blob/master/images/equipe/Vinicius.png' alt='python' /></a>
<a href='https://github.com/SaviorsServices/CommunityService/blob/master/images/equipe/Ulysses.png'><img width="130" src='https://github.com/SaviorsServices/CommunityService/blob/master/images/equipe/Ulysses.png' alt='python' /></a>
<a href='https://github.com/SaviorsServices/CommunityService/blob/master/images/equipe/Thiago.png'><img width="130" src='https://github.com/SaviorsServices/CommunityService/blob/master/images/equipe/Thiago.png' alt='python' /></a>
<a href='https://github.com/SaviorsServices/CommunityService/blob/master/images/equipe/Amanda.png'><img width="130" src='https://github.com/SaviorsServices/CommunityService/blob/master/images/equipe/Amanda.png' alt='python' /></a>



