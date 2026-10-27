FROM registry.access.redhat.com/ubi9/python-311
COPY rechner.py server.py ./
EXPOSE 8080
CMD ["python", "server.py"]
