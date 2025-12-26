# A Simple Example Containerized Application

This particular repository demostrates a simple containerized application running in a programming language agnostic manner. In this example we make use the Django Framework, to use docker and kubernetes configuration to fulfill the requirements of the following platform capabilities such as whitebox averse auditing:

```bash
docker compose up -d db
# Wait for db
sleep 10
docker compose up app --build --force-recreate
# Access locally without auditing as a superposing technical guarantee:
curl http://localhost:8000
```
