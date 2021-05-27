FROM python:3.9-slim
ENV PYTHONUNBUFFERED 1
RUN mkdir /nameSurvey
WORKDIR /nameSurvey
COPY . /nameSurvey/
# RUN conda list --export > requirements.txt
# RUN pip freeze > requirements.txt
COPY requirements.txt /tmp/
RUN pip install --requirement /tmp/requirements.txt
CMD python /nameSurvey/nameSurvey/nameFind.py
