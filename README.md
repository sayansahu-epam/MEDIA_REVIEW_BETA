## About the Project

The Media Review System is a command-line based application developed in Python that allows users to manage media content such as movies, series, and songs, along with user reviews and ratings. The project is designed to simulate a real-world backend system while remaining simple enough to be operated entirely through a CLI.

The system supports adding media items, searching and listing them, submitting reviews, and viewing aggregated information such as top-rated media and personalized recommendations. Reviews can be added individually or in bulk using a CSV file, making the system suitable for handling larger datasets efficiently.

A key focus of this project is clean architecture and proper separation of concerns. The codebase is organized into layers such as models, services, database access objects (DAO), and utilities. Business logic is kept separate from data persistence and user interaction, which improves readability, maintainability, and extensibility.

The project also demonstrates the use of common design patterns. The Factory Pattern is used to create different types of media objects (Movie, Series, Song) based on input, ensuring centralized and consistent object creation. The Observer Pattern is used to generate notifications when reviews are added, with notifications being stored persistently in a SQLite database and fetched on demand through CLI commands.

Overall, this project serves as a practical example of building a modular, extensible, and well-structured backend application using Python, SQLite, and standard software engineering principles.



## Features

### Media Management
- Add media items such as movies, series, and songs
- List all available media items
- Search media by title
- View top-rated media based on user reviews

### Review Management
- Add a single review for a media item
- Add multiple reviews at once using a CSV file (bulk review)
- View all reviews associated with a specific media item
- Ratings validation to ensure data consistency

### Notifications
- Generate notifications whenever a review is added
- Persist notifications using SQLite
- Fetch notifications on demand for a specific media item via CLI

### Recommendations
- Generate media recommendations for users based on review data
- Display personalized suggestions through CLI commands

### Architecture & Design
- Layered architecture with clear separation of concerns
- Factory Pattern for media object creation
- Observer Pattern for notification generation
- Thread-safe review insertion for improved performance



## Project Structure

The project follows a modular and layered directory structure to maintain clarity, separation of concerns, and ease of maintenance.




MEDIA_REVIEW_SYSTEM/
│
├── media_review.py                # Main CLI entry point
├── media_review.db                # SQLite database file
├── bulk_reviews.csv               # CSV file for bulk review input
├── README.md                      # Project documentation
├── .gitignore                     # Git ignore rules
│
├── cache/
│   ├── redis_client.py            # Redis connection handling
│   └── review_cache.py            # Review caching logic
│
├── database/
│   ├── db_connection.py           # SQLite connection & table creation
│   ├── media_dao.py               # Media database operations
│   ├── review_dao.py              # Review database operations
│   └── user_dao.py                # User database operations
│
├── models/
│   ├── media.py                   # Media models (Media, Movie, Series, Song)
│   ├── review.py                  # Review model
│   └── user.py                    # User model
│
├── patterns/
│   ├── media_factory.py           # Factory Pattern for Media creation
│   └── observer.py                # Observer Pattern implementation
│
├── services/
│   ├── media_service.py           # Media-related business logic
│   ├── review_service.py          # Review handling & threading
│   ├── notification_service.py    # Notification storage and retrieval
│   ├── recommendation_service.py  # Recommendation logic
│   └── user_service.py            # User-related operations
│
├── utils/
│   ├── cli_parser.py              # CLI argument parsing helpers
│   └── thread_manager.py          # Thread management utilities
│
├── tests/
│   ├── conftest.py                # Pytest configuration
│   ├── test_basic.py              # Basic application tests
│   ├── test_cli_basic.py          # CLI command tests
│   ├── test_media_dao.py           # Media DAO tests
│   ├── test_review_dao.py          # Review DAO tests
│   ├── test_user_dao.py            # User DAO tests
│   └── test_media_review.db        # Test database
│
├── venv/                          # Python virtual environment
└── __pycache__/                   # Python cache files



## Architecture & Design Explanation

The Media Review System is designed using a layered architecture to ensure separation of concerns, scalability, and ease of maintenance. Each layer in the system has a clearly defined responsibility, and communication between layers follows a structured flow.

### Layered Architecture

The application is divided into the following layers:

#### 1. CLI Layer
The CLI layer is implemented in `media_review.py`.  
It is responsible for:
- Parsing command-line arguments
- Validating user input at a basic level
- Routing commands to the appropriate service methods

This layer does not contain business logic or database logic.

---

#### 2. Service Layer
The service layer contains the core business logic of the application.  
Files inside the `services/` directory handle operations such as:
- Adding and retrieving media
- Managing reviews
- Generating recommendations
- Handling notifications

The service layer acts as a bridge between the CLI and the database layer and ensures that business rules are applied consistently.

---

#### 3. Model Layer
The model layer defines the domain entities of the system.  
Classes such as `Media`, `Movie`, `Series`, `Song`, `Review`, and `User` represent real-world concepts and define the structure of the data used throughout the application.

Models do not interact directly with the database.

---

#### 4. Database Access Layer (DAO)
The DAO layer, located in the `database/` directory, is responsible for all database interactions.  
Each DAO file handles CRUD operations for a specific entity and uses SQLite as the underlying database.

This layer ensures that SQL logic is isolated from business logic.

---

### Design Patterns Used

#### Factory Pattern
The Factory Pattern is implemented using `MediaFactory`.  
It centralizes the creation of media objects and returns the correct subclass (`Movie`, `Series`, or `Song`) based on the media type. This avoids scattered conditional logic and makes it easy to extend the system with new media types.

---

