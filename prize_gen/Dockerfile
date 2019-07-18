ARG PRIZE_GEN_VERSION=account
FROM node:${PRIZE_GEN_VERSION}
 
WORKDIR /usr/src/app

COPY package*.json ./

RUN npm install

COPY . .

EXPOSE 5002
ENTRYPOINT [ "node", "server.js" ]
