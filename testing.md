
## Backend Testing

### Database Configuration Testing

**Description:** This section outlines the testing process for the database configuration, including the desired outcome and steps taken during testing.

**Desired Outcome:**
- Verify that the database configuration functions correctly based on the environment ('DEV' or production).
- Confirm that the correct database engine (SQLite for development or PostgreSQL for production) is used.
- Ensure that the connection to the database is established successfully.

**Steps of Testing:**
1. Check the environment variable 'DEV' to determine whether it's a development environment.
2. If 'DEV' is present, configure the database using SQLite.
3. If not, configure the database using the 'DATABASE_URL' environment variable, assuming a production environment.
4. Print 'connected' to confirm a successful database connection.
5. CLI command: `python manage.py makemigrations --dry-run`
6. Observer the CLI outcome.
7. Remove the bug print.

**Observations:**

![Code Snippet](https://res.cloudinary.com/pjdevex/image/upload/v1696196071/thepropshop/testing/Screenshot_2023-10-01_233328_c57qah.png)
- The code snippet above demonstrates the database configuration logic.

![CLI Command and Outcome](https://res.cloudinary.com/pjdevex/image/upload/v1696196071/thepropshop/testing/Screenshot_2023-10-01_233343_iayyjh.png)
- When the 'DEV' environment variable is set, running the code produces the expected SQLite configuration.
- In a production environment without 'DEV', the 'DATABASE_URL' environment variable is used to configure PostgreSQL.

**Conclusion:** 
- The database configuration successfully adapts to different environments, either using SQLite for development or PostgreSQL for production.

