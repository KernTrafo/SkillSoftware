FROM ubuntu:latest
LABEL maintainer="neubuerger.felix@fh-swf.de"
RUN adduser kerntrafo

WORKDIR /home/kerntrafo
# install system dependencies
RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip

# copy and install the python requirements
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN pip install gunicorn
RUN pip install nltk
RUN mkdir nltk_data
RUN [ "python", "-c", "import nltk; nltk.download('all',  download_dir='/usr/nltk_data')" ]

ENV NLTK_DATA='/usr/nltk_data/'
# copy the apps contents

COPY app app
# COPY migrations migrations
COPY main.py config.py run.sh export_data.py Stellenplan_V2.3.xlsx needed_skills.txt ./
# COPY app.db ./
RUN chmod +x run.sh

#RUN chown -R kerntrafo:kerntrafo ./

RUN chmod 776 .
USER kerntrafo
EXPOSE 8000
ENTRYPOINT ["./run.sh"]