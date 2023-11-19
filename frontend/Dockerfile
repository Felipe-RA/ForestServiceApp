FROM node:20 
# 20 is the latest LTS version of node as of 18/11/2023.  https://endoflife.date/nodejs

WORKDIR /app

COPY package.json /app/

RUN npm install

COPY . /app

RUN npm run build

CMD ["npm", "start"]
