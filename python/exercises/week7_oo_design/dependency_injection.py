"""Dependency injection: a session manager you can test

Code that calls time.time() or uuid4() directly is hard to test. Instead PASS IN what it
needs (the clock and the id generator). This is dependency injection.

  sessions = SessionManager(ttl_seconds=60, clock=time.time, id_factory=lambda: "s1")
  sid = sessions.create("ada")        # a new session id from id_factory()
  sessions.get_user(sid)              # "ada" while the session is valid, else None
  sessions.is_valid(sid)
  sessions.revoke(sid)

Rules:
- A session is valid while clock() - created_at < ttl_seconds. At exactly ttl it is expired.
- get_user() returns None for unknown or expired sessions and forgets the expired one.
- touch(sid) restarts the clock for a VALID session and returns True. For an unknown or
  expired session it returns False and does nothing.
- revoke(sid) removes a session. Revoking an unknown id is fine (do nothing).
- Raise ValueError if ttl_seconds <= 0 or the user name is blank.
- If id_factory returns an id that is already in use, raise RuntimeError.

Concepts: dependency injection, test doubles, why "now" and "random" should be parameters.
"""


class SessionManager:
    def __init__(self, ttl_seconds: float, clock, id_factory) -> None:
        raise NotImplementedError

    def create(self, user: str) -> str:
        raise NotImplementedError

    def get_user(self, session_id: str) -> str | None:
        raise NotImplementedError

    def is_valid(self, session_id: str) -> bool:
        raise NotImplementedError

    def touch(self, session_id: str) -> bool:
        raise NotImplementedError

    def revoke(self, session_id: str) -> None:
        raise NotImplementedError
