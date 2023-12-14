
PYENV
--------
HOW TO USE

### Install python version

```bash
$ pyenv install 3.8.13

# create environment

# pyenv virtualenv [PYTHON VERSION] [NAME of ENV]
$ pyenv virtualenv 3.8.13 apps3

# envs are stored in .pyenv/versions/

# activate environment
pyenv activate NAME

# deactivate
pyenv deactivate
```

What should be installed before:
1. pyenv
2. homebrew on mac and virtualenv via homebrew 



——————

### PACKAGE INSTALLATION

```bash
# install package inside environment
$ pip install -e .

# OR via requirements.txt

$ pip install -Ur requirements.txt


# list of libs installed:
$ pip list
```

--------


### INSTALLATION OF TOOLS:


1. PYENV INSTALLATION AND ENV MANAGEMENET

```bash
#1 install pyenv
git clone https://github.com/pyenv/pyenv.git ~/.pyenv

#2 Configure your shell's environment for Pyenv into .bashrc

export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv init -)"
export PYENV_VIRTUALENV_DISABLE_PROMPT=1
if which pyenv-virtualenv-init > /dev/null; then eval "$(pyenv virtualenv-init -)"; fi
```

---------

2 VIRTUALENV - on mac with homebrew

2.1 homebrew install

```bash
# ON MAC
pyenv-virtualenv

# taken from https://akrabat.com/creating-virtual-environments-with-pyenv/
$ brew install readline xz
$ brew install pyenv pyenv-virtualenv


# NOT ON MAC install virtualenv
git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
```


-----

WITHOUT HOMEBREW: 

```bash
# Installation:
$ python3 -m pip install --user virtualenv

# Example of usage:
$ mkdir virtualenv-example
$ cd virtualenv-example=
$ virtualenv -p python3.7 env
```


== FINISH INSTALLATION ==

--------------------------------


OLDER WAYS:


PIPIENV TOOL
--------
```bash
#0 Install tool
pip3.7 install --user pipenv

or
sudo -H pip3.7 install -U pipenv


#1 initilize project and create environment (env name = will be name of folder)
# from catalog with project
pipenv --python python3.7


#2 while working daily
# from project folder -- activate this command
pipenv shell

# install packages (after activating environment)
pipenv install PACKAGENAME
```


------
