## Pre-requisitos

### 1) docker-ce

- Instalar pré-requisitos do docker:
  ```sh
  $ sudo apt-get update
  $ sudo apt-get install \
      apt-transport-https \
      ca-certificates \
      curl \
      software-properties-common
  $ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
  $ sudo add-apt-repository \
    "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
    $(lsb_release -cs) \
    stable"
  ```
- Instalar o docker-ce:
  ```sh
  $ sudo apt-get update
  $ sudo apt-get install docker-ce
  ```
- Habilitar execução sem root (reinicie a sessão do seu usuarío para que funcione):
  ```sh
  $ sudo usermod -aG docker $USER
  ```
- Testar instalação:
  ```sh
  $ docker run hello-world
  ```

### 2) docker-compose

- Instalar o docker-compose:
  ```sh
  $ sudo curl -L https://github.com/docker/compose/releases/download/1.19.0/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
  $ sudo chmod +x /usr/local/bin/docker-compose
  ```
- Testar a instalação:
  ```sh
  $ docker-compose --version
  ```

### 3) Git

- Instalar o Git:
  ```sh
  $ sudo apt-get install git
  ```
- Configuração básica do git:
  ```sh
  $ git config --global user.name "Fulano Ciclano de Tal"
  $ git config --global user.email fulano.tal@servidor.com
  ```
