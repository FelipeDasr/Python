def todos_params(*args, **kwargs):
    print(f"args: {args}")
    print(f"kwards: {kwargs}")

todos_params("a", "b", "c", legal=True, valor=12.99)
todos_params("Felipe", True, [1, 6, 8], valor=34, pesado=False)