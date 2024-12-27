# Task Management API

This API allows users to manage their tasks, including creating, updating, deleting, and marking tasks as complete.  It's built using Django REST framework and provides a RESTful interface for interacting with task data.

## Features

* **User Authentication:** Secure user authentication using JWT (JSON Web Tokens).
* **Task Creation:** Create new tasks with title, description, due date, priority, and status.
* **Task Retrieval:** Retrieve a list of tasks belonging to the authenticated user.
* **Task Update:** Update existing tasks with new information.
* **Task Deletion:** Delete tasks.
* **Task Completion:** Mark tasks as completed.
* **Input Validation:** Robust input validation to ensure data integrity.
* **Error Handling:** Comprehensive error handling with appropriate HTTP status codes.


## Technologies Used

* **Python:** Programming language.
* **Django:** Web framework.
* **Django REST framework:** REST framework for building APIs.
* **djangorestframework-simplejwt:** JWT authentication library.
* **PostgreSQL (Recommended):** Database (other databases may also work).


## Getting Started

1. **Clone the repository:**
   ```bash
   git clone https://github.com/OmarGhoz/Task-Management-API
