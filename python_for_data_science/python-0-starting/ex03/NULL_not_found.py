import math


def is_not_object(object: any):

    if type(object) is bool:
        print(f"Fake : {object} {type(object)}")
    elif type(object) is str:
        print(f"Empty: {type(object)}")
    elif type(object) is int:
        print(f"Zero : {object} {type(object)}")


def NULL_not_found(object: any) -> int:

    if isinstance(object, float) and math.isnan(object):
        print(f"Cheese: {object} : {type(object)}")
        return 0
    elif object is None:
        print(f"Nothing: {object} : {type(object)}")
    elif not object:
        is_not_object(object)
    else:
        print("Type not found")
        return 1

    return 0
