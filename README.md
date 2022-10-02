## Mineiríssima 🍵

ERP / MVC Model

### Pré-requisitos
<hr>

<ul>
  <li>Mysql</li>  
  https://www.mysql.com/downloads/
  <li>Pycharm</li>
  https://www.jetbrains.com/pt-br/pycharm/download/#section=windows
</ul>

### 📁 Download do projeto
<hr>

Clone o repositório e realiza o descompactamento. 

```
https://github.com/leandroleonardo/mineirissima
```

### 📃 Configuração de banco de dados
<hr>

Abra a pasta config_SQL e execute configuracao.sql para gerar as 
tabelas e dados de produtos, em seguida execute o script base_de_teste.sql 
para gerar uma massa de dados para teste.

```
https://github.com/leandroleonardo/mineirissima/tree/main/config_SQL
```

### 🖥️ Configuração da IDE 
<hr>

Para executar o projeto abra ele no Pycharm.

![image](https://user-images.githubusercontent.com/57691941/190924523-1ea0a5d2-042e-41bd-bb61-74e36fa70f05.png)

O projeto utiliza algumas bibliotecas, então para roda-lo é necessário a instalação das demais. 
Para instalar basta executar o seguinte código em seu terminal.

```
pip install tk
pip install PyMySQL
pip install matplotlib
pip install pandas
pip install tkcalendar
```

Depois navegue até a pasta controllers, clique com o botão direito 
do mouse no arquivo main.py e selecione a opção Run 'main'.

![image](https://user-images.githubusercontent.com/57691941/193470637-17852af1-9ea5-4456-be7c-e019eccc47fd.png)

### 🖥️ Configuração do programa
<hr>

Quando abrir o software pela primeira vez, deverá configurar o banco de dados, para isso basta navegar 
até a opção de configuração localizado no canto superior esquerdo e adicionar o 
nome do usuário do banco, senha e chave.

![image](https://user-images.githubusercontent.com/57691941/193472057-17e90bfe-cf20-4f47-862e-299035313921.png)

Depois, basta realizar o login com os seguintes dados:

```
Usuário: admin
Senha: admin
```


