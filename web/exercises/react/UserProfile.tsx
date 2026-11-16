/**
 * React 6: fetching data with useEffect (and the race condition)
 *
 *   <UserProfile userId="1" fetchUser={(id) => Promise<{ name: string; email: string }>} />
 *
 * Render:
 * - While loading:  <p>Loading...</p>
 * - On success:     <h2>{name}</h2> and <p>{email}</p>
 * - On failure:     <p role="alert">Something went wrong: {message}</p>
 *                   (message is error.message, or String(error) if it is not an Error)
 *
 * Behaviour:
 * - Fetch when the component mounts and again whenever userId changes. Show the loading text
 *   again while the new user loads.
 * - IGNORE stale results. If userId changes from "1" to "2" and the answer for "1" arrives
 *   AFTER the answer for "2", the screen must still show user 2. Use a flag in the effect
 *   and set it in the cleanup function.
 * - Do not update state after the component has unmounted.
 * - Assume fetchUser is a stable function (the dependency list is [userId, fetchUser]).
 *
 * Concepts: useEffect, cleanup functions, race conditions, loading/error/success states.
 */
export type User = { name: string; email: string };
export type UserProfileProps = { userId: string; fetchUser: (id: string) => Promise<User> };

export function UserProfile(props: UserProfileProps) {
  return null;
}
