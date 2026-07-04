from flask import jsonify
from utils.logger import logger


def success_response(message, data=None, status_code=200):

    response = {
        "success": True,
        "message": message,
    }
    if data is not None:
        response["data"] = data

    logger.debug("success_response message=%s status_code=%s", message, status_code)
    return jsonify(response), status_code


def error_response(message, status_code=400):

    response = {
        "success": False,
        "message": message,
    }
    return jsonify(response), status_code

