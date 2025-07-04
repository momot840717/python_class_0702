from drink_machine import DrinkMachine
from drink_service import DrinkService


def main():
    # 實例化
    dm_class = DrinkMachine()
    service = DrinkService(dm_class)
    service.run()



"""
只有 __name__ 等於 '__main__'
就是在 drink_main.py 執行程式時 main()才會被啟動
如果在其他頁面執行 if 就判定 False 不會執行 main()
"""
# print(__name__)
if __name__ == '__main__':
    main()