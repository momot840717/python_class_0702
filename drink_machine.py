
class DrinkMachine():
    def __init__(self):
        self.menu = {}


    def add_drinking(self, name, price, stock):
        if name in self.menu:
            self.menu[name]["price"] = price
            self.menu[name]["stock"] += stock
        else:
            self.menu[name] = {
                "price": price, "stock": stock}


    def buy_drinking(self, name):
        if name not in self.menu:
            return f"沒有{name}"
        drink_info = self.menu[name]

        if drink_info['stock'] <= 0:
            return f"{name}已售完"
        
        drink_info['stock'] -= 1
        return f"謝謝購買--{name}, 此次消費 {drink_info['price']} 元"
        
        
    def show_menu(self):
        # 如果是空字典 {} 就會回傳 False, not False 雙重否定 --> True
        if not self.menu:  
            print("沒有庫存")
            return
        print("飲料菜單")
        print("="*35)
        for name, info in self.menu.items():
            print(f"** {name}\t|| 價格: {info["price"]}, 剩餘 {info["stock"]}\t||")
            print("="*35)

    def pop_drinking(self, name):
        return self.menu.pop(name)

