FROM python:3.10-alpine

WORKDIR /app

ENV PYTHONUNBUFFERED=1
ENV PATH="/scripts:/py/bin:$PATH"

COPY ./app /app
COPY ./scripts /scripts
COPY ./etc/requirements.txt /requirements.txt
COPY ./etc/requirements.dev.txt /requirements.dev.txt

EXPOSE 8000

ARG DEV=false

RUN apk add --update --no-cache postgresql-client jpeg-dev zlib zlib-dev && \
    apk add --update --no-cache --virtual .build-deps \
        build-base postgresql-dev musl-dev linux-headers && \
    python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /requirements.txt && \
    if [ "$DEV" = "true" ]; then /py/bin/pip install -r /requirements.dev.txt; fi && \
    apk del .build-deps && \
    rm -rf /var/cache/apk/* /root/.cache /requirements.txt /requirements.dev.txt && \
    # Crear usuario sin acceso root
    adduser --disabled-password --no-create-home django-user && \
    # Preparar directorios con permisos adecuados
    mkdir -p /vol/web/media /vol/web/static && \
    chown -R django-user:django-user /vol && \
    chmod -R 755 /vol && \
    chmod -R +x /scripts

USER django-user

CMD ["run.sh"]
