Project Title

Briefly describe your project and its purpose.

**Table of Contents**
<!-- TOC -->

- [Strategy](#strategy)
- [Scope](#scope)
    - [features and functionalities](#features-and-functionalities)
- [Structure](#structure)
  - [Frameworks/technologies used](#frameworkstechnologies-used)
- [Skeleton](#skeleton)
  - [Backend](#backend)
    - [Technologies, libraries, and frameworks](#technologies-libraries-and-frameworks)
    - [Database](#database)
      - [*Database schema*](#database-schema)
    - [API Documentation](#api-documentation)
      - [CRUD table](#crud-table)
      - [API endpoint and values](#api-endpoint-and-values)
      - [*Listings*](#listings)
      - [*Filter and Search*](#filter-and-search)
      - [*Save listing*](#save-listing)
    - [Backend Testing](#backend-testing)
    - [Bugs](#bugs)
- [Surface](#surface)
  - [Frontend](#frontend)
    - [Libraries](#libraries)
    - [Enhanced User Experience with React](#enhanced-user-experience-with-react)
    - [Color mood](#color-mood)
    - [Code Quality and Consistency](#code-quality-and-consistency)
    - [Code Linters](#code-linters)
- [Getting Started](#getting-started)
- [Installation](#installation)
- [Usage](#usage)
- [Deployment](#deployment)
- [Benchmarking](#benchmarking)
- [References](#references)
    - [Tools used](#tools-used)

<!-- /TOC -->


# Strategy

- High-level goals and objectives 
- Target audience
- Problem to be solves
- Overarching strategies you have in mind.


# Scope

### features and functionalities 

- *Boosting Visibility*  

Enhance your listing's visibility with our custom sorting algorithm! Listings with over 4 photos and 150+ word descriptions are given a 70% priority boost, ensuring they appear at the top of the list for higher user engagement. Get your listings noticed!

- user stories
- project roadmap to help others understand the scope of the project.



# Structure


- Describe the overall architecture and structure
- frameworks/technologies used
- Arrangement of the frontend and backend within the same repository

## Frameworks/technologies used
  1. [![Auto Markdown TOC](https://img.shields.io/badge/Auto_Markdown_TOC-v3.0.12-blue?logoColor=white)](https://open-vsx.org/extension/huntertran/auto-markdown-toc) - Generate TOC (table of contents) of headlines from parsed markdown file.
  2. [![Miniwebtool - Django Secret Key Generator](https://img.shields.io/badge/Miniwebtool-Django_Secret_Key_Generator-54c247)](https://miniwebtool.com/django-secret-key-generator/) - Generates secure random secret keys for Django web applications.
  3. 

| No. | Library/ dependacy                                                                                                        | Description                                                                                                     |
|----|---------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| 1.  | [![Auto Markdown TOC](https://img.shields.io/badge/Auto_Markdown_TOC-v3.0.12-blue?logoColor=white)](https://open-vsx.org/extension/huntertran/auto-markdown-toc) | Generate TOC (table of contents) of headlines from parsed markdown file.                                      |
| 2.  | [![Miniwebtool - Django Secret Key Generator](https://img.shields.io/badge/Miniwebtool-Django_Secret_Key_Generator-54c247)](https://miniwebtool.com/django-secret-key-generator/) | Generates secure random secret keys for Django web applications.                                              |


# Skeleton

- basic layout
    - directory structure
    - key files. 
    - overview of the main components, modules/packages used in your Django REST framework and React.js project.

## Backend

- Technologies, libraries, and frameworks
- the data models 
- authentication methods
- API endpoints
- how to add new features or endpoints to the backend.

### Technologies, libraries, and frameworks

| No. | Framework/Library/Dependency                                | Purpose                                             |
|----|-------------------------------------------------------------|-----------------------------------------------------|
| 1  | [![asgiref 3.7.2](https://img.shields.io/badge/asgiref-3.7.2-BC7D29)](https://pypi.org/project/asgiref/) | ASGI framework, often used in Django applications. |
| 2  | [![backports.zoneinfo 0.2.1](https://img.shields.io/badge/backports.zoneinfo-0.2.1-0088CC)](https://pypi.org/project/backports.zoneinfo/) | Backports of Python zoneinfo module for working with time zones. |
| 3  | [![black 23.9.1](https://img.shields.io/badge/black-23.9.1-000000)](https://pypi.org/project/black/) | The uncompromising code formatter for Python. |
| 4  | [![click 8.1.7](https://img.shields.io/badge/click-8.1.7-333333)](https://pypi.org/project/click/) | A simple Python module to add command-line interface creation capabilities to your software. |
| 5  | [![cloudinary 1.34.0](https://img.shields.io/badge/cloudinary-1.34.0-FF8800)](https://pypi.org/project/cloudinary/) | Python SDK for Cloudinary, a cloud-based image and video management platform. |
| 6  | [![coverage 7.3.2](https://img.shields.io/badge/coverage-7.3.2-brightgreen)](https://coverage.readthedocs.io/en/7.3.2/) | A tool for measuring code coverage of Python programs. |
| 7  | [![dj-database-url 2.1.0](https://img.shields.io/badge/dj-database-url-2.1.0-FF3333)](https://pypi.org/project/dj-database-url/) | A Django package for configuring database connections via URLs. |
| 8  | [![dj-rest-auth 5.0.1](https://img.shields.io/badge/dj-rest-auth-5.0.1-1D78B8)](https://pypi.org/project/dj-rest-auth/) | A Django app for handling RESTful authentication. |
| 9  | [![Django 4.2.5](https://img.shields.io/badge/Django-4.2.5-092E20?logo=django)](https://pypi.org/project/Django/) | A high-level Python web framework that encourages rapid development and clean, pragmatic design. |
| 10 | [![django-cloudinary-storage 0.3.0](https://img.shields.io/badge/django--cloudinary--storage-0.3.0-2C3E50?logo=django)](https://pypi.org/project/django-cloudinary-storage/) | Django package that provides Cloudinary storages for both media and static files as well as management commands for removing unnecessary files. |
| 11 | [![django-cors-headers 4.2.0](https://img.shields.io/badge/django-cors-headers-4.2.0-FF9900)](https://pypi.org/project/django-cors-headers/) | A Django app for handling Cross-Origin Resource Sharing (CORS). |
| 12 | [![django-oauth-toolkit 2.3.0](https://img.shields.io/badge/django-oauth-toolkit-2.3.0-00B3E0)](https://pypi.org/project/django-oauth-toolkit/) | A package for adding OAuth2 capabilities to Django projects. |
| 13 | [![djangorestframework 3.14.0](https://img.shields.io/badge/djangorestframework-3.14.0-33AADD?logo=django)](https://pypi.org/project/djangorestframework/) | A powerful and flexible toolkit for building Web APIs in Django. |
| 14 | [![djangorestframework-simplejwt 5.3.0](https://img.shields.io/badge/djangorestframework-simplejwt-5.3.0-339933?logo=django)](https://pypi.org/project/djangorestframework-simplejwt/) | A package for adding simple JWT authentication to Django REST framework. |
| 15 | [![drf-social-oauth2 2.1.3](https://img.shields.io/badge/drf-social-oauth2-2.1.3-428BCA)](https://pypi.org/project/drf-social-oauth2/) | The main library that enables OAuth2 token-based authentication for email, password, as well as Google and Facebook. |
| 16 | [![ecdsa 0.18.0](https://img.shields.io/badge/ecdsa-0.18.0-4D4D4D)](https://pypi.org/project/ecdsa/) | A Python library for ECDSA (Elliptic Curve Digital Signature Algorithm). |
| 17 | [![gunicorn 21.2.0](https://img.shields.io/badge/gunicorn-21.2.0-366790)](https://pypi.org/project/gunicorn/) | A Python WSGI HTTP server for running web applications. |
| 18 | [![jwcrypto 1.5.0](https://img.shields.io/badge/jwcrypto-1.5.0-483D8B)](https://pypi.org/project/jwcrypto/) | A library for working with JSON Web Tokens (JWT). |
| 19 | [![oauthlib 3.2.2](https://img.shields.io/badge/oauthlib-3.2.2-4B0082)](https://pypi.org/project/oauthlib/) | A generic and reusable Python implementation of OAuth1 and OAuth2. |
| 20 | [![pathspec 0.11.2](https://img.shields.io/badge/pathspec-0.11.2-339933)](https://pypi.org/project/pathspec/) | A utility library for gitignore-style pattern matching of file paths. |
| 21 | [![phonenumbers 8.13.23](https://img.shields.io/badge/phonenumbers-8.13.23-0099CC)](https://pypi.org/project/phonenumbers/) | A Python library for working with phone numbers. |
| 22 | [![Pillow 10.0.1](https://img.shields.io/badge/Pillow-10.0.1-blue?logo=pillow)](https://pypi.org/project/Pillow/) | Adds image processing capabilities to your Python interpreter. |
| 23 | [![psycopg2 2.9.8](https://img.shields.io/badge/psycopg2-2.9.8-336791)](https://pypi.org/project/psycopg2/) | PostgreSQL adapter for Python. |
| 24 | [![pyasn1 0.5.0](https://img.shields.io/badge/pyasn1-0.5.0-4B0082)](https://pypi.org/project/pyasn1/) | A Python library for working with ASN.1 data. |
| 25 | [![pyenchant 3.2.2](https://img.shields.io/badge/pyenchant-3.2.2-FF5500)](https://pypi.org/project/pyenchant/) | A spellchecking library for Python. |
| 26 | [![PyJWT 2.8.0](https://img.shields.io/badge/PyJWT-2.8.0-0099CC)](https://pypi.org/project/PyJWT/) | A Python library for working with JSON Web Tokens (JWT). |
| 27 | [![python-jose 3.3.0](https://img.shields.io/badge/python-jose-3.3.0-006699)](https://pypi.org/project/python-jose/) | A Python library for working with JOSE (JSON Object Signing and Encryption). |
| 28 | [![python3-openid 3.2.0](https://img.shields.io/badge/python3-openid-3.2.0-FFA500)](https://pypi.org/project/python3-openid/) | A Python 3 implementation of the OpenID protocol. |
| 29 | [![requests-oauthlib 1.3.1](https://img.shields.io/badge/requests-oauthlib-1.3.1-0099CC)](https://pypi.org/project/requests-oauthlib/) | A library for adding OAuth support to HTTP requests. |
| 30 | [![responses 0.23.3](https://img.shields.io/badge/responses-0.23.3-336791)](https://pypi.org/project/responses/) | A utility for mocking HTTP requests in Python. |
| 31 | [![rsa 4.9](https://img.shields.io/badge/rsa-4.9-00B3E0)](https://pypi.org/project/rsa/) | A Python library for working with RSA (Rivest–Shamir–Adleman) encryption. |
| 32 | [![social-auth-app-django 5.3.0](https://img.shields.io/badge/social-auth-app-django-5.3.0-FF9966)](https://pypi.org/project/social-auth-app-django/) | An extension for Python Social Auth that integrates with Django. |
| 33 | [![social-auth-core 4.4.2](https://img.shields.io/badge/social-auth-core-4.4.2-428BCA)](https://pypi.org/project/social-auth-core/) | The core library for Python Social Auth. |
| 34 | [![sqlparse 0.4.4](https://img.shields.io/badge/sqlparse-0.4.4-1A4E8B)](https://pypi.org/project/sqlparse/) | SQL parsing and formatting library for Python. |
| 35 | [![types-PyYAML 6.0.12.12](https://img.shields.io/badge/types-PyYAML-6.0.12.12-FFA500)](https://pypi.org/project/types-PyYAML/) | Type hints for PyYAML. |
| 36 | [![urllib3 1.26.16](https://img.shields.io/badge/urllib3-1.26.16-0055FF)](https://pypi.org/project/urllib3/) | HTTP library for Python, used for making HTTP requests. |
| 37 | [![whitenoise 6.5.0](https://img.shields.io/badge/whitenoise-6.5.0-6699CC)](https://pypi.org/project/whitenoise/) | Simplifies serving static files in Django web applications. |





### Database

- the schema
- data models
- guidance on how to migrate and manage the database.

#### *Database schema*

### API Documentation

This Provides documentation on the available endpoints, request/response formats, and authentication methods. 

#### CRUD table

| ||Resources | |
|:----|:----|:----|:----|
|Method|ACCOUNTS|LISTINGS|FAVORITES
|create/POST|✓|✓|✓|
|retrive/ GET|✓|✓|✓|
|update/ PUT|✓|✓|x|
|destroy/ DELETE|x|✓|✓|
|list/GET|✓|✓|✓|
|search/GET|x|✓|x|



#### API endpoint and values

- #### *Authentication*

|Operation|Method|Endpoint|Expected Value|
|:----|:----|:----|:----|
|Registration|POST|api/create/|email, username, password, first_name|
|Login|POST|api-auth/login/|username, password|
|Logout|POST|api-auth/logout/|(No specific request data expected)|
|User Detail|GET|api/users/int:pk/|email, username, first_name, last_name, created_at, updated_at, image|
|Current User|GET|api/currentUser/|email, username, first_name, last_name, created_at, updated_at, image, is_current_user|
|User List|GET|api/users/| |
|Access Token|POST|api-auth/token/|Authorization code|
|Refresh Token|POST|api-auth/convert-token|Refresh token|


#### *Listings*

This section provides an overview of the available API endpoints and their functionalities for managing listings. The API follows a CRUD (Create, Read, Update, Delete) structure for listing resources.


|**HTTP Method**|**URI**|**CRUD Operation**|**View Name**|**Description**|**User Story #**|**Page**|
| :- | :- | :- | :- | :- | :- | :- |
|**GET**|/listings/|Read|ListAllListingsView|Returns a list of all listings.||Home|
|**GET**|/listings/{listing\_id}|Read|RetrieveListingView|Returns the details of a specific listing by ID.|||
|**POST**|/listings/|Create|CreateListingView|Creates a new listing.|||
|**PUT**|/listings/{listing\_id}|Update|UpdateListingView|Updates an existing listing by ID.|||
|**DELETE**|/listings/{listing\_id}|Delete|DeleteListingView|Deletes a listing by ID.|||

#### *Filter and Search*

The filter and search functionality allows users to search for properties based on specific criteria, save their searches, and view a list of their saved searches.


|**HTTP Method**|**URI**|**CRUD Operation**|**View Name**|**Description**|**User Story #**|
| :- | :- | :- | :- | :- | :- |
|**GET**|/api/properties/search|Read|Search Listings|Returns a list of properties that match the search criteria.||
|**POST**|/api/properties/filter|Read|Filter Listings|Returns a list of properties that match the filter criteria.||
|**POST**|/api/properties/save-search|Create|Save Search|Saves a list of properties that match the search criteria.||
|**GET**|/api/properties/saved-searches|Read|List Saved Searches|Returns a list of saved searches.||
|**DELETE**|/api/properties/saved-searches/{id}|Delete|Delete Saved Search|Deletes a saved search.||


#### *Save listing*


|**HTTP Method**|**URI**|**CRUD Operation**|**View Name**|**Description**|
| :- | :- | :- | :- | :- |
|**POST**|/listings/save|Create|Save Listing|Saves a property listing to the user's saved listings.|
|**GET**|/listings/saved|Read|List Saved Listings|Returns a list of the user's saved property listings.|
|**GET**|/listings/saved/{listing\_id}|Read|Retrieve Saved Listing|Returns the details of a specific saved property listing.|
|**DELETE**|/listings/saved/{listing\_id}|Delete|Delete Saved Listing|Deletes a property listing from the user's saved listings.|

### Backend Testing

### Bugs

- Bug: Custom Permission Class 'IsOwnerOrReadOnly' Attribute Error #76

# Surface

Discuss the user interface (UI) and user experience (UX) aspects of the project. Highlight the design principles, styles, and libraries used for creating the frontend while shareing screenshots and wireframes to give a visual sense of the project's appearance.

- Technologies, libraries, and frameworks
- Wireframe
- screenshots

## Frontend

Describe the technologies, libraries, and frameworks used in the frontend of your project. Provide information on how the user interface is structured and how to customize or extend it.

### Libraries


|No|Library|Specific use in the application|Justification|
| :- | :- | :- | :- |
|||||
|||||

### Enhanced User Experience with React
how the use of a React library and/or implemented feature has contributed to improved user experience.

|No|Title|Description|
| :- | :- | :- |
|1|Responsive and Interactive UI|React's component-based architecture allows for smooth transitions and dynamic updates, <br>providing users with an engaging and interactive interface.|
|2|Faster Load Times|React's Virtual DOM optimizes rendering, <br>resulting in quicker initial load times and a more responsive feel, which users will appreciate.|
|3|Real-Time Updates|Leveraging React, we've implemented real-time updates,<br>` `ensuring that users receive the latest information instantly, <br>whether it's in a chat application, a live dashboard, or other real-time scenarios.|
|4|Single-Page Application (SPA) Flow|By adopting React in our project, <br>we've created a seamless navigation experience within our application. <br>Users can move between sections without the interruption of full-page reloads.|
|5|Progressive Web App (PWA) Features|With React, we've enabled features such as offline access and push notifications, <br>turning our web application into a PWA, which offers users a more app-like experience.|
|6|Component Reusability|Our implementation of React promotes component reusability, <br>resulting in a consistent and user-friendly interface throughout the application.|
|7|Optimized Rendering|React's efficient rendering process ensures smooth animations and transitions, <br>providing users with a polished and visually appealing experience.|
|8|Error Handling|We've used React's error boundaries to gracefully handle errors, <br>ensuring that users receive informative error messages, <br>which helps build trust and confidence.|
|9|State Management|React, coupled with Redux (or your chosen state management library), <br>ensures that our application's data remains consistent and responsive, <br>delivering a smoother user experience.|
|10|Accessibility|By design, our React components prioritize accessibility, <br>making sure that all users, including those with disabilities, <br>can navigate and interact with our application effectively.|
|11|Testing and Debugging|We've incorporated React's support for component-level testing and <br>debugging tools like React DevTools, <br>which means our application is more stable and reliable for users.|
|12|Third-Party Libraries|The extensive React ecosystem has enabled us to integrate third-party libraries seamlessly, <br>enhancing the capabilities of our application and further enriching the user experience.|


### Color mood

### Code Quality and Consistency

### Code Linters






# Getting Started

Provide instructions for setting up and running your project locally. Include prerequisites, dependencies, or system requirements. This will guide users through the setup process for both the frontend and backend.

# Installation

List the specific steps required to install the project, including any environment variables or configuration files that need to be set up. including code snippets and commands for clarity.



# Usage

This section explain how users can interact with the project. Provide examples of common use cases and any necessary command-line instructions or API requests. Include information on how to start the development servers for both the frontend and backend.


# Deployment

Explain the deployment process for the project. Provide instructions for deploying both the frontend and backend to a production environment. Include any hosting or server-specific details.

# Benchmarking
By evaluating and comparing the features, performance, and user experience of Lanka Property Web, Ikman.lk, and Bayut, ThePropShop aims to set a high standard for the platform, ensuring it meets or exceeds industry-leading competitors in the real estate listing market. Please visit the sites for further information.

1. [Lanka Property Web](https://www.lankapropertyweb.com/)
1. [Ikman.lk](https://ikman.lk/)
1. [bayut](https://www.bayut.com/)

# References

1. [Django Rest framework](https://www.django-rest-framework.org/)
2. [Django for APIs](https://djangoforapis.com/)
3. [Markdown Tips & Tricks 2022 - Markdown Crash Course](https://www.youtube.com/watch?v=ftOBvusMHjQ)
4. [Adding Social Authentication to Django](https://testdriven.io/blog/django-social-auth/)
5. [Email + Social Logins in Django – Step by Step Guide](https://www.geeksforgeeks.org/email-social-logins-in-django-step-by-step-guide/)
6. [Drf-Social-Oauth2: Easy oauth2 integration](https://drf-social-oauth2.readthedocs.io/en/latest/index.html)
7. [Create New App In Facebook Developers Account Create App ID and App Secret Key In Facebook Developer](https://youtu.be/2XVmmXKJGVg?si=XDUmDDKjHqU7MbIA)
8. [Django Rest Framework Course - Social Logins with React and DRF - Part-9](https://www.youtube.com/watch?v=wlcCvzOLL8w&t=2245s)
9. [Serializer fields](https://www.django-rest-framework.org/api-guide/fields/#serializer-fields)
10. [django.contrib.humanize](https://docs.djangoproject.com/en/4.2/ref/contrib/humanize/#intcomma)
11. [MERN Stack Project: Build a Modern Real Estate Marketplace with react MERN (jwt, redux toolkit)](https://github.com/sahandghavidel/mern-estate/blob/main/client/src/App.jsx)
12. [https://estate.100jsprojects.com/](https://estate.100jsprojects.com/)

### Tools used

| No. | Name                                       | Purpose                                    |
|----|--------------------------------------------|--------------------------------------------|
| 1  | [Shields.io](https://shields.io/badges)  | Create badges. |
| 2  | [Simple Icons](https://simpleicons.org/) | Find and download SVG icons for various brands and products. |
|3| [Canva](https://www.canva.com/) | free-to-use online graphic design tool. |
|4| [Google Fonts](https://fonts.google.com/) |  Computer font and web font service owned by Google.  |
|5| [Font Awsome](https://fontawesome.com/) |  Internet's icon library and toolkit |
