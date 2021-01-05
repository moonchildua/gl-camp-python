FROM python:3.8.5

WORKDIR /app

COPY . /app

RUN chmod +x python3-package.sh \
    && ./python3-package.sh

ENTRYPOINT ["python", "metrics.py"]