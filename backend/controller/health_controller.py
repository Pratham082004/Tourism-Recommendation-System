from utils.responses import success_response

def is_healthy():
    return success_response("API is healthy")

def home():
    return success_response(
        "Welcome to the Tourism Recommendation System",
    )




