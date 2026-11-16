/**
 * Validate a form
 *
 * Read a <form> with FormData and return an object of error messages, keyed by field name.
 * Return {} when everything is valid.
 *
 *   validateForm(form) -> { email: "Enter a valid email", terms: "You must accept the terms" }
 *
 * Fields and the EXACT messages:
 *   name      trimmed, must not be empty             "Name is required"
 *   email     trimmed, empty                         "Email is required"
 *             trimmed, not like x@y.z (no spaces,    "Enter a valid email"
 *             one @, a dot after the @)
 *   password  at least 8 characters (not trimmed)    "Password must be at least 8 characters"
 *   terms     a checkbox: must be checked            "You must accept the terms"
 * Only one message per field. A checkbox that is not checked is simply missing from FormData.
 *
 * Concepts: FormData, trimming input, validating on the client (and why servers must check too).
 */
export function validateForm(form: HTMLFormElement): Record<string, string> {
  throw new Error("Not implemented yet");
}
