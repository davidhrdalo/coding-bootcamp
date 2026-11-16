const EMAIL = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

export function validateForm(form: HTMLFormElement): Record<string, string> {
  const data = new FormData(form);
  const text = (key: string) => String(data.get(key) ?? "").trim();
  const errors: Record<string, string> = {};

  if (!text("name")) errors.name = "Name is required";

  const email = text("email");
  if (!email) errors.email = "Email is required";
  else if (!EMAIL.test(email)) errors.email = "Enter a valid email";

  if (String(data.get("password") ?? "").length < 8) {
    errors.password = "Password must be at least 8 characters";
  }
  if (!data.get("terms")) errors.terms = "You must accept the terms";
  return errors;
}
