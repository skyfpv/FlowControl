from flask_restful import Resource

mockUserAuthorized = {
    "id":1,
    "email":"SuperFastPilot123@host.com",
    "password": "password123",
    "handle":"SuperFastPilot123",
    "color":"ff00ff",
    "profileImageUrl":"https://host.com/api/userurls/123"
}

mockUserUnuthorized = {
    "id":1,
    "handle":"SuperFastPilot123",
    "color":"ff00ff",
    "profileImageUrl":"https://host.com/api/userurls/123"
}

class Users(Resource):
    def get(self):
        users = [mockUserUnuthorized,mockUserUnuthorized,mockUserUnuthorized]
        return {"response" : users}, 200

    def post(self):
        return {"response" : mockUserAuthorized},  201

    def put(self):
        return {"response" : mockUserAuthorized}

    def delete(self):
        return {"response" : mockUserAuthorized}
