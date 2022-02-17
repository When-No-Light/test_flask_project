FROM python:3.9-buster

# Make a diractory for our application
WORKDIR /app
# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt


# Copy our source code
COPY . /app

# Run the application
CMD ["flask", "run"]