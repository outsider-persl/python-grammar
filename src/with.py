class CustomContext:
    def __enter__(self):
        print("Entering the context.")
        return self  # 可以返回自定义对象

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting the context.")
        if exc_type:
            print(f"An error occurred: {exc_value}")


# 使用自定义上下文管理器
with CustomContext() as ctx:
    print("Inside the context.")
    # 可以在这里引发异常来测试异常处理
    # raise ValueError("An error!")  # 注释掉以避免引发异常

raise IOError("An error occurred while working with the file.")