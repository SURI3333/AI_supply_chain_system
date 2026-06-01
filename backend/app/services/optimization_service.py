




def optimize(stock, demand):
    reorder = max(demand - stock, 0)

    return {
        "reorder_quantity": reorder,
        "safety_stock": demand * 0.2
    }