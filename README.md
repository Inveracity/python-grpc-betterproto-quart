# Python, gRPC, Betterproto and Quartz

This is just some code exploration to figure out how these fancy things work

## Run it

```
# Install prerequisites
pip install pipenv
pipenv sync --dev

# Generate python code from protocol buffers
# pipenv run generate # do not run this, it's broken right now, the generated code is currently included in bookstore/lib

# Run the recommendations gRPC service
recommendations = "python -m bookstore.rec_service"

# Run the webserver
web = "python -m bookstore.marketplace.marketplace"
```

The webserver asks the recommendations service for book recommendations in the "mystery" category and shows them in the browser.

## Known issues

- Betterproto version 2.0.0b2 does not generate the base class in order for the grpc server to start, this is solved by downloading the `master` branch of betterproto and copying it in to the virtual environment that pipenv generates. Hopefully this is fixed in 2.0.0b3

## Resources

- Realpython on Microservices with gRPC: https://realpython.com/python-microservices-grpc
- Betterproto: https://github.com/danielgtaylor/python-betterproto
- Quarts: https://pypi.org/project/pyobjc-framework-Quartz/
