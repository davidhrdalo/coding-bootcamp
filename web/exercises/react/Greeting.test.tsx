import { render, screen } from "@testing-library/react";
import { describe, expect, it } from "vitest";
import { Greeting } from "./Greeting";

describe("Greeting", () => {
  it("greets by name with a full stop", () => {
    render(<Greeting name="Ada" />);
    expect(screen.getByRole("heading", { level: 1 })).toHaveTextContent("Hello, Ada.");
  });

  it("uses an exclamation mark when excited", () => {
    render(<Greeting name="Ada" excited />);
    expect(screen.getByRole("heading", { level: 1 })).toHaveTextContent("Hello, Ada!");
  });

  it("trims the name", () => {
    render(<Greeting name="  Ada  " />);
    expect(screen.getByRole("heading")).toHaveTextContent(/^Hello, Ada\.$/);
  });

  it("falls back to stranger for a blank name", () => {
    render(<Greeting name="   " />);
    expect(screen.getByRole("heading")).toHaveTextContent("Hello, stranger.");
  });

  it("renders children in an extra div", () => {
    render(<Greeting name="Ada">Welcome back</Greeting>);
    expect(screen.getByTestId("extra")).toHaveTextContent("Welcome back");
  });

  it("renders no extra div without children", () => {
    render(<Greeting name="Ada" />);
    expect(screen.queryByTestId("extra")).not.toBeInTheDocument();
  });

  it("can render elements as children", () => {
    render(
      <Greeting name="Ada">
        <button>Go</button>
      </Greeting>,
    );
    expect(screen.getByRole("button", { name: "Go" })).toBeInTheDocument();
  });
});
