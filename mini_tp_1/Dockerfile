FROM alpine
WORKDIR /app
COPY app_test.py .
RUN apk add --update vim
RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools
RUN pip freeze > /requirements.txt
RUN pip install Flask
EXPOSE 5000
CMD ["python","/app/app_test.py"]
