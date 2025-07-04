class DrinkService:
    def __init__(self, dm_class):
        self.dm_class = dm_class

    def run(self):
        while True:
            print(f"歡迎光臨, 目前飲料如下")
            self.dm_class.show_menu()
            drink_name = input("輸入你要買的飲料名稱:")
            if drink_name == 'admin':
                while True:
                    admin_mode = input("輸入1: 補飲料, 輸入2: 看庫存資訊, 輸入3 移除品項, 輸入0 退出管理模式 --")
                    if admin_mode == '1':
                        self.admin_add_drink()
                    elif admin_mode == '2':
                        self.dm_class.show_menu()
                    elif admin_mode == '3':
                        self.dm_class.show_menu()
                        menu_key = input('輸入要刪除的品項名稱')
                        print(f"成功移除: {self.dm_class.pop_drinking(menu_key)}")
                    elif admin_mode == '0':
                        print('退出管理模式')
                        break
            else:
                print(self.dm_class.buy_drinking(drink_name))

    def admin_add_drink(self):
        print("輸入你要補貨的資訊，如果沒有就在任意處輸入 quit")
        while True:
            name = input('飲料名稱:')
            if (name =='quit'):
                print("完成補貨")
                break
            price = self.input_info('價格')
            if (price =='quit'):
                print("完成補貨")
                break
            stock = self.input_info('數量')
            if (stock =='quit'):
                print("完成補貨")
                break
            self.dm_class.add_drinking(name, price, stock)

    def input_info(self, word):
        while True:
            string = input(f"{word}:")
            if string.isdigit():
                return int(string)
            elif string == 'quit':
                return string
            print('重新輸入')

