FROM node:20.0.0-alpine

WORKDIR /app

RUN apk update
RUN if [ -f package.json ]; then npm install; fi

ENV HOST 0.0.0.0
EXPOSE 3000

ENTRYPOINT npm run dev