# 15 - Web fundamentals: HTTP, the browser and REST

Job ads keep asking for "how a web application is built end to end", "HTTP, the DOM, SSL" and "REST APIs".
This note is the whole picture in one page. Practise it in Python week 5 and 6 and in the `web/` track.

## HTTP is just text

A **request** is a request line, headers, a blank line and an optional body:

```
POST /todos HTTP/1.1
Host: api.example.com
Content-Type: application/json
Authorization: Bearer eyJhbGciOi...

{"title": "Buy milk"}
```

A **response** is a status line, headers, a blank line and a body: `HTTP/1.1 201 Created`.
Everything else (HTTPS, HTTP/2, cookies) is detail on top of that. HTTPS is the same text sent through an encrypted TLS tunnel.

- **Methods:** GET (read), POST (create / do something), PUT (replace), PATCH (partial update), DELETE.
- **Idempotent** means doing it ten times has the same effect as once. GET, PUT, DELETE are idempotent. POST is not. This decides which requests are safe to retry automatically.
- **Status codes by family:** 2xx success (200 OK, 201 Created, 204 No Content), 3xx redirect (301, 302), 4xx the client got it wrong (400 bad input, 401 not logged in, 403 not allowed, 404 not found, 409 conflict, 429 slow down), 5xx the server failed (500, 502, 503, 504).
- **401 vs 403:** 401 means "I don't know who you are". 403 means "I know who you are and you may not do this".
- **Headers to know:** `Content-Type`, `Accept`, `Authorization`, `Cache-Control`, `Set-Cookie` / `Cookie`, `Location`, `Retry-After`.
- **URLs:** `https://host:443/path?query=1#fragment`. The fragment is never sent to the server.
- **Cookies** are a header the browser sends back automatically. Flags: `HttpOnly` (JavaScript cannot read it), `Secure` (HTTPS only), `SameSite` (limits cross-site sending, which helps against CSRF). Tokens in an `Authorization` header are sent only when your code adds them. See note 09 for sessions vs JWTs.

## The browser

1. The browser asks DNS for an IP address, opens a TLS connection, sends a GET, and receives HTML.
2. It parses the HTML into the **DOM**, a tree of objects you can read and change with JavaScript.
3. It fetches CSS, scripts and images, then lays the page out and paints it.

- **Events bubble.** A click on a `<span>` inside a `<li>` fires on the span, then the li, then up to the root. **Event delegation** uses this: one listener on the parent, then `event.target.closest(selector)` to find the row. It also covers rows added later.
- **`textContent` vs `innerHTML`.** Set user text with `textContent`. Putting user text into `innerHTML` lets an attacker run script on your page (**XSS**).
- **`fetch` only rejects on network failure.** A 404 or 500 is a normal response: check `response.ok`.
- **CORS:** a browser blocks a page from reading a response from another origin unless that server allows it with `Access-Control-Allow-Origin`. It is enforced by the browser, not the server.
- **Same-origin policy, XSS, CSRF** are the three web security words to be able to explain in two sentences each.

## REST in practice

- **Resources are nouns:** `/todos`, `/todos/42`, `/users/7/posts`. The method is the verb.
- **Status codes carry meaning:** 201 plus a `Location` header on create, 204 on delete, 404 for a missing resource, 405 plus `Allow` for the wrong method, 400 for invalid input, 409 for conflicts.
- **PUT replaces, PATCH changes some fields.** DELETE twice should not be an error for the caller's intent (the end state is the same), though returning 404 the second time is common.
- **Collections need pagination**, filtering and sorting, or one request can return a million rows.
- **Version and validate.** Check input on the server even if the client checks too (anyone can send any request with curl).
- **Rate limiting** protects a service: answer 429 with a `Retry-After` header.
- **Retry safely:** retry idempotent requests on 429 and 5xx with exponential backoff and a limit. Do not auto-retry a POST.

## JWTs in one paragraph

A JSON Web Token is three base64url pieces: `header.payload.signature`. The payload holds **claims** (`sub` who, `exp` expiry, `iat` issued at). Anyone can read a payload: encoding is not encryption. The **signature** proves the issuer created it, and a server must verify the signature (and `exp`, and the audience and issuer) before trusting any claim. This is what Okta hands your app after an OIDC login (see note 09).

## Where to practise

| Topic | Exercises |
|---|---|
| HTTP text, URLs, query strings, cookies, status codes, JWTs | `python/exercises/week5_web_http/` (`python run.py week5`) |
| Routing, CRUD, auth middleware, pagination, rate limiting | `python/exercises/week6_rest_api/` (`python run.py week6`) |
| DOM, events, forms, fetch, retry, debounce | `web/exercises/dom/` and `web/exercises/api/` (`python run.py web-dom`, `web-api`) |

## Say it out loud

1. What happens between typing a URL and seeing a page?
2. What is the difference between 401 and 403? Between PUT and PATCH?
3. What does idempotent mean, and why does it matter for retries?
4. Why does `fetch` not throw on a 404?
5. What is XSS, and what is the one habit that prevents most of it?
6. What is a JWT? Can you trust one you only decoded?
7. What is CORS, and who enforces it?
8. How would you design the endpoints for a to-do app?

## Learn more

- [MDN: HTTP overview](https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview) and [HTTP status codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)
- [MDN: Introduction to the DOM](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/Introduction) and [event bubbling](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting/Event_bubbling)
- [MDN: Using the Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch) and [CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS)
- [jwt.io introduction](https://jwt.io/introduction)
- [OWASP Top Ten](https://owasp.org/www-project-top-ten/)
