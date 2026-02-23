# 📈 Stocks API - FastAPI & MongoDB Atlas

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-00a67d.svg?logo=fastapi)
![MongoDB](https://img.shields.io/badge/MongoDB-Atlas-47A248.svg?logo=mongodb)

A lightweight, blazing-fast REST API built with **FastAPI** and **MongoDB Atlas** for managing stock data. This project serves as a practical implementation of CRUD operations using `pymongo` and provides real-time access to stock symbols, IDs, and prices.

---

## ✨ Features

- **Create**: Add new stocks to the database with validation.
- **Read**: Fetch all stocks or find specific ones by their unique symbol.
- **Update**: Modify existing stock details (prices, symbols) by their MongoDB ID.
- **Delete**: Remove stocks from the database securely.
- **Aggregations**: Includes a Jupyter Notebook demonstrating MongoDB aggregations.
- **Fast & Interactive Docs**: Auto-generated Swagger UI (`/docs`) and ReDoc (`/redoc`) powered by FastAPI.

---

## 📂 Project Structure

```text
├── .venv/                      # Virtual environment (ignored by git usually)
├── Aggregations in MongoDB.ipynb # Bonus: MongoDB Aggregations tutorial notebook
├── database.py                 # MongoDB connection and collection setup
├── helpers.py                  # Helper functions for data serialization
├── main.py                     # FastAPI application and routing logic
├── requirements.txt            # Project dependencies
└── README.md                   # Project documentation
```

---

## 🚀 Getting Started

Follow these instructions to get the project up and running on your local machine.

### Prerequisites

- Python 3.8+ installed
- A **MongoDB Atlas** account (or local MongoDB server)
- `uvicorn` installed globally or in your environment (for running FastAPI)

### 1. Clone the Repository
```bash
git clone <your-repository-url>
cd Practice_01
```

### 2. Set Up a Virtual Environment (Optional but Recommended)
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install Dependencies
Install the required Python packages (`fastapi`, `pymongo`, etc.):
```bash
pip install -r requirements.txt
pip install uvicorn  # Required to run the FastAPI server
```

### 4. Configure MongoDB Credentials
Open `database.py` and update your MongoDB Atlas credentials:
```python
username = "Your Username Here"
password = quote_plus("Your Password Here")
dbName = "stocks_data"
```
> **Security Note:** In a production environment, always use `.env` files (e.g., `python-dotenv`) to manage sensitive credentials!

### 5. Run the Application
Start the FastAPI server using `uvicorn`:
```bash
uvicorn main:app --reload
```
The API will be available at: **http://127.0.0.1:8000**

---

## 📡 API Endpoints

Once the application is running, you can access the interactive Swagger UI documentation at **http://127.0.0.1:8000/docs**.

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/` | Welcome message and API status |
| `POST` | `/stocks/` | Create a new stock (Requires JSON body: `{"symbol": "AAPL", "price": 150}`) |
| `GET` | `/stocks/` | Retrieve a list of all stocks |
| `GET` | `/stocks/{stock_symbol}` | Get the details of a specific stock by its symbol |
| `PUT` | `/stocks/{stock_id}` | Update a specific stock by its MongoDB object ID |
| `DELETE`| `/stocks/{stock_id}` | Delete a specific stock by its MongoDB object ID |

---

## 🛠️ Built With

* **[FastAPI](https://fastapi.tiangolo.com/)** - Modern, fast web framework for building APIs.
* **[MongoDB Atlas](https://www.mongodb.com/cloud/atlas)** - Fully managed cloud database service.
* **[Pymongo](https://pymongo.readthedocs.io/)** - Python driver for MongoDB.
