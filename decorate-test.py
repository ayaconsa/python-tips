

def decorate(f):
    def __wrapper():
        print('デコレート前')
        f()
        # 引数として渡された関数を実行
        print('デコレート後')
    
    return __wrapper

@decorate
def main():
    print('メイン')


if __name__=="__main__":
    main()
