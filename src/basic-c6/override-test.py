class SuperClass:
    def hoge(self):
        print("SuperClass.hoge")


class SubClass(SuperClass):   # SuperClassを継承したSubClassを定義
    def hoge(self):   # SuperClassのメソッドと同名のメソッドを定義
        print("SubClass.hoge")


it = SubClass()   # SubClassのインスタンスを作成
it.hoge()   # hoge()メソッドを実行
