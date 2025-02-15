FROM node:latest

RUN mkdir -p /app/api

WORKDIR /app/api
COPY ./api/package*.json ./
RUN yarn

COPY ./api .
EXPOSE 8000
CMD [ "node", "app.js" ]
