from flask import Blueprint, request

from .data.search_data import USERS


bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200


def search_users(args):
    """Search users database

    Parameters:
        args: a dictionary containing the following search parameters:
            id: string
            name: string
            age: string
            occupation: string

    Returns:
        a list of users that match the search parameters
    """
    x = []
    y = []

    for i in args:
        y.append(i)

    for user in USERS:
        for arg in args:
            if args[arg] == user[arg]:
                x.append(user)   
            elif args[arg] in user[arg]:
                x.append(user)    
            

    return x



def bonus_search(args):
    """
    """
    x = []
    y = []
    list_1 = []
    for i in args:
        y.append(i)

    for user in USERS:
        for arg in args:
            if args[arg] == user[arg]:
                x.append(user)   
            elif args[arg] in user[arg]:
                x.append(user)    

    x.append(list_1)
    return x