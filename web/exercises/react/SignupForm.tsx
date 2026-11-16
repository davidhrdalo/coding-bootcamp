/**
 * React 9: forms, validation and async submit
 *
 *   <SignupForm onSubmit={async ({ email, password }) => { ... }} />
 *
 * Render a <form> with an input labelled "Email", an input labelled "Password"
 * (type="password") and a submit button.
 *
 * Behaviour:
 * - Both inputs are CONTROLLED (value and onChange from state).
 * - On submit call event.preventDefault(), then validate:
 *     email (trimmed) must look like x@y.z       -> <p role="alert">Enter a valid email</p>
 *     password must be at least 8 characters     -> <p role="alert">Password must be at least 8 characters</p>
 *   Show every error that applies. If there are errors, do NOT call onSubmit.
 * - If valid, call onSubmit({ email: trimmedEmail, password }). onSubmit may return a Promise.
 *     While it is pending the button is disabled and reads "Signing up..."; otherwise it reads
 *     "Sign up".
 *     When it resolves, clear both inputs.
 *     If it rejects, keep what the user typed and show
 *     <p role="alert">Could not sign up: {error.message}</p>.
 * - Errors from a previous submit disappear when you submit again.
 *
 * Concepts: controlled forms, preventDefault, validation, async state (pending / error),
 * disabling buttons to stop double submits.
 */
export type SignupValues = { email: string; password: string };
export type SignupFormProps = { onSubmit: (values: SignupValues) => void | Promise<void> };

export function SignupForm(props: SignupFormProps) {
  return null;
}
