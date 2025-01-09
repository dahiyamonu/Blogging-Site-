from django.utils.timezone import now

# class LogRequestsMiddleware:
#     def __init__(self, get_response):

#         self.get_response = get_response
    
#     def __call__(self, request):
#         print(f"[{now()}]  {request.method} request to {request.path}" )

#         response = self.get_response(request)
#         return response

class SessionStorageMiddleware:
    """
    Middleware to handle session storage and log session creation.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Log session details
        if not request.session.session_key:
            print(f"New session created at {now()}")
            request.session['created_at'] = str(now())

        # Store custom session data
        request.session['last_accessed'] = str(now())
        print(f"Session Key: {request.session.session_key}")
        print(f"Session Data: {request.session.items()}")

        # Continue processing the request
        response = self.get_response(request)

        # Perform any session-related cleanup if needed
        return response