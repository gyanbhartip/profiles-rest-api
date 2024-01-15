# Profiles REST API

Profiles REST API course code.

# Build a Backend REST API with Python & Django - Beginner

This is the supplementary cheat sheet document for our course: [Build a Backend REST API with Python & Django - Beginner](https://londonapp.dev/c1)

<!-- TOC depthFrom:2 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 -->

- [Profiles REST API](#profiles-rest-api)
- [Build a Backend REST API with Python \& Django - Beginner](#build-a-backend-rest-api-with-python--django---beginner)
  - [Git](#git)
  - [SSH Key Management](#ssh-key-management)
  - [Virtual Environments](#virtual-environments)
  - [Django Management Commands](#django-management-commands)
  - [Vagrant](#vagrant)
  - [Terminal / GitBash Commands](#terminal--gitbash-commands)

<!-- /TOC -->

## Git

Use the below Git commands in the Windows Command Prompt or macOS Terminal.

**Configure default email and name**

_Note: This only needs to be done the first time you use Git on your machine_

```
git config --global user.email "your@email.com"
git config --global user.name "Your Name"
```

**Initialise a new Git repository**

```
git init
```

**Commit changes to Git**

```
git add .
git commit -am "Commit message"
```

**Set Git remote**

_Note: This only needs to be done once, the details are provided by GitHub after creating a new project_

```
git remote add origin <URL TO PROJECT>
git push -u origin master
```

**Push changes to GitHub**

```
git push origin
```

## SSH Key Management

The below commands are used to manage SSH keys on your local development machine.

**Checking for existing SSH key**

```
ls ~/.ssh/
```

**Print contents of public key**

```
cat ~/.ssh/id_rsa.pub
```

**Generate new SSH key on your local machine**

```
ssh-keygen -t rsa -b 4096 -C "EMAIL ADDRESS"
```

## Virtual Environments

The below commands are used for managing Virtual Environments using Python3-env. Use these commands when connected to your Vagrant server.

**Create new environment**

```
python -m venv ~/env
```

**Activate virtual environment**

```
source ~/env/bin/activate
```

**De-activate virtual environment**

```
deactivate
```

**Install requirements from requirements.txt**

_Note: Virtual environment must be activated_

```
pip install -r requirements.txt
```

## Django Management Commands

**Create new Django project**

```
//old version
django-admin.py startproject profiles_project  .
```

```
//newer versions
python -m django startproject profiles_project .
```

**Create new Django app**

```
python manage.py startapp profiles_api
```

**Start Django development server**

```
python manage.py runserver 0.0.0.0:8000
```

**Create database migrations file**

```
python manage.py makemigrations
```

**Run migrations**

```
python manage.py migrate
```

**Create new superuser**

```
python manage.py createsuperuser
```

## Vagrant

These commands are used for managing Vagrant using the GitBash or Terminal windows.

**Initialise Vagrant on project**

```
vagrant init ubuntu/bionic64
```

**Start Vagrant box**

```
vagrant up
```

**Connect to Vagrant box**

```
vagrant ssh
```

**Disconnect from Vagrant box**

_Note: This command is a standard linux command for ending an SSH session_

```
exit
```

**Stop Vagrant box**

```
vagrant halt
```

**Remove Vagrant box**

```
vagrant destroy
```

**Update Vagrant box image**

_Note: you must rebuild the image after updating_

```
vagrant box update
```

## Terminal / GitBash Commands

Change directory

```
cd /directory_name
```

Change to parent directory

```
cd ..
```

![Alt](https://repobeats.axiom.co/api/embed/0aef20cb506933f028aee461520d0f115176d31a.svg "Repobeats analytics image")
