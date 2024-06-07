FROM python
WORKDIR /app
COPY . /app
CMD ["python3", "for_upload_api.py"]