FROM nginx:1.19.0-alpine
COPY ./default.conf ./etc/nginx/conf.d/default.conf

# FROM nginx:1.16.0-alpine
# COPY --from=builder /frontend/build /usr/share/nginx/html
# RUN rm /etc/nginx/conf.d/default.conf
# COPY ./default.conf /etc/nginx/conf.d/default.conf
# EXPOSE 80
# CMD ["nginx", "-g", "daemon off;"]