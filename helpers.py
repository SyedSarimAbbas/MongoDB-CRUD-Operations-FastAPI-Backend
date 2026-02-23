def stock_helper(stock: dict) -> dict:
    """
    Convert MongoDB stock document into dictionary with only symbol, id, price.
    """
    return {
        "id": str(stock.get("_id")),
        "symbol": stock.get("symbol", ""),
        "price": stock.get("price", 0)
    }
