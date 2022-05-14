FROM node:alpine

WORKDIR '/app'

RUN npm install http-server -g
RUN npm install -g @angular/cli
COPY package.json .
RUN npm install
RUN ng build --prod
COPY ./dist ./dist

CMD ["http-server","./dist/my-app"]

#docker run -p 8082:8080 772a57f46bb3  