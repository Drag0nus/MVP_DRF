# What's inside?
 * [Django](https://github.com/django/django)/[Django REST framework](https://github.com/tomchristie/django-rest-framework)
 * [Redis](https://github.com/antirez/redis)
 * [PostgreSQL](https://github.com/postgres/postgres)
 * [Gunicorn](https://github.com/benoitc/gunicorn) WSGI HTTP Server
 * [nginx](https://nginx.org/)
 * [Tornado](https://github.com/tornadoweb/tornado) for handling websockets and more
 * [Celery](https://github.com/celery/celery) Distributed Task Queue
 * [Supervisor](https://github.com/Supervisor/supervisor) - client/server process management system
 * Config samples for each tool from above
 * and more...

# How to start:
 1. Install [VirtualBox](https://www.virtualbox.org/wiki/Downloads) if not installed.
 2. Install [Vagrant](https://www.vagrantup.com/downloads.html) if not installed.
 3. Install  [Ansible (version 2.0.2)](http://docs.ansible.com/ansible/intro_installation.html) if not installed.
 4. Run `sudo ansible-galaxy install -r ./ansible/requirements.yml` from root project directory for installing Ansible role dependencies.
 5. Run `sudo -- sh -c "echo '192.168.38.66 myrest.local flower.myrest.local api.myrest.local ws.myrest.local' >> /etc/hosts"` for simple accessing to Vagrant machine in your browser.
 6. Run `vagrant up` from root project directory for start the Vagrant machine. At first time machine will be automatically provisioned.
 7. Configure PyCharm (if you are using it):
     - Configuring Python interpreter: File > Settings > Project Interpreter > Add Remote > Vagrant > Python interpreter path: `/home/vagrant/myrest/venv/bin/python` > OK
     - Configuring Django support: File > Settings > Languages & Frameworks > Django > Enable Django support; Django project root: `{project_dir}`; Settings: `django_app/settings.py`
     - Configuring Django run/debug configurations: Run > Edit configurations… > Add new configuration > Django server > Name: Django Development Server; Host: 0.0.0.0; Port: 8000; Run browser: http://myrest.local:8000/; Path mapping: `Local path - path to project on host system : Remote path - path to project on vagrant machine`
     - Configuring Tornado run/debug configurations: Run > Edit configurations… > Add new configuration > Python > Name: Tornado Development Server; Script: `{project_dir}/run_tornado_app.py`; Environment Variables: `DJANGO_SETTINGS_MODULE=myrest.settings;` Path mapping: `Local path - path to project on host system : Remote path - path to project on vagrant machine`
     - Configuring database: Database > Add > Data Source > PostgreSQL > Download Driver > Host: `localhost`; Port: `5433`; Database: `myrest`; User: `myrest`; Password: `{password}` > Configure SSH > Check use SSH tunnel; Proxy host: `127.0.0.1`; Port: `2222`; Proxy user: `vagrant`; Auth type: Key pair; Private key file: `./.vagrant/machines/default/virtualbox/private_key` > OK > Test Connection > OK

***
##### _Notice!_ In this project is used Ansible Vault!
Files `host_vars/staging/vault.yml` and `host_vars/staging/vault.yml` are encrypted by default (Default password is `Ulumulu88`).
They're used to store sensitive data as db names, passwords, keys, secrets etc.
Before deploying to public servers as production or staging you must:

 1. Decrypt necessary files by command `ansible-vault decrypt host_vars/staging/vault.yml host_vars/production/vault.yml` (run it from ansible directory) using default password.
 2. Edit configuration in those files as needed.
    Also if it's first edition of those files you _SHOULD_ edit:
     - database name, user and password;
     - django secret key (http://www.miniwebtool.com/django-secret-key-generator/);
    For passwords better to use generated (http://passwordsgenerator.net/).
 3. Encrypt files again with your _NEW AND SECURE_ password using command `ansible-vault encrypt host_vars/staging/vault.yml host_vars/production/vault.yml`.
 4. Have fun!
***

## How to deploy the project to remote server(s)
 1. Edit respective files in a `host_vars` directory, as well as inventory files. This repo includes default configuration samples for production and staging environments.
 2. Execute `./deploy <inventory name> <tags>` command in the project's root directory, where <inventory name> is the name of your inventory (e.g. "staging" or "production"), and <tags> are optional tags that will execute only the tasks that were marked by this tag (e.g. "provision" tag, which will skip installing most part of the setup and only update the code from a repo and restart services).
 3. Give password to decrypt necessary vault data.
 3. Enjoy deployment :)

# Useful commands

## Deploy.sh script
 - `./deploy {environment} {tags}` - Deploy to {environment} servers by chosen tags. Example: `./deploy vagrant` - will run all deploy process to vagrant machine, `./deploy vagrant backend` - will run backend part of deploy process to vagrant machine.

## Ansible
 - `bin/ansible-playbook -i ./ansible/{environment}.ini ./ansible/site.yml` - Deploy to {environment} servers.

## Vagrant
 - `vagrant up` - Start the virtual machine.
 - `vagrant halt` - Shutdown the virtual machine.
 - `vagrant destroy` - Destroy the virtual machine.
 - `vagrant provision` - Triggers provisioning on a running virtual machine.
 - `vagrant ssh` - Create an ssh connection with the virtual machine.
 - `vagrant reload` - Restarts vagrant machine, loads new Vagrantfile configuration.
 - `vagrant status` - Outputs status of the vagrant machine.
 - `vagrant suspend` - Suspends the machine.
 - `vagrant resume` - Resume a suspended vagrant machine.
 - `vagrant share` - Share your Vagrant environment with anyone in the world.

### SSH
 - `ssh-keygen -t rsa -f ~/.ssh/id_rsa -C "your_email@example.com"` - Generate a new SSH key (https://help.github.com/articles/generating-ssh-keys/).
 - `cat ~/.ssh/id_rsa.pub` - Show SSH public key.
 - `cat ~/.ssh/id_rsa` - Show SSH private key.