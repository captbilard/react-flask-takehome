FROM node:16-alpine 
COPY ./web ./ui
WORKDIR /ui
RUN npm install

RUN npm run build
# Start the app
CMD [ "npm", "start"]