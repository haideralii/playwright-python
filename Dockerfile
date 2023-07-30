# Step 1: Choose the base image
FROM mcr.microsoft.com/playwright/python:v1.35.0-jammy

# Step 2: Set up the working directory
WORKDIR /app

# Step 3: Copy the application files
COPY pages /app/pages

COPY tests /app/tests

COPY utils /app/utils

COPY .env.example /app/

COPY conftest.py /app/

COPY .pytest.ini /app/

COPY requirements.txt /app/

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache -r requirements.txt

RUN python -m playwright install --with-deps

CMD [ "pytest", "-v" ]