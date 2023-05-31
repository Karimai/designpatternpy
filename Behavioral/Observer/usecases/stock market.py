from typing import List, Optional

from pydantic import BaseModel, Field


class Investor(BaseModel):
    name: str

    def update(self, price: float):
        print(f" Dear {self.name}, the price has been updated to {price}!")


class StockMarket(BaseModel):
    stock_price: float = 0
    observers: List[Investor] = []

    def subscribe(self, observer: Investor):
        self.observers.append(observer)

    def unsubscribe(self, observer):
        self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.update(self.stock_price)

    def set_stock_price(self, price: float):
        self.stock_price = price
        self.notify()


if __name__ == "__main__":
    stock_market = StockMarket()

    stock_market.subscribe(Investor(name="Ali"))
    stock_market.subscribe(Investor(name="Karim"))
    stock_market.subscribe(Investor(name="Naghi"))

    stock_market.set_stock_price(10.0)
