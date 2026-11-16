import { act, render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { describe, expect, it, vi } from "vitest";
import { SignupForm } from "./SignupForm";

const email = () => screen.getByLabelText("Email");
const password = () => screen.getByLabelText("Password");
const submit = () => screen.getByRole("button", { name: /sign/i });

function deferred() {
  let resolve!: () => void;
  let reject!: (reason: unknown) => void;
  const promise = new Promise<void>((res, rej) => {
    resolve = res;
    reject = rej;
  });
  promise.catch(() => {});
  return { promise, resolve, reject };
}

describe("SignupForm", () => {
  it("renders the labelled fields and a button", () => {
    render(<SignupForm onSubmit={() => {}} />);
    expect(email()).toBeInTheDocument();
    expect(password()).toHaveAttribute("type", "password");
    expect(submit()).toHaveTextContent("Sign up");
  });

  it("shows every validation error and does not submit", async () => {
    const user = userEvent.setup();
    const onSubmit = vi.fn();
    render(<SignupForm onSubmit={onSubmit} />);
    await user.click(submit());
    const alerts = screen.getAllByRole("alert").map((a) => a.textContent);
    expect(alerts).toEqual(["Enter a valid email", "Password must be at least 8 characters"]);
    expect(onSubmit).not.toHaveBeenCalled();
  });

  it("shows only the errors that apply", async () => {
    const user = userEvent.setup();
    render(<SignupForm onSubmit={vi.fn()} />);
    await user.type(email(), "ada@example.com");
    await user.type(password(), "short");
    await user.click(submit());
    expect(screen.getAllByRole("alert").map((a) => a.textContent)).toEqual(["Password must be at least 8 characters"]);
  });

  it("submits trimmed email and the password, then clears the fields", async () => {
    const user = userEvent.setup();
    const onSubmit = vi.fn();
    render(<SignupForm onSubmit={onSubmit} />);
    await user.type(email(), "  ada@example.com ");
    await user.type(password(), "longenough");
    await user.click(submit());
    expect(onSubmit).toHaveBeenCalledWith({ email: "ada@example.com", password: "longenough" });
    expect(email()).toHaveValue("");
    expect(password()).toHaveValue("");
    expect(screen.queryByRole("alert")).not.toBeInTheDocument();
  });

  it("submits with Enter", async () => {
    const user = userEvent.setup();
    const onSubmit = vi.fn();
    render(<SignupForm onSubmit={onSubmit} />);
    await user.type(email(), "ada@example.com");
    await user.type(password(), "longenough{enter}");
    expect(onSubmit).toHaveBeenCalledTimes(1);
  });

  it("disables the button and shows progress while the promise is pending", async () => {
    const user = userEvent.setup();
    const pending = deferred();
    render(<SignupForm onSubmit={() => pending.promise} />);
    await user.type(email(), "ada@example.com");
    await user.type(password(), "longenough");
    await user.click(submit());
    expect(submit()).toBeDisabled();
    expect(submit()).toHaveTextContent("Signing up...");
    await act(async () => pending.resolve());
    expect(submit()).toBeEnabled();
    expect(submit()).toHaveTextContent("Sign up");
    expect(email()).toHaveValue("");
  });

  it("keeps the input and shows the error when onSubmit rejects", async () => {
    const user = userEvent.setup();
    render(<SignupForm onSubmit={async () => Promise.reject(new Error("email taken"))} />);
    await user.type(email(), "ada@example.com");
    await user.type(password(), "longenough");
    await user.click(submit());
    expect(await screen.findByRole("alert")).toHaveTextContent("Could not sign up: email taken");
    expect(email()).toHaveValue("ada@example.com");
    expect(submit()).toBeEnabled();
  });

  it("clears old errors when you submit again", async () => {
    const user = userEvent.setup();
    render(<SignupForm onSubmit={vi.fn()} />);
    await user.click(submit());
    expect(screen.getAllByRole("alert")).toHaveLength(2);
    await user.type(email(), "ada@example.com");
    await user.type(password(), "longenough");
    await user.click(submit());
    expect(screen.queryByRole("alert")).not.toBeInTheDocument();
  });
});
