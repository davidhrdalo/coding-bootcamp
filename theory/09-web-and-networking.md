# 09 - How the web works (HTTP, DNS, auth)

## What happens when you open a URL

1. **DNS** turns the name (`sayelle.app`) into an IP address.
2. Your device opens a **TCP** connection to that address, and **TLS** encrypts it (HTTPS).
3. The browser sends an **HTTP request**; the server replies with a **response** (status, headers, body).
4. The browser renders the response, which may trigger more requests (scripts, images, API calls).

## HTTP essentials

| Method | Meaning | Safe to repeat? |
|---|---|---|
| GET | read | yes |
| POST | create / run an action | no |
| PUT | replace | yes |
| PATCH | partial update | usually |
| DELETE | remove | yes |

Status code families: **2xx** success (200 OK, 201 Created), **3xx** redirect, **4xx** client error
(400 bad request, 401 unauthenticated, 403 forbidden, 404 not found, 429 too many requests),
**5xx** server error (500, 503).

- **REST:** URLs name resources (`/users/42`), methods say what to do, responses are usually JSON.
- **Stateless:** each request carries what the server needs; the server does not remember you between calls.
- **Caching:** headers such as `Cache-Control` let responses be reused. A CDN is a cache near the user.
- **Cookies vs tokens:** cookies are sent automatically by browsers; tokens (such as a JWT) are sent in an `Authorization` header.
- **CORS:** a browser rule that blocks a web page from calling another origin unless that server allows it.

## Authentication vs authorisation

- **Authentication** = who are you? **Authorisation** = what are you allowed to do?
- **OAuth 2.0** is a framework for *delegated authorisation* (an app gets limited access without your password).
- **OpenID Connect (OIDC)** is a thin identity layer on top of OAuth 2.0 that adds an **ID token** proving who logged in. Identity providers such as Okta use it for single sign-on.
- **Tokens:** the *ID token* says who the user is; the *access token* authorises calls to an API; a *refresh token* gets new access tokens. Many are **JWTs** (signed JSON with a header, payload and signature).
- **Authorization Code flow with PKCE** is the recommended flow for browser and mobile apps.
- **SSO (single sign-on):** log in once with an identity provider (Okta), and use many apps.

You can talk about this confidently: it is real, high-scale work on your resume.

## Interview questions

1. What happens when you type a URL into a browser and press Enter?
2. What is the difference between GET and POST? Between 401 and 403?
3. What does "stateless" mean for an API, and why does it matter?
4. What is the difference between OAuth 2.0 and OpenID Connect?
5. How does a JWT work, and how do you know it has not been tampered with?
6. What is CORS?

## Learn more

- [MDN: An overview of HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview)
- [MDN: HTTP response status codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)
- [How DNS works (illustrated comic)](https://howdns.works/)
- [OAuth 2.0 Simplified](https://www.oauth.com/)
- [Okta: OAuth 2.0 and OpenID Connect overview](https://developer.okta.com/docs/concepts/oauth-openid/)
- [JWT introduction](https://jwt.io/introduction)
