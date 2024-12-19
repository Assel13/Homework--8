# Homework 8

Этот проект включает Jupyter Notebook, работающий в Docker контейнере.

## Как запустить

1. Склонируйте репозиторий:
    ```bash
    git clone https://github.com/Assel13/homework8.git
    ```

2. Перейдите в директорию проекта:
    ```bash
    cd homework8
    ```

3. Постройте Docker-образ:
    ```bash
    docker build -t my-jupyter-notebook .
    ```

4. Запустите Docker контейнер:
    ```bash
    docker run -p 8888:8888 my-jupyter-notebook
    ```

5. Откройте Jupyter Notebook в браузере по адресу: [http://localhost:8888](http://localhost:8888). Если потребуется токен, проверьте вывод терминала.

## Содержание

- [notebooks](./notebooks): директория с Jupyter ноутбуками.
- [data](./data): данные для анализа.
