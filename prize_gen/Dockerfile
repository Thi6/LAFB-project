
FROM node:10
ARG VERSION=smallprize 
WORKDIR /usr/src/app

COPY package*.json ./

RUN npm install

COPY . .
RUN cp ./routes/${VERSION}.js ./routes/account.js
EXPOSE 5002
ENTRYPOINT [ "node", "server.js" ]
