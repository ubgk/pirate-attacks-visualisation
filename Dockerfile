FROM python:3.10-slim-buster

# Create the container user
RUN useradd -ms /bin/bash vizuser
WORKDIR /home/vizuser
# Switch to "vizuser"
USER vizuser

# Add user bin to PATH
ENV PATH="/home/vizuser/.local/bin:$PATH"

# Install dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY assets assets
COPY data data
COPY visualizations visualizations
COPY utils utils

COPY app.py app.py

ENV MAPBOX_STYLE="mapbox://styles/paolaos/clbkzimcc002y14lkv0e29b9y"
ENV MAPBOX_TOKEN="pk.eyJ1IjoicGFvbGFvcyIsImEiOiJjbGJremQxa2swMnZjM29tdjhxMHpmbnVnIn0.SPBize1vnl4Zd047-aj5sQ"

# Variable port for Heroku
ENV PORT=8000
EXPOSE $PORT

# Docker does not expand variables, so we need to tell it to not-bypass the Shell to evaluate $PORT
CMD ["sh", "-c", "gunicorn --workers=1 --threads=4 --worker-class=gthread --bind=0.0.0.0:${PORT} app:server"]
