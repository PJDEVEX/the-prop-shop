Project Title

Briefly describe your project and its purpose.

**Table of Contents**
<!-- TOC -->

- [Strategy](#strategy)
- [Scope](#scope)
- [Structure](#structure)
  - [Frameworks/technologies used](#frameworkstechnologies-used)
- [Skeleton](#skeleton)
  - [Backend](#backend)
    - [Technologies, libraries, and frameworks](#technologies-libraries-and-frameworks)
    - [Database](#database)
      - [*Database schema*](#database-schema)
    - [API Documentation](#api-documentation)
      - [*CRUD tables*](#crud-tables)
      - [*Listings*](#listings)
      - [*Filter and Search*](#filter-and-search)
      - [*Save listing*](#save-listing)
    - [Backend Testing](#backend-testing)
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

- features and functionalities 
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
| 1  | [![Django 4.2.5](https://img.shields.io/badge/Django-4.2.5-092E20?logo=django)](https://pypi.org/project/Django/) | A high-level Python web framework that encourages rapid development and clean, pragmatic design. |
| 2  | [![django-cloudinary-storage 0.3.0](https://img.shields.io/badge/django--cloudinary--storage-0.3.0-2C3E50?logo=django)](https://pypi.org/project/django-cloudinary-storage/) | Django package that provides Cloudinary storages for both media and static files as well as management commands for removing unnecessary files. |
| 3  | [![Pillow 10.0.1](https://img.shields.io/badge/Pillow-10.0.1-blue?logo=pillow)](https://pypi.org/project/Pillow/) | Adds image processing capabilities to your Python interpreter. |
| 4  | [![asgiref 3.7.2](https://img.shields.io/badge/asgiref-3.7.2-BC7D29)](https://pypi.org/project/asgiref/) | ASGI framework, often used in Django applications. |
| 5  | [![backports.zoneinfo 0.2.1](https://img.shields.io/badge/backports.zoneinfo-0.2.1-0088CC)](https://pypi.org/project/backports.zoneinfo/) | Backports of Python zoneinfo module for working with time zones. |
| 6  | [![cloudinary 1.34.0](https://img.shields.io/badge/cloudinary-1.34.0-FF8800)](https://pypi.org/project/cloudinary/) | Python SDK for Cloudinary, a cloud-based image and video management platform. |
| 7  | [![sqlparse 0.4.4](https://img.shields.io/badge/sqlparse-0.4.4-1A4E8B)](https://pypi.org/project/sqlparse/) | SQL parsing and formatting library for Python. |
| 8  | [![urllib3 1.26.16](https://img.shields.io/badge/urllib3-1.26.16-0055FF)](https://pypi.org/project/urllib3/) | HTTP library for Python, used for making HTTP requests. |
| 9  | [![djangorestframework 3.14.0](https://img.shields.io/badge/djangorestframework-3.14.0-33AADD?logo=django)](https://pypi.org/project/djangorestframework/) | A powerful and flexible toolkit for building Web APIs in Django. |
| 10 | [![black 23.9.1](https://img.shields.io/badge/black-23.9.1-000000)](https://pypi.org/project/black/) | The uncompromising code formatter for Python. |
| 11 | [![click 8.1.7](https://img.shields.io/badge/click-8.1.7-333333)](https://pypi.org/project/click/) | A simple Python module to add command-line interface creation capabilities to your software. |
| 12 | [![pathspec 0.11.2](https://img.shields.io/badge/pathspec-0.11.2-339933)](https://pypi.org/project/pathspec/) | Utility library for gitignore style pattern matching of file paths. |
| 13 | [![pyenchant 3.2.2](https://img.shields.io/badge/pyenchant-3.2.2-FF5500)](https://pypi.org/project/pyenchant/) | A spellchecking library for Python. |

whitenoise - https://pypi.org/project/whitenoise/ 
djangorestframework-simplejwt - https://pypi.org/project/djangorestframework-simplejwt/
dj-rest-auth 5.0.1 - https://pypi.org/project/dj-rest-auth/
drf-social-oauth2 2.1.3 - https://drf-social-oauth2.readthedocs.io/en/latest/ - the main library which enables us oauth2 token based authentication for email password as well as google and facebook

### Database

- the schema
- data models
- guidance on how to migrate and manage the database.

#### *Database schema*

### API Documentation

This Provides documentation on the available endpoints, request/response formats, and authentication methods. 

#### *CRUD tables*

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

1. [Markdown Tips & Tricks 2022 - Markdown Crash Course](https://www.youtube.com/watch?v=ftOBvusMHjQ)
2. [Adding Social Authentication to Django](https://testdriven.io/blog/django-social-auth/)
3. [Email + Social Logins in Django – Step by Step Guide](https://www.geeksforgeeks.org/email-social-logins-in-django-step-by-step-guide/)

### Tools used

| No. | Name                                       | Purpose                                    |
|----|--------------------------------------------|--------------------------------------------|
| 1  | [Shields.io](https://shields.io/badges)  | Create badges. |
| 2  | [Simple Icons](https://simpleicons.org/) | Find and download SVG icons for various brands and products. |

