/**
 * React 1: components, props and conditional rendering
 *
 * A component is a function from props to UI. Build <Greeting>:
 *
 *   <Greeting name="Ada" />                 -> <h1>Hello, Ada.</h1>
 *   <Greeting name="Ada" excited />         -> <h1>Hello, Ada!</h1>
 *   <Greeting name="  " />                  -> <h1>Hello, stranger.</h1>
 *   <Greeting name="Ada">Welcome back</Greeting>
 *       -> the h1, then <div data-testid="extra">Welcome back</div>
 *
 * Rules:
 * - The text is "Hello, <who><mark>" where mark is "!" when excited is true, otherwise ".".
 * - who is the trimmed name, or "stranger" when the name is empty after trimming.
 * - Only render the extra <div> when children were passed.
 * - Do not use useState: this component has no state.
 *
 * Concepts: props, default values, children, conditional rendering, fragments.
 */
import type { ReactNode } from "react";

export type GreetingProps = { name: string; excited?: boolean; children?: ReactNode };

export function Greeting(props: GreetingProps) {
  return null;
}
