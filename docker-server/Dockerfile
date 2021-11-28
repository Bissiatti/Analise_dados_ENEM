FROM python:3.8.12

RUN apt-get update -y && apt-get upgrade -y && apt-get install nodejs -y

RUN apt-get install npm -y

WORKDIR /usr/app

RUN pip install lightgbm

COPY package*.json ./

RUN npm install

COPY . .

EXPOSE 3000

CMD ["npm", "start"]