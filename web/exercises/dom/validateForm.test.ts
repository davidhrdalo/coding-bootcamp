import { describe, expect, it } from "vitest";
import { validateForm } from "./validateForm";

type Values = { name?: string; email?: string; password?: string; terms?: boolean };

function formWith(values: Values): HTMLFormElement {
  const form = document.createElement("form");
  const add = (name: string, value: string, type = "text") => {
    const input = document.createElement("input");
    input.name = name;
    input.type = type;
    input.value = value;
    form.append(input);
  };
  add("name", values.name ?? "");
  add("email", values.email ?? "");
  add("password", values.password ?? "", "password");
  const terms = document.createElement("input");
  terms.type = "checkbox";
  terms.name = "terms";
  terms.checked = values.terms ?? false;
  form.append(terms);
  return form;
}

const valid: Values = { name: "Ada", email: "ada@example.com", password: "longenough", terms: true };

describe("validateForm", () => {
  it("returns no errors for a valid form", () => {
    expect(validateForm(formWith(valid))).toEqual({});
  });

  it("reports every problem at once", () => {
    expect(validateForm(formWith({}))).toEqual({
      name: "Name is required",
      email: "Email is required",
      password: "Password must be at least 8 characters",
      terms: "You must accept the terms",
    });
  });

  it("trims the name", () => {
    expect(validateForm(formWith({ ...valid, name: "   " }))).toEqual({ name: "Name is required" });
  });

  it.each(["plain", "a@b", "a b@c.com", "a@b@c.com", "@b.com", "a@.com"])(
    "rejects the email %s",
    (email) => {
      expect(validateForm(formWith({ ...valid, email }))).toEqual({ email: "Enter a valid email" });
    },
  );

  it("accepts a normal email and trims it", () => {
    expect(validateForm(formWith({ ...valid, email: "  ada@mail.example.org  " }))).toEqual({});
  });

  it("requires 8 characters for the password, exactly", () => {
    expect(validateForm(formWith({ ...valid, password: "1234567" }))).toEqual({
      password: "Password must be at least 8 characters",
    });
    expect(validateForm(formWith({ ...valid, password: "12345678" }))).toEqual({});
  });

  it("requires the terms box to be ticked", () => {
    expect(validateForm(formWith({ ...valid, terms: false }))).toEqual({ terms: "You must accept the terms" });
  });
});
