# First stage
FROM python:3.8 AS builder
COPY requirements.txt .

# install dependencies to the local user directory (e.g. /root/.local)
RUN pip install --user -r requirements.txt

# Second stage
FROM python:3.8-slim
WORKDIR /code

# copy only the dependencies installation files from the 1st stage image
COPY --from=builder /root/.local /root/.local
COPY ./src .

# update PATH environment variable
ENV PATH=/root/.local:$PATH

# run the app
CMD [ "python", "./main.py" ]
