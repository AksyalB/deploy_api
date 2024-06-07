FROM python:3.10.11

WORKDIR /app

# Copy file requirements.txt ke dalam container
COPY requirement.txt .

# Install dependencies menggunakan pip
RUN pip install --no-cache-dir -r requirement.txt

COPY . /app
CMD ["python3", "for_upload_api.py"]