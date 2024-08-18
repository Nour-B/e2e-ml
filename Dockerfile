# lightweight python
FROM python:3.7

ARG GITHUB_SHA
ARG GITHUB_REF

LABEL GITHUB_SHA=${GITHUB_SHA}
LABEL GITHUB_REF=${GITHUB_REF}

# Add an environment variable APP_HOME=/app to the container.
ENV APP_HOME=/app

# Make /app current directory
WORKDIR $APP_HOME

# Copy local code to the container image.
COPY app/ .

# Install dependencies
RUN pip3 install -r requirements.txt

# Application port
EXPOSE 8501

# Run the streamlit on container startup
CMD [ "streamlit", "run","--server.enableCORS","false","myapp.py" ]