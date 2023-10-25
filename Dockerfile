FROM python:3.8

ARG UID
ARG GID

# Update the package list, install sudo, create a non-root user, and grant password-less sudo permissions
RUN addgroup --gid $GID me && \
    adduser --uid $UID --gid $GID --disabled-password --gecos "" me && \
    echo 'me ALL=(ALL) NOPASSWD: ALL' >> /etc/sudoers

# Set the non-root user as the default user
USER me