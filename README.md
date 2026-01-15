# Crypto Project

This project demonstrates a secure client-server architecture with robust cryptographic features, built using **FastAPI** (Backend) and **React** (Frontend).

## 🔒 Security Features

This application implements several core security best practices and cryptographic mechanisms:

*   **Bcrypt Password Hashing**: User passwords are never stored in plain text. We use the **Bcrypt** hashing algorithm (via `passlib`) to securely hash passwords before storage. This protects against rainbow table attacks and brute-force attempts.
*   **JWT Authentication**: Stateless authentication is handled using **JSON Web Tokens (JWT)**. Upon login, a signed token is issued containing the user's identity and role. This token is verified on every protected API request, ensuring secure access without server-side sessions.
*   **Role-Based Access Control (RBAC)**: The system distinguishes between different user roles (e.g., `user`, `admin`). API endpoints are protected to ensure that only authorized roles can perform sensitive actions.
*   **OTP Verification**: High-security actions like **Registration** and **Password Reset** require email-based One-Time Password (OTP) verification, proving ownership of the registered email address.
*   **Input Validation**: All incoming data is rigorously validated using **Pydantic** schemas. This prevents injection attacks and ensures data integrity by enforcing strict type and format checks (e.g., valid email formats).
*   **CORS Configuration**: Cross-Origin Resource Sharing (CORS) is explicitly configured to allow requests only from trusted frontend origins, preventing unauthorized cross-site requests.

## 🚀 How to Run

### prerequisites
- **Python 3.9+**
- **Node.js 16+**

### 1. Backend (Server)

Navigate to the `server` directory and install the dependencies:

```bash
cd server
pip install -r requirements.txt
```

Run the FastAPI server:

```bash
uvicorn src.main:app --reload
```

The server will start at `http://127.0.0.1:8000`.
- API Docs: `http://127.0.0.1:8000/docs`

### 2. Frontend (Client)

Open a new terminal, navigate to the `client` directory, and install dependencies:

```bash
cd client
npm install
```

Start the React development server:

```bash
npm start
```

The application will open at `http://localhost:3000`.

## 🧪 Running Tests

To run the backend test suite:

```bash
cd server
pytest
```
