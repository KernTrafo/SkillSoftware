FROM python:3
LABEL maintainer="neubuerger.felix@fh-swf.de"

WORKDIR /home/utility

# copy and install the python requirements
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY util_scripts .

CMD ["export_data.py"]
ENTRYPOINT ["python"]