def demo(a, b=10, *args, **kwargs):
    print(f"a = {a}, b = {b}")
    print(f"args = {args}")
    print(f"kwargs = {kwargs}")


demo(5, 20, 30, 40, key="key", value="value")
# 输出:
# a = 5, b = 20
# args = (30, 40)
# kwargs = {'key1': 'value1', 'key2': 'value2'}
