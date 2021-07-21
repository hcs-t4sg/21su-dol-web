FROM python:3.9.5

WORKDIR /ui

ADD . /ui
RUN pip install -r requirements.txt
RUN python -m spacy download en_core_web_sm
RUN pip install -e ./ableist-language-detector

#ENV MLFLOW_TRACKING_URI=http://localhost:5000

EXPOSE 5000
EXPOSE 1234

#COPY ./runServer.sh /usr/bin/
#RUN chmod a+x /usr/bin/runServer.sh
#
#COPY ./serveModel.sh /usr/bin/
#RUN chmod a+x /usr/bin/serveModel.sh
