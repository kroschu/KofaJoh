FROM python:3.11
LABEL developed_by='@LeoAlecksey'
WORKDIR /usr/src/app
COPY ./requirements.txt .
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt
COPY ./main.py .
COPY ./button.py .
COPY ./LICENCE.md .
COPY ./requests.db ./requests.db
COPY ./.env .
COPY ./.gitignore .
COPY ./start.sh .
CMD ["/bin/bash", "/usr/src/app/start.sh"]
