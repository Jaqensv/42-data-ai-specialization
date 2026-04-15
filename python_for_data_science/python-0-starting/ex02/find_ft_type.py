def all_thing_is_obj(object: any) -> int:

    message = type(object).__name__.capitalize()

    if isinstance(object, str):
        print(f"{object} is in the kitchen : {type(object)}")
    elif type(object) in (list, tuple, set, dict):
        print(f"{message} : {type(object)}")
    else:
        print("Type not found")

    return 42
