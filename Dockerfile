# Author: Ke
FROM postgres
ENV POSTGRES_PASSWORD dbpassword
ENV POSTGRES_DB password_manager
COPY password_db.sql /docker-entrypoint-initdb.d/