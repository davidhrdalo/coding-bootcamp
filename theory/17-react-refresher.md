# 17 - React refresher

This is a quick tune-up of the React ideas interviews probe. It assumes you have used React or React Native before.
Practise in `web/exercises/react/` (`python run.py web-react`, after `python run.py setup-web`).

## The mental model

**UI is a function of state:** `UI = f(props, state)`. You do not change the page. You change state, and React re-renders the component and works out the smallest DOM update. If you know SwiftUI this is the same idea: `@State` is `useState`, a view's inputs are props, and `Binding` is a value plus a setter you pass down.

## What to be able to explain

- **Props flow down, events flow up.** A parent passes values and callbacks. A child never edits a prop.
- **State updates are scheduled, not immediate.** `setCount(count + 1)` twice in one handler adds 1, because both read the same stale `count`. Use the functional form, `setCount(c => c + 1)`, when the new value depends on the old one.
- **Never mutate state.** Return a new array or object (`[...items, item]`, `{...obj, done: true}`). React compares references, so a mutation can mean no re-render.
- **Derived data is not state.** If you can compute it from props and state (a filtered list, a total), compute it during render. Copying it into state creates two sources of truth that drift apart.
- **Keys** tell React which list item is which. Use a stable id, not the array index, or state (a checked box, a typed value) sticks to the wrong row when the list changes.
- **Controlled inputs:** `value` comes from state and `onChange` updates it. React is the single source of truth for the field.
- **`useEffect`** runs after render to sync with something outside React (network, timers, subscriptions). Return a **cleanup** function. The dependency array lists everything the effect reads. A wrong or missing dependency is the most common hook bug.
- **Race conditions in effects:** if the user changes `userId` quickly, responses can arrive out of order. Guard with an `ignore` flag set in cleanup (or an AbortController).
- **Rules of hooks:** call hooks at the top level, in the same order every render, only from components and custom hooks.
- **Custom hooks** (`useToggle`, `useDebouncedValue`) share stateful logic, not state. Each call gets its own state.
- **Context** passes a value to everything below a provider without prop drilling. Every consumer re-renders when the value changes, so memoise the value you provide.
- **`useReducer`** suits state with several related fields and named updates. The reducer is a pure `(state, action) -> state` function, trivial to unit test.
- **`React.memo`, `useMemo`, `useCallback`** skip work when inputs are unchanged. They only help when props are referentially stable. Measure first, and do not wrap everything.
- **Strict Mode** runs effects twice in development to expose missing cleanup. Do not "fix" that by removing the cleanup.
- **Server vs client rendering** (Next.js): components run on the server by default in the App Router, and `"use client"` opts into browser-only features like state and effects. If you have used Next.js, be ready to explain the difference.

## Testing React

Use React Testing Library, which tests what a user sees, not implementation details.

- Find things the way a user would: `getByRole("button", { name: "Add" })`, `getByLabelText("Email")`, `getByText(...)`. Avoid test ids unless nothing else fits.
- Use `userEvent` (not `fireEvent`) to click and type, and `await findBy...` for things that appear after async work.
- Fake the network by passing a function prop or mocking `fetch`. Never hit a real API in a unit test.

## React Native, the differences that matter

- No DOM. You render `View`, `Text`, `Image`, `ScrollView`, `FlatList` instead of `div`, `span`, `img`, and scrolling lists. Text must be inside `<Text>`.
- Styles are JavaScript objects (`StyleSheet.create`), not CSS. Layout is Flexbox with `flexDirection: "column"` by default.
- Lists use `FlatList` (virtualised) with `keyExtractor`, not `array.map` for long lists.
- Navigation is a library (React Navigation or Expo Router), not URLs and a browser history.
- Platform code: `Platform.OS`, and native modules for things JavaScript cannot do.
- Hooks, state, props, context, reducers and effects all work exactly the same.

## Say it out loud

1. What happens when you call `setState`?
2. Why must you not mutate state? Why use the functional update form?
3. Why are keys needed, and why is the index a bad key?
4. What is the dependency array, and what goes wrong if it is wrong?
5. How do you avoid a race condition when fetching in `useEffect`?
6. When would you use `useReducer` over `useState`? When is `memo` worth it?
7. What is derived state, and why avoid duplicating it?
8. How does React Native differ from React for the web?

## Learn more

- [react.dev: Learn React](https://react.dev/learn) (start with "Thinking in React", "Choosing the State Structure" and "You Might Not Need an Effect")
- [react.dev: Synchronizing with Effects](https://react.dev/learn/synchronizing-with-effects)
- [Testing Library: React](https://testing-library.com/docs/react-testing-library/intro/) and [which query to use](https://testing-library.com/docs/queries/about/#priority)
- [React Native: core components](https://reactnative.dev/docs/components-and-apis)
- [Kent C. Dodds: common testing mistakes](https://kentcdodds.com/blog/common-mistakes-with-react-testing-library)
