from fastapi import FastAPI, HTTPException
from typing import List, Dict
from bson import ObjectId
from database import stocks_collection
from helpers import stock_helper

app = FastAPI(
    title="Stocks API",
    description="API to manage stock data in MongoDB Atlas",
    version="1.0"
)

@app.get("/")
def root():
    return {"message": "Welcome to Stocks API. Use /stocks/ to get all stocks."}

# Create a new stock
@app.post("/stocks/", response_model=Dict)
def create_stock(stock: Dict):
    if "symbol" not in stock or "price" not in stock:
        raise HTTPException(status_code=400, detail="Stock must have 'symbol' and 'price'")
    
    stock["symbol"] = stock["symbol"].upper()
    result = stocks_collection.insert_one(stock)
    new_stock = stocks_collection.find_one({"_id": result.inserted_id})
    return stock_helper(new_stock)

# Get all stocks
@app.get("/stocks/", response_model=List[Dict])
def get_stocks():
    try:
        stocks_cursor = stocks_collection.find()
        stocks = [stock_helper(stock) for stock in stocks_cursor]

        if not stocks:
            raise HTTPException(status_code=404, detail="No stocks found")
        return stocks

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching stocks: {e}")

# Get a stock by symbol
@app.get("/stocks/{stock_symbol}", response_model=Dict)
def get_stock(stock_symbol: str):
    try:
        stock = stocks_collection.find_one({"symbol": stock_symbol.upper()})
        if not stock:
            raise HTTPException(status_code=404, detail=f"Stock '{stock_symbol}' not found")
        return stock_helper(stock)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching stock: {e}")

# Update a stock by ID
@app.put("/stocks/{stock_id}", response_model=Dict)
def update_stock(stock_id: str, stock: Dict):
    try:
        result = stocks_collection.update_one(
            {"_id": ObjectId(stock_id)},
            {"$set": stock}
        )
        if result.modified_count == 1:
            updated_stock = stocks_collection.find_one({"_id": ObjectId(stock_id)})
            return stock_helper(updated_stock)
        raise HTTPException(status_code=404, detail="Stock not found")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Invalid stock ID or update failed: {e}")

# Delete a stock by ID
@app.delete("/stocks/{stock_id}")
def delete_stock(stock_id: str):
    try:
        result = stocks_collection.delete_one({"_id": ObjectId(stock_id)})
        if result.deleted_count == 1:
            return {"message": "Stock deleted successfully"}
        raise HTTPException(status_code=404, detail="Stock not found")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Invalid stock ID or deletion failed: {e}")
