# Use an official Python runtime as a parent image
FROM python:3.10

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

# Set the working directory in the container
WORKDIR /app

# Add the requirements file and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt



# Add the rest of the application code
COPY /app .

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "app.py"]

#docker build -t my-python-app .
#docker run -p 4000:80 my-python-app