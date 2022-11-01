## Para instalar o Odoo 15 (Windows)
É necessário fazer uns esforços à mais para instalar o Odoo 15 além de meramente pegar o seu código do GitHub e jogar no seu projeto.\
\
O site https://learnopenerp.blogspot.com/2021/10/configure-install-odoo15-with-pycharm-on-windows.html ensina alguns passos a serem seguidos antes de executar o famigerado\
`pip install -r requirements.txt`.

###  Instale  o Python 3.8
O Odoo 15 utiliza alguns scripts desatualizados para novas versões do Python. Por isso a versão utilizada aqui é o Python 3.8.
\
Use-o preferencialmente para criar um ambiente virtual onde instalaremos o Odoo 15.

### Altere o requirements.txt
Altere as seguintes linhas do arquivo (que vem junto na pasta do Odoo 15):

- 3: `cryptography==2.6.1` por `cryptography==36.0`
- 17: `libsass==0.18.0` por `libsass==0.21.0`

### Faça download de alguns programas prévios para o Windows 
Esses arquivos são necessários tanto para execução do Odoo quanto para sua instalação.

Por isso baixe:
- wkhtmltopdf, 
- Win64OpenSSL
- PostgreSQL
- Visual Code BuildTools

Acerca do último item (Visual Code BuildTools), instale o módulo `Desenvolvimento para Desktop com C++`, com:
- Ferramentas de compilação
- Ferramentas do  CMake
- Recursos principais de ferramentas de testes
- AddressSanitizer do C++

Não se esqueça de incluir o  `wkhtmltopdf` e  `Win64OpenSSL` no `PATH` do seu sistema (o endereço da pasta `bin` deles).

Pronto! Agora é só dar o `pip install -r requirements.txt` para instalar os requisitos!

##  Configurar o Odoo 15 antes de iniciar
Alguns passos para configurar o Odoo 15 e ligar ele com o PostgreSQL 

###  Inicie o PostGreSQL e crie um usuário pro Odoo
Você pode fazer isso com a ferramenta `pgAdmin4` que vem com o PostgreSQL.

### Crie o  arquivo de configuração do odoo
Crie um arquivo dentro da pasta raiz do Odoo 15 chamado de odoo.conf e coloque as seguintes informações nele:

<pre><code>
    [options]
    db_host = {endereco_db}
    db_port = {porta_db}
    db_user = {nome_usuario_odoo}
    db_password = {senha_db}
    db_filter = .*
    addons_path = {pasta addons do odoo (path absoluto) para o ./odoo-15.0/addons},
                  {pasta do addons customizada, conforme o Capítulo 3 do tutorial de Odoo}
    log_handler = [':INFO']
    log_level = info
    bin_path = {pasta pro bin do wkhtmltopdf}
</code></pre>

### Crie o arquivo de debug
Isso vai depender da IDE que você está usando, mas o básico que você deve saber é:
- O arquivo de script a ser executado é o odoo-15.0\odoo-bin
- Coloque como argumento para esse script `-c {caminho absoluto para o "odoo-15.0\odoo.conf"}`
- Selecione o Python 3.8 como interpretador, preferencialmente dentro de um Ambiente Virtual (venv)

Agora, é só iniciar o PostgreeSQL e executar o debug para continuar seguindo com o tutorial do Odoo!