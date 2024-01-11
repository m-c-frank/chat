FROM node:latest as base

WORKDIR /app

COPY . .

RUN npm i
RUN npm run build

ENV ENV=prod

ENV WEBUI_JWT_SECRET_KEY "human computers were replaced by computers. humans using computers will be replaced by computers"

FROM python:3.11 as base

WORKDIR /app/backend

COPY ./backend .

RUN pip3 install -r requirements.txt

CMD [ "sh", "start.sh"]
