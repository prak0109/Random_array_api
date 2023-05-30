
## Random Array API

An Api endpoint which takes a sentence as an input and returns a random 500 dimensional array of floats. 


## Documentation

The provided code demonstrates several considerations to make the solution production-quality:

Logging: The code includes a logging configuration with an appropriate log level (INFO) and a logger object. This allows for proper logging of events, errors, and exceptions during runtime. Logging helps in debugging and monitoring the application in a production environment.

Error Handling: The code includes error handling logic with appropriate HTTP status codes and error messages. It checks for different types of errors such as invalid sentence type, missing sentence, and exceptions during array generation. The error responses are consistent and provide meaningful information to the client.

Swagger Documentation: The code uses Flask-Swagger-UI to generate and serve API documentation using the OpenAPI (Swagger) specification. Swagger UI provides a user-friendly interface for exploring and testing the API endpoints. This documentation is helpful for both developers and consumers of the API.

Separation of Concerns: The code follows the principle of separation of concerns by separating the route handling functions, the random array generation function, and the main application logic. This modular structure enhances code readability, maintainability, and testability.

Input Validation: The code performs input validation on the "sentence" parameter. It checks the type of the input, verifies if it is a non-empty string, and rejects numerical values. By validating input, the code ensures that only valid data is processed, reducing the chances of unexpected behavior or security vulnerabilities.

Swagger JSON and Static Files: The code includes routes to serve the Swagger JSON file and the static Swagger UI files. This ensures that the Swagger UI interface and API documentation are accessible to users.

Portability: The code utilizes Flask, a lightweight web framework, making the solution easily portable and deployable. Flask's simplicity and scalability allow for easy integration with other systems and services.

Code Organization: The code follows a standard structure with imports, configurations, route definitions, and a main application block. This organization improves code readability and makes it easier for other developers to understand and maintain the codebase.

Deployment Readiness: The code includes the necessary configuration and code blocks to run the Flask application using the app.run() method. This allows the application to be executed directly, making it deployment-ready with minimal additional setup.


## Installation

Install python dependancies using pip

```bash
  pip install requirements.txt
```
    
## Running Tests

To run tests, run the following command from the terminal

```bash
  python test_api.py
```


## Tech Stack

**Client:** Flask Server

**Server:** Localhost


## Run Locally




Install dependencies

```bash
  pip install requirements.txt
```

Start the server

```bash
  python app.py
```


## API Reference

#### Get all items

```http
  POST /random_array
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| sentence | `This is an example sentence` | Use form-data from POSTMAN to pass key and value |

#### Get swagger for api

```http
  GET /swagger/
```


