FROM tensorflow/tensorflow:1.12.0-py3

ENV LANG=C.UTF-8
ENV FLASK=run.py
RUN mkdir /gpt2-app
WORKDIR /gpt2-app
ADD . /gpt2-app
RUN pip3 install -r requirements.txt
RUN python3 app/main/gpt2/download_model.py 117M

RUN flask db init && \
    flask db migrate && \
    flask db upgrade

CMD ["python", "run.py"]