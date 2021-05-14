## Requirements

### 1) docker-ce

- Install docker requirements:
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
- Install docker-ce:
  ```sh
  $ sudo apt-get update
  $ sudo apt-get install docker-ce
  ```
- Enable execution without root (restart your user session to work):
  ```sh
  $ sudo usermod -aG docker $USER
  ```
- Test it:
  ```sh
  $ docker run hello-world
  ```

### 2) docker-compose

- Install docker-compose:
  ```sh
  $ sudo curl -L https://github.com/docker/compose/releases/download/1.19.0/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
  $ sudo chmod +x /usr/local/bin/docker-compose
  ```
- Test it:
  ```sh
  $ docker-compose --version
  ```

### 3) Git

- Install Git:
  ```sh
  $ sudo apt-get install git
  ```
- Basic config of git:
  ```sh
  $ git config --global user.name "John Doe"
  $ git config --global user.email john.doe@server.com
  ```
