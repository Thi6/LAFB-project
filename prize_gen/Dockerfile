
FROM node:10
ARG VERSION=bigprize 
WORKDIR /usr/src/app

COPY package*.json ./

RUN npm install

COPY . .
RUN cp ./routes/${VERSION}.js ./routes/account.js
EXPOSE 5002
ENTRYPOINT [ "node", "server.js" ]
