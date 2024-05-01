# Hootsi App

Hootsi App is a web application developed with Flask that allows performing CRUD (Create, Read, Update, Delete) operations on a MySQL database. The application is containerized using Docker to facilitate deployment and management.

## Prerequisites
- Python (version 3.x)
- Docker
- Basic knowledge of SQL and relational databases

## Installation and Execution
1. **Clone the Repository**: Clone this repository to your local machine using the following command:
   ```
   git clone https://github.com/JulianTorrest/hootsi_app.git
   ```

2. **Configure the Database**: Open the `app.py` file and update the database URI in the Flask application configuration (`SQLALCHEMY_DATABASE_URI`) with the details of your MySQL database.

3. **Build the Docker Image**: From the root directory of the project, run the following command to build the Docker image:
   ```
   docker build -t hootsi_app .
   ```

4. **Run the Application with Docker Compose**: Once the image has been built, you can run the application and MySQL database using Docker Compose with the following command:
   ```
   docker-compose up -d
   ```

5. **Access the Application**: Open a web browser and navigate to `http://localhost:5000` to access the application.

## Project Structure
- `app.py`: Main file of the Flask application.
- `models.py`: Defines the database models using SQLAlchemy.
- `forms.py`: Contains WTForms forms for data validation.
- `routes.py`: Defines the routes and logic of the application.
- `templates/`: Folder containing HTML templates for the user interface.
- `static/`: Optional folder for static files such as CSS, JavaScript, etc.

## Unit and Integration Testing
The `test_app.py` file contains unit and integration tests for the Flask application. You can run these tests using the following command:
```
python -m unittest test_app.py
```

## Contribution
Contributions are welcome! If you find any bugs or have any suggestions for improvement, feel free to open an issue or submit a pull request.

## License
This project is licensed under the [MIT License](LICENSE).
