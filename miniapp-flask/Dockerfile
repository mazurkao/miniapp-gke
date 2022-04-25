FROM python:3.6

ARG project_dir=/app/

ADD requirements.txt $project_dir
ADD logging.yaml $project_dir
ADD app.py $project_dir

WORKDIR $project_dir

#RUN pip install flask
RUN pip install -r requirements.txt

EXPOSE 5555

CMD ["python", "app.py"]
