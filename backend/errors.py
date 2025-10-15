from flask import jsonify

class ApiError(Exception):
    status_code = 400
    code = "bad_request"
    def __init__(self, message, status_code=None, code=None, details=None):
        super().__init__(message)
        if status_code: self.status_code = status_code
        if code: self.code = code
        self.details = details
        self.message = message

def register_error_handlers(app):
    @app.errorhandler(ApiError)
    def handle_api_error(err: ApiError):
        payload = {"error": {"code": err.code, "message": str(err)}}
        if err.details: payload["error"]["details"] = err.details
        return jsonify(payload), err.status_code
    @app.errorhandler(404)
    def not_found(_):
        return jsonify({"error": {"code": "not_found", "message": "Resource not found"}}), 404
    @app.errorhandler(405)
    def method_not_allowed(_):
        return jsonify({"error": {"code": "method_not_allowed", "message": "Method not allowed"}}), 405
    @app.errorhandler(500)
    def server_error(_):
        return jsonify({"error": {"code": "internal_server_error", "message": "Internal server error"}}), 500