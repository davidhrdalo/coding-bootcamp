import { act, render, screen } from "@testing-library/react";
import { describe, expect, it, vi } from "vitest";
import { type User, UserProfile } from "./UserProfile";

function deferred<T>() {
  let resolve!: (value: T) => void;
  let reject!: (reason: unknown) => void;
  const promise = new Promise<T>((res, rej) => {
    resolve = res;
    reject = rej;
  });
  promise.catch(() => {}); // a rejection nobody listens to must not crash the test run
  return { promise, resolve, reject };
}

const ada: User = { name: "Ada Lovelace", email: "ada@example.com" };
const bob: User = { name: "Bob Barker", email: "bob@example.com" };

describe("UserProfile", () => {
  it("shows loading, then the user", async () => {
    const fetchUser = vi.fn(async () => ada);
    render(<UserProfile userId="1" fetchUser={fetchUser} />);
    expect(screen.getByText("Loading...")).toBeInTheDocument();
    expect(await screen.findByRole("heading", { name: "Ada Lovelace" })).toBeInTheDocument();
    expect(screen.getByText("ada@example.com")).toBeInTheDocument();
    expect(screen.queryByText("Loading...")).not.toBeInTheDocument();
    expect(fetchUser).toHaveBeenCalledWith("1");
    expect(fetchUser).toHaveBeenCalledTimes(1);
  });

  it("shows an error message when the fetch fails", async () => {
    const fetchUser = vi.fn(async () => {
      throw new Error("boom");
    });
    render(<UserProfile userId="1" fetchUser={fetchUser} />);
    expect(await screen.findByRole("alert")).toHaveTextContent("Something went wrong: boom");
  });

  it("copes with a rejection that is not an Error", async () => {
    const fetchUser = vi.fn(() => Promise.reject("plain text"));
    render(<UserProfile userId="1" fetchUser={fetchUser} />);
    expect(await screen.findByRole("alert")).toHaveTextContent("Something went wrong: plain text");
  });

  it("fetches again and shows loading when userId changes", async () => {
    const second = deferred<User>();
    const fetchUser = vi.fn((id: string) => (id === "1" ? Promise.resolve(ada) : second.promise));
    const { rerender } = render(<UserProfile userId="1" fetchUser={fetchUser} />);
    await screen.findByText("Ada Lovelace");
    rerender(<UserProfile userId="2" fetchUser={fetchUser} />);
    expect(screen.getByText("Loading...")).toBeInTheDocument();
    expect(screen.queryByText("Ada Lovelace")).not.toBeInTheDocument();
    await act(async () => second.resolve(bob));
    expect(await screen.findByText("Bob Barker")).toBeInTheDocument();
    expect(fetchUser).toHaveBeenCalledTimes(2);
  });

  it("ignores a stale response that arrives after a newer one (race condition)", async () => {
    const slow = deferred<User>();
    const fast = deferred<User>();
    const fetchUser = vi.fn((id: string) => (id === "1" ? slow.promise : fast.promise));
    const { rerender } = render(<UserProfile userId="1" fetchUser={fetchUser} />);
    rerender(<UserProfile userId="2" fetchUser={fetchUser} />);
    await act(async () => fast.resolve(bob));
    expect(await screen.findByText("Bob Barker")).toBeInTheDocument();
    await act(async () => slow.resolve(ada));
    expect(screen.getByText("Bob Barker")).toBeInTheDocument();
    expect(screen.queryByText("Ada Lovelace")).not.toBeInTheDocument();
  });

  it("ignores a stale failure too", async () => {
    const slow = deferred<User>();
    const fast = deferred<User>();
    const fetchUser = vi.fn((id: string) => (id === "1" ? slow.promise : fast.promise));
    const { rerender } = render(<UserProfile userId="1" fetchUser={fetchUser} />);
    rerender(<UserProfile userId="2" fetchUser={fetchUser} />);
    await act(async () => fast.resolve(bob));
    await act(async () => slow.reject(new Error("old failure")));
    expect(screen.queryByRole("alert")).not.toBeInTheDocument();
    expect(screen.getByText("Bob Barker")).toBeInTheDocument();
  });

  it("does not update after unmount", async () => {
    const pending = deferred<User>();
    const errors = vi.spyOn(console, "error").mockImplementation(() => {});
    const { unmount } = render(<UserProfile userId="1" fetchUser={() => pending.promise} />);
    unmount();
    await act(async () => pending.resolve(ada));
    expect(errors).not.toHaveBeenCalled();
    errors.mockRestore();
  });
});
