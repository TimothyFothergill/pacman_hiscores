import pymongo

client = pymongo.MongoClient("mongodb://0.0.0.0:5001")
db = client["hiscores"]
col = db["latest"]


def add_to_database(username, score, email, image_data):
    col.insert({"username": username, "score": score, "email": email, "image_data": image_data})
    return 1


def remove_from_database():
    pass


def show_all_database_documents():
    col_list = col.find()
    return col_list
