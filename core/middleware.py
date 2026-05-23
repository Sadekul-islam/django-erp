"""
Branch Isolation Middleware

এই middleware এর কাজ:

✅ logged-in user detect করা
✅ user.branch বের করা
✅ request.branch এ attach করা
"""

# =====================================================
# Branch Middleware
# =====================================================
class BranchMiddleware:

    """
    Request এর সাথে current branch attach করবে
    """

    # =============================================
    # middleware initialize
    # =============================================
    def __init__(self, get_response):

        self.get_response = get_response

    # =============================================
    # request processing
    # =============================================
    def __call__(self, request):

        # default branch None
        request.branch = None

        # =========================================
        # user login থাকলে
        # =========================================
        if request.user.is_authenticated:

            # user এর branch request এ attach
            request.branch = request.user.branch

        # next middleware/view
        response = self.get_response(request)

        return response