# Python, gRPC, Betterproto and Quartz

This is just some code exploration to figure out how these fancy things work

## Run it

```
# Install prerequisites
pip install pipenv
pipenv sync --dev

# Generate python code from protocol buffers
# pipenv run generate

# Run the recommendations gRPC service
pipenv run recommendations

# Run the green gRPC service, this service changes the background colour
pipenv run green

# Run the webserver
pipenv run web
```

Browse: http://127.0.0.1:5000/

additionally change the background colour:

- http://127.0.0.1:5000/moldy
- http://127.0.0.1:5000/pastel
- http://127.0.0.1:5000/modern

The webserver asks the recommendations service for book recommendations in the "mystery" category and shows them in the browser.

## Known issues

- Betterproto version 2.0.0b2 does not generate the base class in order for the grpc server to start, this is solved by downloading the `master` branch of betterproto and copying it in to the virtual environment that pipenv generates. Hopefully this is fixed in 2.0.0b3

## Resources

- Realpython on Microservices with gRPC: https://realpython.com/python-microservices-grpc
- Betterproto: https://github.com/danielgtaylor/python-betterproto
- Quart: https://pypi.org/project/Quart/
