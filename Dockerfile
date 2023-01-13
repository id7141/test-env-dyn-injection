FROM python:3.10.2
COPY . .
ENV PYTHONUNBUFFERED=1
CMD [ "python", "main.py" ]