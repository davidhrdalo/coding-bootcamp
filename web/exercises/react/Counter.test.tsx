import { act, render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { describe, expect, it, vi } from "vitest";
import { Counter } from "./Counter";

const count = () => screen.getByTestId("count");
const button = (name: string) => screen.getByRole("button", { name });

describe("Counter", () => {
  it("starts at the initial value, default 0", () => {
    const { unmount } = render(<Counter />);
    expect(count()).toHaveTextContent("0");
    unmount();
    render(<Counter initial={5} />);
    expect(count()).toHaveTextContent("5");
  });

  it("increments and decrements", async () => {
    const user = userEvent.setup();
    render(<Counter />);
    await user.click(button("Increment"));
    await user.click(button("Increment"));
    await user.click(button("Decrement"));
    expect(count()).toHaveTextContent("1");
  });

  it("stays inside min and max and disables the buttons at the limits", async () => {
    const user = userEvent.setup();
    render(<Counter initial={1} min={0} max={2} />);
    await user.click(button("Increment"));
    expect(count()).toHaveTextContent("2");
    expect(button("Increment")).toBeDisabled();
    await user.click(button("Decrement"));
    await user.click(button("Decrement"));
    expect(count()).toHaveTextContent("0");
    expect(button("Decrement")).toBeDisabled();
    expect(button("Increment")).toBeEnabled();
  });

  it("forces the initial value into range", () => {
    render(<Counter initial={50} max={10} />);
    expect(count()).toHaveTextContent("10");
  });

  it("resets to the initial value", async () => {
    const user = userEvent.setup();
    render(<Counter initial={3} />);
    await user.click(button("Increment"));
    await user.click(button("Reset"));
    expect(count()).toHaveTextContent("3");
  });

  it("calls onChange after each real change, but not on the first render", async () => {
    const user = userEvent.setup();
    const onChange = vi.fn();
    render(<Counter initial={0} max={1} onChange={onChange} />);
    expect(onChange).not.toHaveBeenCalled();
    await user.click(button("Increment"));
    expect(onChange).toHaveBeenLastCalledWith(1);
    await user.click(button("Reset"));
    expect(onChange).toHaveBeenLastCalledWith(0);
    expect(onChange).toHaveBeenCalledTimes(2);
  });

  it("does not call onChange when Reset changes nothing", async () => {
    const user = userEvent.setup();
    const onChange = vi.fn();
    render(<Counter onChange={onChange} />);
    await user.click(button("Reset"));
    expect(onChange).not.toHaveBeenCalled();
  });

  it("adds up two updates made in the same event (functional update)", () => {
    render(<Counter />);
    const inc = button("Increment");
    act(() => {
      inc.click();
      inc.click();
    });
    expect(count()).toHaveTextContent("2");
  });
});
