# jjownd

## Description
jjownd is a dynamically generated moodboard web application, built using Python and Flask. It serves an non-interactive page where users can view all images passsed to the `/src` directrory.

## Installation
The application is Dockerized for easy installation and setup:
1. Ensure Docker is installed on your system.
2. Build the Docker image using the provided Dockerfile.
3. Run the Docker container, which will start the web application.

## Usage
Access the application through a web browser on port 80. The web interface allows for the creation and viewing of moodboards.


## Running with Docker

Run the Docker container, mounting a local directory to `/src` in the container:
   ```bash
   docker run -p 80:80 -v /path/to/local/src:/src ghcr.io/saahirlol/jjownd:main
   ```

Replace `/path/to/local/src` with the path to your local directory containing the images.

## Running with Docker Compose

Create a `docker-compose.yml` file with the following content:

```yaml
version: '3'
services:
  jjownd:
    image: ghcr.io/saahirlol/jjownd:main
    ports:
      - "80:80"
    volumes:
      - /path/to/local/src:/src
```

Replace `/path/to/local/src` with the path to your local directory containing the images.

Then run the application using:

```bash
docker-compose up
```
