class SessionManager:
    def __init__(self, ttl_seconds: float, clock, id_factory) -> None:
        if ttl_seconds <= 0:
            raise ValueError("ttl must be positive")
        self._ttl = ttl_seconds
        self._clock = clock
        self._id_factory = id_factory
        self._sessions = {}

    def _expired(self, started: float) -> bool:
        return self._clock() - started >= self._ttl

    def create(self, user: str) -> str:
        if not user or not user.strip():
            raise ValueError("user is required")
        session_id = self._id_factory()
        if session_id in self._sessions:
            raise RuntimeError("session id already in use")
        self._sessions[session_id] = (user, self._clock())
        return session_id

    def get_user(self, session_id: str) -> str | None:
        entry = self._sessions.get(session_id)
        if entry is None:
            return None
        user, started = entry
        if self._expired(started):
            del self._sessions[session_id]
            return None
        return user

    def is_valid(self, session_id: str) -> bool:
        return self.get_user(session_id) is not None

    def touch(self, session_id: str) -> bool:
        user = self.get_user(session_id)
        if user is None:
            return False
        self._sessions[session_id] = (user, self._clock())
        return True

    def revoke(self, session_id: str) -> None:
        self._sessions.pop(session_id, None)
