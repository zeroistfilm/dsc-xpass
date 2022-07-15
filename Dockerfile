FROM ubuntu:20.04
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update
RUN apt-get install -y python3 pip
RUN pip install fastapi uvicorn[standard] aiohttp pandas matplotlib apscheduler sqlalchemy psycopg2-binary opencv-python boto3 python-multipart requests
RUN apt-get install -y libgl1-mesa-glx
RUN apt-get install -q -y libglib2.0-0
