FROM node:14-alpine 
COPY ./web ./ui
WORKDIR /ui
RUN npm install

RUN npm run build
# Start the app
CMD [ "npm", "start"]