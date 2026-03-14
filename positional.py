def greet( *args, **kwargs ):
  for name in *args:
    print(f"Hi {name}")
    
  for key, value in **kwargs:
    print(f"{key} = {value}")
