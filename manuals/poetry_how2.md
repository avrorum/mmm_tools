
## 1 ЧАСТЬ


По шагам с поетри создание проектов:


Поставить поетри под 3 версию пайтоне - см подробно
https://ru.hexlet.io/blog/posts/ispolzovanie-neskolkih-versiy-python-na-unix-podobnyh-operatsionnyh-sistemah


По степам 

- https://ru.hexlet.io/projects/49/members/9745?step_id=207 and here 

- https://python-poetry.org/docs/basic-usage/ 



### First installation and initialization

1. Create directory with name of project 
`$mkdir PROJECT_NAME`

2. inside directory call 	
`$poetry new PROJECT_NAME`

If existed project: `$ call "poetry init`



Если нужно использовать в поетри версию питона другую, чем системную

1)  После "poetry new PROJECT_NAME" в .toml  прописать нужную версию питона, например:
```
==
[tool.poetry.dependencies]
python = "^3.8"
==
```

2) Задать в поетри: 
`poetry env use .venv/bin/python`

3) Проверить
`poetry run python`


//


### Установка пакетов в проект: 

`Poetry add PACKAGE_NAME`	      # для целей последующего использования юзером

`Poetry add PACKAGE_NAME --dev` # для целей разработки 


или: 
Add in pyproject.toml

## 


poetry install
- no need 4
- no need activate env created

дальше проверка работы


https://python-poetry.org/docs/managing-environments/


-------
## 2 ЧАСТЬ


#1 запуск скрипта проекта через поетри 
poetry run SCRIPTNAME (f.e. brain-gcd)

Example:
`
poetry run python -m brain_games.scripts.brain_games
poetry run python -m gendiff.scripts.gendiff -h
`

#2 проверка стиля через поетри

`poetry run flake8 brain_games`
OR
`make lint`


#3 перестроение пакета проекта через поетри после обновления кода пакета/проекта
poetry build
OR
make build 

#4 установка пакета через поетри  локально после обновления кода 
poetry install
OR 
make package-install 


#5 публикация пакета  во вншений репозиторий 
после внесения изменений
poetry publish --repository testPyPi
		name
		password

----

Useful commands 

poetry add PACK_NAME
	- add package in project dependencies

poetry remove PACK_NAME
	- delete

poetry update --lock
	- update packages from dependencies w/0 crushing


poetry build
	-- сборка пакета для последующей установки
	для его установки локально `python3 -m pip install --user dist/hello-0.1.0-py3-none-any.whl`

если нужна локальная установка пакета без его сборки, то 
`python3 -m pip install . ` , где "." -  текущая директория

---

Если нужно использовать в поетри версию питона другую, чем системную

После "poetry new PROJECT_NAME" в .toml  прописать нужную версию питона

```bash
$ poetry env use .venv/bin/python
```

Если нужно использовать в поетри версию питона другую, чем системную, то подменить командой:
?
```bash
# temporary set python version as local
Poetry local 3.8.13

poetry env use /full/path/to/python
```
потом такой же командой вернуть нужную

---



