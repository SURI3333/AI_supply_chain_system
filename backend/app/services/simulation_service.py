



def simulate(demand_increase, delay):

    revenue_loss = demand_increase * 10000
    delay_cost = delay * 2000

    return {
        "revenue_loss": revenue_loss,
        "delay_cost": delay_cost
    }