#### Observer Pattern
The Observer Pattern is used for notification handling.  
When a review is added, a notification event is triggered without tightly coupling the review logic to the notification logic. Notifications are stored persistently in SQLite and can be retrieved later using CLI commands.

This design allows notification behavior to evolve independently of the review system.

---

### Threading & Performance
Review creation uses a thread management utility to handle review insertion asynchronously. This simulates real-world scenarios where write operations may be processed in parallel and ensures that the system remains responsive during bulk operations.

---

### Overall Design Goals
- Loose coupling between components
- High readability and maintainability
- Easy extensibility for future features
- Clear separation of responsibilities
- Practical use of design patterns in a real application

The architecture is intentionally designed to balance simplicity with real-world backend design practices.




## CLI Commands

All functionality in the Media Review System is accessed through command-line arguments using the `media_review.py` script. Only one command is executed at a time.

### The general format is:

```bash
python media_review.py <command> [arguments]



### List All Media

Displays all media items available in the system.

python media_review.py --list



### Search Media by Title

Searches media items whose title matches the given keyword.

python media_review.py --search "<TITLE>"

python media_review.py --search "Inception"



### Add Media

Adds a new media item to the system.

python media_review.py --add-media <MEDIA_ID> "<TITLE>" <TYPE>

python media_review.py --add-media 17 "Blinding Lights" song



### List All Users

Displays all users in the system.

python media_review.py --list-users



### Add User

Adds a new user to the system.

python media_review.py --add-user <USER_ID> "<NAME>"

python media_review.py --add-user <USER_ID> "<NAME>"


### Add Single Review

Adds a review for a specific media item by a user.

python media_review.py --review <USER_ID> <MEDIA_ID> <RATING> "<COMMENT>"

python media_review.py --review 1 17 5 "Great song"



### Bulk Review (CSV)

Adds multiple reviews at once using a CSV file.

Bulk Review (CSV)

Adds multiple reviews at once using a CSV file.

python media_review.py --bulk-review bulk_reviews.csv


CSV file format (header required):

media_id,rating,comment
1,5,Amazing movie
2,4,Very good


### View Reviews for a Media Item

Displays all reviews associated with a specific media item.


python media_review.py --reviews <MEDIA_ID>

python media_review.py --reviews 17


### View Top-Rated Media

Displays media items sorted by average rating.

python media_review.py --top-rated



### Get Recommendations for a User

Displays recommended media items for a given user.

python media_review.py --recommend <USER_ID>

python media_review.py --recommend 1



### View Notifications for a Media Item

Fetches and displays stored notifications related to a specific media item.

python media_review.py --notification <MEDIA_ID>

python media_review.py --notification 1







## Database Design

The Media Review System uses SQLite as its database to keep the application lightweight and easy to set up. The database is file-based and is automatically created when the application is executed. All database tables are initialized inside the `create_tables()` function in `database/db_connection.py`.

The database schema is intentionally simple and focuses on clarity and extensibility.

---

### Users Table

The `users` table stores information about users who interact with the system.

Columns:
- user_id  
- name  

This table is used to identify users who submit reviews and to generate media recommendations.

---

### Media Table

The `media` table stores all media items managed by the system, regardless of type.

Columns:
- media_id  
- title  
- media_type  

The `media_type` field allows the system to support multiple media categories such as movies, series, and songs using a single table.

---

### Reviews Table

The `reviews` table stores user reviews and ratings for media items.

Columns:
- review_id  
- user_id  
- media_id  
- rating  
- comment  

This table connects users and media items and is central to features such as review listing, average rating calculation, and recommendation generation. Rating values are validated at the application level.

---

### Notifications Table

The `notifications` table stores notifications generated when reviews are added.

Columns:
- id  
- media_id  
- message  

Notifications are stored persistently so they can be retrieved later using CLI commands. This allows notifications to remain available even after the application is restarted.

---

### Database Design Principles

- SQLite is used for simplicity and portability
- Each table has a clear, single responsibility
- SQL logic is isolated in DAO modules
- Business logic does not directly access SQL
- The schema is designed to support future enhancements

This database design keeps the system easy to understand while supporting all current features of the application.





## Testing

Testing is used in the Media Review System to ensure that core functionality works correctly and that database operations behave as expected. The project includes automated tests written using the `pytest` framework.

All test files are located in the `tests/` directory.

---

### Testing Approach

The testing strategy focuses on validating:
- Database operations
- Core application logic
- CLI command behavior

Tests are written to be independent, repeatable, and easy to understand.

---

### Test Coverage

The following areas of the application are covered by tests:

- Media database operations  
- Review database operations  
- User database operations  
- Basic CLI command execution  
- General application flow validation  

Each test module targets a specific component of the system.

---

### Test Files

The `tests/` directory contains the following files:

- `conftest.py`  
  Sets up shared fixtures and test configuration.

- `test_basic.py`  
  Contains basic sanity tests to verify that the application initializes correctly.

- `test_cli_basic.py`  
  Tests core CLI commands to ensure they execute without errors.

- `test_media_dao.py`  
  Tests database operations related to media items.

- `test_review_dao.py`  
  Tests database operations related to reviews.

- `test_user_dao.py`  
  Tests database operations related to users.

- `test_media_review.db`  
  A separate SQLite database used exclusively for testing to avoid interfering with production data.

---

### Running Tests

Tests can be executed using the following command:

```bash
pytest





It is recommended to run tests in a virtual environment to ensure dependency isolation.

Testing Principles

Tests use a separate database to prevent data corruption

Database logic is tested independently from CLI logic

Failures are isolated to make debugging easier

The test suite can be extended as new features are added

This testing setup helps maintain stability and confidence as the project evolves.




