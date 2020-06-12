FROM python:3.7-slim
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./
RUN pip install -r requirements.txt
EXPOSE 9000
CMD ["python", "app.py", "--host=0.0.0.0"]