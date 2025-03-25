/*
 * Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT.
 */

export type Fetcher = (
  input: RequestInfo | URL,
  init?: RequestInit,
) => Promise<Response>;

type Awaitable<T> = T | Promise<T>;

const DEFAULT_FETCHER: Fetcher = (input, init) => fetch(input, init);

export interface HTTPClientOptions {
  fetcher?: Fetcher;
}

type BeforeRequestHook = (req: Request) => Awaitable<Request | void>;
type RequestErrorHook = (err: unknown, req: Request) => Awaitable<void>;
type ResponseHook = (res: Response, req: Request) => Awaitable<void>;

export class HTTPClient {
  private fetcher: Fetcher;
  private requestHooks: BeforeRequestHook[] = [];
  private requestErrorHooks: RequestErrorHook[] = [];
  private responseHooks: ResponseHook[] = [];

  constructor(private options: HTTPClientOptions = {}) {
    this.fetcher = options.fetcher || DEFAULT_FETCHER;
  }

  async request(request: Request): Promise<Response> {
    let req = request;
    for (const hook of this.requestHooks) {
      const nextRequest = await hook(req);
      if (nextRequest) {
        req = nextRequest;
      }
    }

    try {
      const res = await this.fetcher(req);

      for (const hook of this.responseHooks) {
        await hook(res, req);
      }

      return res;
    } catch (err) {
      for (const hook of this.requestErrorHooks) {
        await hook(err, req);
      }

      throw err;
    }
  }

  /**
   * Registers a hook that is called before a request is made. The hook function
   * can mutate the request or return a new request. This may be useful to add
   * additional information to request such as request IDs and tracing headers.
   */
  addHook(hook: "beforeRequest", fn: BeforeRequestHook): this;
  /**
   * Registers a hook that is called when a request cannot be made due to a
   * network error.
   */
  addHook(hook: "requestError", fn: RequestErrorHook): this;
  /**
   * Registers a hook that is called when a response has been received from the
   * server.
   */
  addHook(hook: "response", fn: ResponseHook): this;
  addHook(
    ...args:
      | [hook: "beforeRequest", fn: BeforeRequestHook]
      | [hook: "requestError", fn: RequestErrorHook]
      | [hook: "response", fn: ResponseHook]
  ) {
    if (args[0] === "beforeRequest") {
      this.requestHooks.push(args[1]);
    } else if (args[0] === "requestError") {
      this.requestErrorHooks.push(args[1]);
    } else if (args[0] === "response") {
      this.responseHooks.push(args[1]);
    } else {
      throw new Error(`Invalid hook type: ${args[0]}`);
    }
    return this;
  }

  /** Removes a hook that was previously registered with `addHook`. */
  removeHook(hook: "beforeRequest", fn: BeforeRequestHook): this;
  /** Removes a hook that was previously registered with `addHook`. */
  removeHook(hook: "requestError", fn: RequestErrorHook): this;
  /** Removes a hook that was previously registered with `addHook`. */
  removeHook(hook: "response", fn: ResponseHook): this;
  removeHook(
    ...args:
      | [hook: "beforeRequest", fn: BeforeRequestHook]
      | [hook: "requestError", fn: RequestErrorHook]
      | [hook: "response", fn: ResponseHook]
  ) {
    let target: unknown[];
    if (args[0] === "beforeRequest") {
      target = this.requestHooks;
    } else if (args[0] === "requestError") {
      target = this.requestErrorHooks;
    } else if (args[0] === "response") {
      target = this.responseHooks;
    } else {
      throw new Error(`Invalid hook type: ${args[0]}`);
    }

    const index = target.findIndex((v) => v === args[1]);
    if (index >= 0) {
      target.splice(index, 1);
    }

    return this;
  }

  clone() {
    const child = new HTTPClient(this.options);
    child.requestHooks = this.requestHooks.slice();
    child.requestErrorHooks = this.requestErrorHooks.slice();
    child.responseHooks = this.responseHooks.slice();

    return child;
  }
}

export function matchContentType(response: Response, pattern: string): boolean {
  if (pattern === "*" || pattern === "*/*") {
    return true;
  }

  const contentType =
    response.headers.get("content-type") ?? "application/octet-stream";

  const idx = contentType.split(";").findIndex((raw) => {
    const ctype = raw.trim();
    if (ctype === pattern) {
      return true;
    }

    const parts = ctype.split("/");
    if (parts.length !== 2) {
      return false;
    }

    return `${parts[0]}/*` === pattern || `*/${parts[1]}` === pattern;
  });

  return idx >= 0;
}

const codeRangeRE = new RegExp("^[0-9]xx$", "i");

export function matchStatusCode(
  response: Response,
  codes: number | string | (number | string)[],
) {
  const actual = `${response.status}`;
  const expectedCodes = Array.isArray(codes) ? codes : [codes];
  if (!expectedCodes.length) {
    return false;
  }

  return expectedCodes.some((ec) => {
    const code = `${ec}`;

    if (code === "default") {
      return true;
    }

    if (!codeRangeRE.test(`${code}`)) {
      return code === actual;
    }

    const expectFamily = code.charAt(0);
    if (!expectFamily) {
      throw new Error("Invalid status code range");
    }

    const actualFamily = actual.charAt(0);
    if (!actualFamily) {
      throw new Error(`Invalid response status code: ${actual}`);
    }

    return actualFamily === expectFamily;
  });
}

export function matchResponse(
  response: Response,
  code: number | string | (number | string)[],
  contentTypePattern: string,
): boolean {
  return (
    matchStatusCode(response, code) &&
    matchContentType(response, contentTypePattern)
  );
}

const headerValRE = /, */;
export function unpackHeaders(headers: Headers): Record<string, string[]> {
  const out: Record<string, string[]> = {};

  for (const [k, v] of headers.entries()) {
    out[k] = v.split(headerValRE);
  }

  return out;
}
