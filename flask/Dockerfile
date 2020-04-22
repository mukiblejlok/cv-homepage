FROM python:3.7

ARG PROXY

# Install Dos2Unix to handle .sh edited in Windows
RUN apt-get update
RUN apt-get install dos2unix

RUN python -m pip install --upgrade pip --proxy="$PROXY"

# Install Flask Requirements
COPY ./requirements/flask.txt /tmp/requirements/flask.txt
RUN pip install -r /tmp/requirements/flask.txt --proxy="$PROXY"

# Install Azure Requirements
COPY ./requirements/azure.txt /tmp/requirements/azure.txt
RUN pip install -r /tmp/requirements/azure.txt --proxy="$PROXY"


# Adding non-root user to run the app
ARG APP_USER
RUN useradd --create-home $APP_USER
WORKDIR /home/$APP_USER

# Copy application
COPY . /home/$APP_USER/

# Copy shell scripts
COPY ./*.sh /home/$APP_USER/
RUN chmod 755 /home/$APP_USER/*.sh
RUN dos2unix /home/$APP_USER/*.sh

# Switch to app user
USER $APP_USER

# Expose default port
ARG FLASK_PORT
EXPOSE $FLASK_PORT
