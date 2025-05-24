# FastAPI Project

This project is a demonstration of building a web application using FastAPI, a modern, fast (high-performance) web framework for building APIs with Python 3.6+ based on standard Python type hints.

## Features
- **Automatic Documentation**: Utilizes Swagger UI(Docs) and ReDoc for easy access and testing of API endpoints.
- **Asynchronous Programming**: Leverages Python's modern features for enhanced performance and simplicity.
- **Typing System**: Supports type hints to define variable types using Pydantic.
- **OpenAPI and JSON Schema**: Automatically generates API schemas, supporting robust API development.

## Installation

To set up the application locally, follow these steps:

1. **Clone the repository**:

   git clone <https://github.com/lavanyap2823/FastAPI>


2. **Set up a virtual environment**:

   python -m venv fastapi-env
   source fastapi-env/bin/activate


3. **Install the required packages**:

   pip install -r requirements.txt


4. **Run the application**:

   uvicorn main:app --reload


## Requirements

Ensure you have the following installed:

- Python 3.6+
- FastAPI
- Uvicorn
- SQLAlchemy
- Pydantic

Refer to the `requirements.txt` file for a full list of dependencies.

## Usage

1. Start the FastAPI server using Uvicorn:

   uvicorn main:app --reload


2. Access the automatic interactive API documentation at:
   - [Swagger UI](http://127.0.0.1:8000/docs)
   - [ReDoc](http://127.0.0.1:8000/redoc)

## Deploying

1. Ensure you're in the `app` directory where the application files are located.
2. Use the `doppler` CLI or similar deployment platform to push your application to the cloud server.
3. Monitor the server logs for successful deployment.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License.

## Contact

For questions or feedback, please reach out to [lavanyap2823@gmail.com].