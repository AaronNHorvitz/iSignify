# Stage 1: Use a modern, slim Python runtime as the base image
FROM python:3.10-slim

# Stage 2: Set the working directory inside the container
WORKDIR /code

# Stage 3: Copy only the requirements file to leverage Docker's layer caching
COPY ./requirements.txt /code/requirements.txt

# Stage 4: Install the Python dependencies
RUN pip install --no-cache-dir --requirement /code/requirements.txt

# Stage 5: Copy your application's source code from the backend/src directory
COPY ./backend/src /code/src

# Stage 6: Expose the port that the application will run on
EXPOSE 8000

# Stage 7: Define the command to run the application using uvicorn
# Note that we now refer to the main module as "src.main"
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]