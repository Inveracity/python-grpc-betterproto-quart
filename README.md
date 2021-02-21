# Python, gRPC, Betterproto and Quartz

This is just some code exploration to figure out how these fancy things work

```
# Install prerequisites
pip install pipenv
pipenv sync --dev

# Generates python code from protocol buffers
pipenv run grpc_recommendations

# Run the recommendations gRPC service
recommendations = "python -m bookstore.rec_service"

# Run the webserver
web = "python -m bookstore.marketplace.marketplace"
```

The webserver asks the recommendations service for book recommendations in the "mystery" category and shows them in the browser.

## Resources

- Realpython on Microservices with gRPC: https://realpython.com/python-microservices-grpc
- Betterproto: https://github.com/danielgtaylor/python-betterproto
- Quarts: https://pypi.org/project/pyobjc-framework-Quartz/
