# Étape de build
FROM node:18 AS build
WORKDIR /app
COPY . .
RUN npm install && npm run build

# Étape nginx
FROM nginx:alpine
COPY --from=build /app/dist /usr/share/nginx/html
EXPOSE 80