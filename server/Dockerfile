FROM python:3.6-slim 

WORKDIR '/app'

RUN python -m pip install sklearn
RUN python -m pip install scipy
RUN python -m pip install numpy
RUN python -m pip install demjson
RUN python -m pip install matplotlib
RUN python -m pip install pandas
RUN python -m pip install neupy

RUN apt update
RUN yes |  apt install nodejs npm

COPY package.json .
RUN npm install 
COPY . .

CMD ["npm","start"]
