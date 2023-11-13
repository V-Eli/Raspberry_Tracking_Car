#MULTI-ETAPA
#BUILD STAGE
FROM node:16-bullseye-slim AS build-stage

RUN npm install -g @angular/cli

RUN apt-get update && apt-get install -y --no-install-recommends \
    git  `# For developer container`

# Instala los archivos que estan en el package.json
COPY frontend/package*.json /code/frontend/
WORKDIR /code/frontend/
RUN npm ci --legacy-peer-deps

#Ahora copia la carpeta hello world y hace el build
COPY frontend /code/frontend/
RUN ng build

#PROD STAGE
FROM nginx as production-stage

RUN mkdir /app
COPY --from=build-stage /code/frontend/dist/ /app
COPY frontend/nginx.conf  /etc/nginx/nginx.conf

EXPOSE 4200
# EXPOSE 5000
# EXPOSE 5010

STOPSIGNAL SIGTERM

CMD ["nginx", "-g", "daemon off;"]