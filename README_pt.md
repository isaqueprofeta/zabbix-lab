# Laboratório simples em docker para o Zabbix com PostgreSQL, Grafana e Zapix(Testes em API)

## Important Note:

Se você estiver usando o Zabbix 5.0 LTS ou usando uma versão anterior ao release do 5.4 por favor, remova ou comente as linhas do container zabbix-reports, ou o docker-compose não vai subir.

## Conteúdo

- Zabbix:
  - Zabbix Server zabbix-server:10051
  - Zabbix Agent em: zabbix-agent:10050
  - Zabbix Frontend em: http://zabbix-frontend:8080
- Banco de dados:
  - Postgresql em : postgresql:5432
  - PGAdmin em : http://pgadmin:5050
- Ferramentas de apoio:
  - Zapix em: http://zapix
  - Grafana em: http://grafana:3000
  - Mailhog: http://mailhog:8025
- Provisionamento / Pré-configurações:
  - Grafana já está provisionado com :
    - Instalados o plugin e datasources para Zabbix
    - Configurado o Datasource do Zabbix para o Zabbix
    - Configurado o Datasource PostgreSQL para o banco de dados do Zabbix
    - Notification Channel usando e-mail e MailHog
  - Zabbix já está provisionado com :
    - Atualização do host "Zabbix server" para usar o nome zabbix-agent com DNS
    - Atualização do Tipo de Mídia EMail para usar o MailHog
    - Configurada a Mídia E-Mail para o usuário "Admin" usando MailHog
    - Habilitada a ação "Report problems to Zabbix administrators"
  - Zabbix 5.4 or mais atual:
    - Container para os Relatórios agendados do zabbix-web-server
    - Configurada a URL do Frontend para o lab: http://zabbix-frontend:8080

## Como usar:

- [Instalar os pré-requisitos](./REQUIREMENTS.md)
- Copiar o projeto e a dependência do zapix para sua estação:
  ```sh
  $ git clone --recurse-submodules https://git.serpro/monitoracao/zabbix-lab.git
  ```
- Em caso de esquecimento do parâmetro "--recurse-submodules" acima, ative o zapix usando os comandos abaixo:
  ```sh
  $ git submodule init
  $ git submodule update
  ```
- **Se necessário** editar as variaveis de opções de versão:

  ```sh
  $ vim .env
  ```

  | Ambiente         | Padrão     | Outras Opções |
  | ---------------- | ---------- | ------------- |
  | ZABBIX_VERSION   | 5.4-latest | 5.0-latest ou 5.2-latest ou trunk (o último é para versões de desenvolvimento)|
  | POSTGRES_VERSION | 12         | 11 |

- Iniciar o gestor do hosts para facilitar acesso:
  ```sh
  $ docker run -d \
      -v /var/run/docker.sock:/tmp/docker.sock \
      -v /etc/hosts:/tmp/hosts \
      dvdarias/docker-hoster
  ```
- Iniciar o projeto com o docker-compose
  ```sh
  $ docker-compose up -d
  ```
- **Observe** que a estrutura em docker **não usa 'localhost'** então não use esse hostname 'localhost' para configurar o PGAdmin para PostgreSQL e no mailhog. Para configurar os mesmos, atentar-se para a opção de hostname para cada contêiner dentro da configuração do arquivo docker-compose.yml.

# Sobre o Zabbix

![Zabbix](https://assets.zabbix.com/img/logo/zabbix_logo_500x131.png)

O Zabbix é uma solução de monitoramento distribuído de código aberto para grandes ambientes - O repositório base desse projeto que contem todos os **Dockerfiles** do [Zabbix](https://zabbix.com/) para [Docker](https://www.docker.com/) é o [zabbix-docker](https://github.com/zabbix/zabbix-docker) com [builds automáticas](https://registry.hub.docker.com/u/zabbix/) publicadas no [Docker Hub Registry](https://registry.hub.docker.com/).

# Sobre o Zapix

Ferramenta Online para testes e desenvolvimento usando pesquisas dentro da API Web do Zabbix - Projeto original em: [Github Zapix](https://github.com/monitoringartist/zapix) por [monitoringartist](https://monitoringartist.com/).

# Sobre o Grafana

![Grafana](https://raw.githubusercontent.com/grafana/grafana/master/docs/logo-horizontal.png)

[Grafana](https://grafana.com) é uma ferramenta para relatórios e análise de dados - Versão em container já configurada para uso com o plugin do zabbix

# Sobre o Mailhog

![MailHog](https://raw.githubusercontent.com/mailhog/MailHog-UI/master/assets/images/hog.png)

Ferramenta para teste de envio de emails para desenvolvedores - [MailHog](https://github.com/mailhog/MailHog).
