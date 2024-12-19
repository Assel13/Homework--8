FROM jupyter/base-notebook

COPY . /home/jovyan/work/

RUN pip install some-library

WORKDIR /home/jovyan/work

CMD ["start-notebook.sh"]
