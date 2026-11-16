import { useEffect, useState } from "react";

export type User = { name: string; email: string };
export type UserProfileProps = { userId: string; fetchUser: (id: string) => Promise<User> };

type State = { status: "loading" } | { status: "error"; message: string } | { status: "ok"; user: User };

export function UserProfile({ userId, fetchUser }: UserProfileProps) {
  const [state, setState] = useState<State>({ status: "loading" });

  useEffect(() => {
    let ignore = false;
    setState({ status: "loading" });
    fetchUser(userId).then(
      (user) => {
        if (!ignore) setState({ status: "ok", user });
      },
      (error: unknown) => {
        if (!ignore) setState({ status: "error", message: error instanceof Error ? error.message : String(error) });
      },
    );
    return () => {
      ignore = true;
    };
  }, [userId, fetchUser]);

  if (state.status === "loading") return <p>Loading...</p>;
  if (state.status === "error") return <p role="alert">Something went wrong: {state.message}</p>;
  return (
    <div>
      <h2>{state.user.name}</h2>
      <p>{state.user.email}</p>
    </div>
  );
}
