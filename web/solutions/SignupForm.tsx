import { type FormEvent, useState } from "react";

export type SignupValues = { email: string; password: string };
export type SignupFormProps = { onSubmit: (values: SignupValues) => void | Promise<void> };

const EMAIL = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

export function SignupForm({ onSubmit }: SignupFormProps) {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [errors, setErrors] = useState<string[]>([]);
  const [pending, setPending] = useState(false);

  async function handleSubmit(event: FormEvent) {
    event.preventDefault();
    const trimmed = email.trim();
    const problems: string[] = [];
    if (!EMAIL.test(trimmed)) problems.push("Enter a valid email");
    if (password.length < 8) problems.push("Password must be at least 8 characters");
    setErrors(problems);
    if (problems.length > 0) return;

    setPending(true);
    try {
      await onSubmit({ email: trimmed, password });
      setEmail("");
      setPassword("");
    } catch (error) {
      const message = error instanceof Error ? error.message : String(error);
      setErrors([`Could not sign up: ${message}`]);
    } finally {
      setPending(false);
    }
  }

  return (
    <form onSubmit={handleSubmit}>
      <label>
        Email
        <input value={email} onChange={(e) => setEmail(e.target.value)} />
      </label>
      <label>
        Password
        <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} />
      </label>
      {errors.map((message) => (
        <p key={message} role="alert">
          {message}
        </p>
      ))}
      <button type="submit" disabled={pending}>
        {pending ? "Signing up..." : "Sign up"}
      </button>
    </form>
  );
}
