# Employee Management Authentication API

This Employee Management Authentication API provides endpoints for user authentication, including signup, login, reset password, and forget password functionalities.

## Table of Contents
- [Installation](#installation)
- [Environment Variables](#environment-variables)
- [Running the Server](#running-the-server)
- [API Endpoints](#api-endpoints)
  - [Signup](#1-signup)
  - [Login](#2-login)
  - [Forget Password](#3-forget-password)
  - [Reset Password](#4-reset-password)
- [License](#license)

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Employee_Management_Auth.git
   cd Backend
   activate venv
   
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. python manage.py migrate
   ```

## Environment Variables

Create a `.env` file in the root of your project directory and add the following variables:

```plaintext
SECRET_KEY=your_secret_key
DEBUG=True
EMAIL_HOST=email_host
EMAIL_PORT=email_port
EMAIL_HOST_USER=email_user
EMAIL_HOST_PASSWORD=email_password
EMAIL_USE_TLS=True
```

## Running the Server

To start the development server, use:
```bash
cd backend

```bash
python manage.py runserver
```

The server should now be running at `http://localhost:8000`.

## API Endpoints

### 1. Signup
- **URL**: `http://localhost:8000/api/signup/`
- **Method**: `POST`
- **Description**: Creates a new user account.

**Request Body:**
```json
{
  "name": "John Doe",
  "email": "johndoe@example.com",
  "password": "password123"
}
```

**Response:**
```json
{
  "message": "User created successfully",
  "user_id": "1"
}
```

### 2. Login
- **URL**: `http://localhost:8000/api/login/`
- **Method**: `POST`
- **Description**: Authenticates the user and returns a token.

**Request Body:**
```json
{
  "email": "johndoe@example.com",
  "password": "password123"
}
```

**Response:**
```json
{
  "token": "jwt_token_here",
  "message": "Login successful"
}
```

### 3. Forget Password
- **URL**: `http://localhost:8000/api/forget-password/`
- **Method**: `POST`
- **Description**: Sends an email to the user with a password reset link.

**Request Body:**
```json
{
  "email": "johndoe@example.com"
}
```

**Response:**
```json
{
  "message": "Password reset link sent to email"
}
```

### 4. Reset Password
- **URL**: `http://localhost:8000/api/reset-password/<token>/`
- **Method**: `POST`
- **Description**: Resets the user's password using the token sent in the email.

**Request Body:**
```json
{
  "new_password": "newpassword123"
}
```

**Response:**
```json
{
  "message": "Password reset successful"
}
```

---

## License

by Wiseman Kamanga CSR LTD
