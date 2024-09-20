FROM nicolaka/netshoot

# Install Python and venv
RUN apk add --no-cache python3 py3-pip python3-dev

# Install dev dependencies and semantic-release
RUN pip3 install --no-cache-dir python-semantic-release

# Copy requirements file
COPY app/requirements.txt /app/

# Create app directory
WORKDIR /app

# Copy app code and requirements
COPY app /app/

# Create and activate virtual environment, then install requirements
RUN python3 -m venv /app/venv
ENV PATH="/app/venv/bin:$PATH"
RUN pip3 install --no-cache-dir --upgrade pip && \
    pip3 install --no-cache-dir -r requirements.txt

# Set Python path
ENV PYTHONPATH=/app:/app/..

# Expose port 80
EXPOSE 80

# Run the Flask app
CMD ["python3", "-m", "app.main"]