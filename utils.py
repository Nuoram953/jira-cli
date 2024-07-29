def run_all_or_specific(self, prefix, func_name=None, order=None):
    if func_name is None:
        if order:
            for func in order:
                getattr(self, func)()
            return

        for attr in dir(self):
            if callable(getattr(self, attr)) and attr.startswith(prefix):
                getattr(self, attr)()
    else:
        full_function_name = prefix + func_name
        if hasattr(self, full_function_name) and callable(getattr(self, full_function_name)):
            getattr(self, full_function_name)()
        else:
            print(f"No method named {func_name}")
