FROM python:3.8

ARG UID
ARG GID

# Create non-root user
RUN addgroup --gid $GID me
RUN adduser --uid $UID --gid $GID --disabled-password --gecos "" me
RUN echo 'me ALL=(ALL) NOPASSWD: ALL' >> /etc/sudoers

# Additional command
RUN pip install --upgrade pip
RUN pip install mysql-connector-python
RUN pip install python-dotenv

# Set the non-root user as the default user
USER me