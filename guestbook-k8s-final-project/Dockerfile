FROM node:20-alpine

WORKDIR /app

COPY package*.json ./
RUN npm install --omit=dev && npm cache clean --force

COPY server.js ./
COPY index.html ./
COPY index.default.html ./

EXPOSE 3000

USER node

CMD ["node", "server.js"]
