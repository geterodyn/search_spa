# frontend
FROM node:12.12.0-alpine as vue-build-stage

WORKDIR /app

COPY ./frontend/package.json ./
RUN npm install
COPY ./frontend .

RUN npm run build

# backend and nginx
FROM nginx:1.17.4-alpine as prod-stage
WORKDIR /app

RUN apk update \
  && apk add --no-cache python3 \
  && pip3 install --upgrade pip setuptools

RUN apk update \
  && apk -u --no-cache add gcc musl-dev linux-headers python3-dev postgresql-dev py3-pip

COPY --from=vue-build-stage /app/dist /usr/share/nginx/html
COPY ./nginx/default.conf /etc/nginx/conf.d/default.conf

COPY ./backend/requirements.txt ./
RUN pip3 install -r requirements.txt
RUN pip3 install gunicorn
COPY ./backend .

ENV DJANGO_SETTINGS_MODULE=searchapp.settings

CMD gunicorn --workers 4 --bind 0.0.0.0:5000 --daemon searchapp.wsgi \
  && sed -i -e "s/__PORT__/$PORT/" /etc/nginx/conf.d/default.conf \
  && nginx -g 'daemon off;'

