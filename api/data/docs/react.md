# React (software)

React (also known as React.js or ReactJS) is a free and open-source front-end JavaScript library that aims to make building user interfaces based on components more "seamless". It is maintained by Meta (formerly Facebook) and a community of individual developers and companies. According to the 2025 Stack Overflow Developer Survey, React is one of the most commonly used web technologies. Based on W3Techs, it is used by 6% of all websites.

React can be used to develop single-page, mobile, or server-rendered applications with frameworks like Next.js and React Router. Because React is only concerned with the user interface and rendering components to the DOM, React applications often rely on libraries for routing and other client-side functionality. A key advantage of React is that it – by default – only re-renders those parts of the page that have changed, avoiding unnecessary re-rendering of unchanged DOM elements. React is used by an estimated 6% of all websites.

React adheres to the declarative programming paradigm. Developers design views for each state of an application, and React updates and renders components when data changes. This is in contrast with imperative programming.

React code is made of entities called components. These components are modular and can be reused. React applications typically consist of many layers of components. The components are rendered to a root element in the DOM using the React DOM library. When rendering a component, values are passed between components through props (short for "properties"). Values internal to a component are called its state.

The two primary ways of declaring components in React are through function components and class components. Since React v16.8, using function components is the recommended way.

Function components, announced at React Conf 2018, and available since React v16.8, are declared with a function that accepts a single "props" argument and returns JSX (JavaScript XML). Function components can use internal state with the useState Hook.

On February 16, 2019, React 16.8 was released to the public, introducing React Hooks. Hooks are functions that let developers "hook into" React state and lifecycle features from function components. Notably, Hooks do not work inside classes — they let developers use more features of React without classes.

React provides several built-in hooks such as useState, useContext, useReducer, useMemo and useEffect. Others are documented in the Hooks API Reference. useState and useEffect, which are the most commonly used, are for controlling state and side effects, respectively.

There are two rules of hooks which describe the characteristic code patterns that hooks rely on:

"Only call hooks at the top level" — do not call hooks from inside loops, conditions, or nested statements so that the hooks are called in the same order each render.

"Only call hooks from React functions" — do not call hooks from plain JavaScript functions so that stateful logic stays with the component.

Although these rules cannot be enforced at runtime, code analysis tools such as linters can be configured to detect many mistakes during development. The rules apply to both usage of Hooks and the implementation of custom Hooks, which may call other Hooks.

React Server Components (RSC) are function components that run exclusively on the server.  The concept was first introduced in the talk "Data Fetching with Server Components".

Currently, server components are most readily usable with Next.js. With Next.js, it's possible to write components for both the server and the client (browser). When a server rendered component is received by the browser, React in the browser takes over and creates the virtual DOM and attaches event handlers. This is called hydration.

Under the hood, the server sends a RSC payload, which is a compact and serialized representation of the rendered React Server Components tree. It's used by React on the client to update the browser's DOM.

Though a similar concept to Server Side Rendering, RSCs do not send corresponding JavaScript to the client as no hydration occurs. As a result, they have no access to hooks. However, they may be asynchronous function, allowing them to directly perform asynchronous operations:

Class components are declared using ES6 classes. They behave the same way that function components do, but instead of using Hooks to manage state and lifecycle events, they use the lifecycle methods on the React.Component base class.

React itself does not come with built-in support for routing. React is primarily a library for building user interfaces, and it does not include a full-fledged routing solution out of the box. Third-party libraries can be used to handle routing in React applications, such as React Router. It allows the developer to define routes, manage navigation, and handle URL changes in a React-friendly way.

Another notable feature is the use of a virtual Document Object Model, or Virtual DOM. React creates an in-memory data-structure, similar to the browser DOM. Every time components are rendered, the result is compared with the virtual DOM. It then updates the browser's displayed DOM efficiently with only the computed differences. This process is called reconciliation. This allows the programmer to write code as if the entire page is rendered on each change, while React only renders the components that actually change. This selective rendering provides a major performance boost.

When ReactDOM.render is called again for the same component and target, React represents the new UI state in the Virtual DOM and determines which parts (if any) of the living DOM needs to change.

Lifecycle methods for class-based components use a form of hooking that allows the execution of code at set points during a component's lifetime.

ShouldComponentUpdate allows the developer to prevent unnecessary re-rendering of a component by returning false if a render is not required.

componentDidMount is called once the component has "mounted" (the component has been created in the user interface, often by associating it with a DOM node). This is commonly used to trigger data loading from a remote source via an API.

componentDidUpdate is invoked immediately after updating occurs.

componentWillUnmount is called immediately before the component is torn down or "unmounted". This is commonly used to clear resource-demanding dependencies to the component that will not simply be removed with the unmounting of the component (e.g., removing any setInterval() instances that are related to the component, or an "eventListener" set on the "document" because of the presence of the component)

render is the most important lifecycle method and the only required one in any component. It is usually called every time the component's state is updated, which should be reflected in the user interface.

Source: https://en.wikipedia.org/wiki/React_%28software%29 (Wikipedia, CC BY-SA 4.0)
