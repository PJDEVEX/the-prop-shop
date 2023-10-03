
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


### API Testing

[![Postman](https://img.shields.io/badge/Postman-FF6C37?logo=postman&logoColor=white)](https://www.postman.com/) 

We have used Postman for seamless API testing.

- General Configaration 
  - Create a Workspace: The Prop Shop
  - Create a New Collection: (Accounts) 

#### Testing - Signup 

  - Add a request for the API endpoint: signup
  - Config 
    - Request method: POST
    - URL: https://8000-pjdevex-thepropshop-fhncw5hdrsb.ws-eu105.gitpod.io/api/accounts/signup
    - Define Headers: 
        ```json
        {
        "key": "Content-Type",
        "value": "application/json"
        }
        ``` 

- **Scenario 1 - "Email already exists"**
    1. **Required:** Verify that the API returns an error message when trying to register with an existing email.
    2. **Config Body (JSON):**
    
        ```json
        {
            "name": "John Doe",
            "email": "john.doe@example.com",
            "password": "SecurePass123!",
            "password2": "SecurePass123!"
        }
        ```

    3. **Press "Send"**
    
    4. **Actual:** The response received the expected error message: "Email already exists." This confirms that the test case passed.
    
        ```json
        {"error": "Email already exists"}
        ```

    5. [**Screenshot**](https://res.cloudinary.com/pjdevex/image/upload/v1696370588/thepropshop/testing/email-already-exists_ov2pfd.png)

- **Scenario 2 - "Password must contain at least 6 characters, including at least one letter, one digit, and one special character (@$!%*#?&)."**
    1. **Required:** Verify that the API returns an error message when registering with a weak password.
    2. **Config Body (JSON):**
    
        ```json
        {
            "name": "Jane Smith",
            "email": "jane.smith@example.com",
            "password": "weak",
            "password2": "weak"
        }
        ```
    
    3. **Press "Send"**
    
    4. **Actual:** The response received the expected error message: "Password must contain at least 6 characters, including at least one letter, one digit, and one special character (@$!%*#?&)." This confirms that the test case passed.

        ```json
        {"error": "Password must contain at least 6 characters, including at least one letter, one digit, and one special character (@$!%*#?&)."}
        ```
    
    5. [**Screenshot**](https://res.cloudinary.com/pjdevex/image/upload/v1696371673/thepropshop/testing/password-must-contain-at-least-6-characters_cw630b.png)

- **Scenario 3 - "Passwords do not match"**
    1. **Required:** Verify that the API returns an error message when the provided passwords do not match.
    2. **Config Body (JSON):**
    
        ```json
        {
            "name": "Alice Johnson",
            "email": "alice.johnson@example.com",
            "password": "StrongPass123!",
            "password2": "MismatchedPass"
        }
        ```
    
    3. **Press "Send"**
    
    4. **Actual:** The response received the expected error message: "Passwords do not match." This confirms that the test case passed.
    
        ```json
        {"error": "Passwords do not match"}
        ```

    5. [**Screenshot**](https://res.cloudinary.com/pjdevex/image/upload/v1696371673/thepropshop/testing/passwords-do-not-match_akavlw.png)

- **Scenario 4 - Successful User Creation**
    1. **Required:** Verify that the API successfully creates a user account with valid data.
    2. **Config Body (JSON):**
    
        ```json
        {
            "name": "New User",
            "email": "new.user@example.com",
            "password": "StrongPass123!",
            "password2": "StrongPass123!"
        }
        ```
    
    3. **Press "Send"**
    
    4. **Actual:** The response confirms that the user was created successfully.
    
        ```json
        {"success": "Congratulations! User created successfully"}
        ```

    5. [**Screenshot**](https://res.cloudinary.com/pjdevex/image/upload/v1696371672/thepropshop/testing/successful-user-creation_tkacyr.png)

