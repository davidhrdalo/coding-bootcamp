import type { ReactNode } from "react";

export type GreetingProps = { name: string; excited?: boolean; children?: ReactNode };

export function Greeting({ name, excited = false, children }: GreetingProps) {
  const who = name.trim() === "" ? "stranger" : name.trim();
  return (
    <>
      <h1>
        Hello, {who}
        {excited ? "!" : "."}
      </h1>
      {children ? <div data-testid="extra">{children}</div> : null}
    </>
  );
}
