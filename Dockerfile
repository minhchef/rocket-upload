# Use the official Python image
FROM python:3.11-slim AS python-base

# Set the working directory in the container
WORKDIR /app

# Install system dependencies for Node.js, pnpm, and Python
RUN apt-get update && apt-get install -y curl gnupg && \
    curl -fsSL https://deb.nodesource.com/setup_18.x | bash - && \
    apt-get install -y nodejs && \
    npm install -g pnpm && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Node.js build stage
FROM python-base AS node-build
WORKDIR /app

COPY src ./src/
WORKDIR /app/src
RUN pnpm install --force
RUN pnpm build

# Copy the rest of the application code
COPY . .

# Final stage to assemble the Python application
FROM python-base AS final
WORKDIR /app

# Copy the Python dependencies and Node.js build artifacts
COPY --from=node-build /app /app

# Expose the port the app runs on
EXPOSE 5000

# Run the Flask app
CMD ["python", "manage.py"]
