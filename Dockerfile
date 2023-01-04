FROM python:latest
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY src src
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \ 
    CMD curl -f http://localhost:5000/health || exit 1
ENTRYPOINT ["python", "./src/app.py"]
EXPOSE 5000