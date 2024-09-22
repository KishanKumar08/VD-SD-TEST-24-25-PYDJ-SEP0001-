import time
import threading

class RateLimiter:
    """
    A simple rate limiter that limits the number of requests a user can make within a given time window.

    Attributes:
    -----------
    max_requests : int
        The maximum number of requests a user can make within the time window.
    window : int
        The time window in seconds within which the request count is checked.
    requests : dict
        A dictionary to store timestamps of requests made by each user.

    Methods:
    --------
    allow_request(user_id):
        Returns True if the user is allowed to make a request, otherwise returns False.
    """
    
    def __init__(self, max_requests, window):
        """
        Initializes the RateLimiter with max requests and time window.

        Parameters:
        -----------
        max_requests : int
            The maximum number of requests allowed per user in the time window.
        window : int
            The time window in seconds for rate limiting.
        """
        self.max_requests = max_requests
        self.window = window
        self.lock = threading.Lock()
        self.requests = {}

    def allow_request(self, user_id):
        """
        Checks if a request from the given user_id is allowed based on rate limits.

        Parameters:
        -----------
        user_id : str
            The ID of the user making the request.

        Returns:
        --------
        bool:
            True if the request is allowed, False otherwise.
        """
        with self.lock:
            now = time.time()
            if user_id not in self.requests:
                self.requests[user_id] = []
            
            # Remove outdated requests
            self.requests[user_id] = [t for t in self.requests[user_id] if now - t < self.window]

            # Check if the user is within the allowed request limit
            if len(self.requests[user_id]) < self.max_requests:
                self.requests[user_id].append(now)
                return True
            return False

def simulate_user_requests(rate_limiter, user_id, num_requests, delay):
    """
    Simulates a user making multiple requests and prints the result of each request.

    Parameters:
    -----------
    rate_limiter : RateLimiter
        The rate limiter object to use for limiting requests.
    user_id : str
        The ID of the user making the requests.
    num_requests : int
        The number of requests to simulate.
    delay : float
        Time delay between consecutive requests in seconds.
    """
    for i in range(num_requests):
        allowed = rate_limiter.allow_request(user_id)
        status = "ALLOWED" if allowed else "DENIED"
        print(f"User {user_id} - Request {i+1}: {status}")
        time.sleep(delay)

if __name__ == '__main__':
    rate_limiter = RateLimiter(5, 60)  # 5 requests per 60 seconds

    # Simulate 6 requests for user 'user1' with a delay of 10 seconds between each request
    user_thread = threading.Thread(target=simulate_user_requests, args=(rate_limiter, 'user1', 6, 10))
    user_thread.start()

    # Simulate another user 'user2' making 6 requests with a delay of 12 seconds
    user_thread_2 = threading.Thread(target=simulate_user_requests, args=(rate_limiter, 'user2', 6, 12))
    user_thread_2.start()

    # Join the threads to ensure they complete
    user_thread.join()
    user_thread_2.join()
