/*
 * Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT.
 */

import { LendingTsCore } from "../core.js";
import {
  encodeJSON as encodeJSON$,
  encodeSimple as encodeSimple$,
} from "../lib/encodings.js";
import * as m$ from "../lib/matchers.js";
import * as schemas$ from "../lib/schemas.js";
import { RequestOptions } from "../lib/sdks.js";
import { extractSecurity, resolveGlobalSecurity } from "../lib/security.js";
import { pathToFunc } from "../lib/url.js";
import * as components from "../models/components/index.js";
import {
  ConnectionError,
  InvalidRequestError,
  RequestAbortedError,
  RequestTimeoutError,
  UnexpectedClientError,
} from "../models/errors/httpclienterrors.js";
import * as errors from "../models/errors/index.js";
import { SDKError } from "../models/errors/sdkerror.js";
import { SDKValidationError } from "../models/errors/sdkvalidationerror.js";
import * as operations from "../models/operations/index.js";
import { Result } from "../types/fp.js";

/**
 * Update company
 *
 * @remarks
 * Use the *Update company* endpoint to update both the name and description of the company.
 * If you use [groups](https://docs.codat.io/lending-api#/schemas/Group) to manage a set of companies, use the [Add company](https://docs.codat.io/lending-api#/operations/add-company-to-group) or [Remove company](https://docs.codat.io/lending-api#/operations/remove-company-from-group) endpoints to add or remove a company from a group.
 *
 * A [company](https://docs.codat.io/lending-api#/schemas/Company) represents a business sharing access to their data.
 * Each company can have multiple [connections](https://docs.codat.io/lending-api#/schemas/Connection) to different data sources, such as one connection to Xero for accounting data, two connections to Plaid for two bank accounts, and a connection to Zettle for POS data.
 */
export async function companiesUpdate(
  client$: LendingTsCore,
  companyId: string,
  companyRequestBody?: components.CompanyRequestBody | undefined,
  options?: RequestOptions,
): Promise<
  Result<
    operations.UpdateCompanyResponse,
    | errors.ErrorMessage
    | SDKError
    | SDKValidationError
    | UnexpectedClientError
    | InvalidRequestError
    | RequestAbortedError
    | RequestTimeoutError
    | ConnectionError
  >
> {
  const input$: operations.UpdateCompanyRequest = {
    companyId: companyId,
    companyRequestBody: companyRequestBody,
  };

  const parsed$ = schemas$.safeParse(
    input$,
    (value$) => operations.UpdateCompanyRequest$outboundSchema.parse(value$),
    "Input validation failed",
  );
  if (!parsed$.ok) {
    return parsed$;
  }
  const payload$ = parsed$.value;
  const body$ = encodeJSON$("body", payload$.CompanyRequestBody, {
    explode: true,
  });

  const pathParams$ = {
    companyId: encodeSimple$("companyId", payload$.companyId, {
      explode: false,
      charEncoding: "percent",
    }),
  };

  const path$ = pathToFunc("/companies/{companyId}")(pathParams$);

  const headers$ = new Headers({
    "Content-Type": "application/json",
    Accept: "application/json",
  });

  const authHeader$ = await extractSecurity(client$.options$.authHeader);
  const security$ = authHeader$ == null ? {} : { authHeader: authHeader$ };
  const context = {
    operationID: "update-company",
    oAuth2Scopes: [],
    securitySource: client$.options$.authHeader,
  };
  const securitySettings$ = resolveGlobalSecurity(security$);

  const requestRes = client$.createRequest$(context, {
    security: securitySettings$,
    method: "PUT",
    path: path$,
    headers: headers$,
    body: body$,
    timeoutMs: options?.timeoutMs || client$.options$.timeoutMs || -1,
  }, options);
  if (!requestRes.ok) {
    return requestRes;
  }
  const request$ = requestRes.value;

  const doResult = await client$.do$(request$, {
    context,
    errorCodes: ["401", "402", "403", "404", "429", "4XX", "500", "503", "5XX"],
    retryConfig: options?.retries
      || client$.options$.retryConfig
      || {
        strategy: "backoff",
        backoff: {
          initialInterval: 500,
          maxInterval: 60000,
          exponent: 1.5,
          maxElapsedTime: 3600000,
        },
        retryConnectionErrors: true,
      },
    retryCodes: options?.retryCodes || ["408", "429", "5XX"],
  });
  if (!doResult.ok) {
    return doResult;
  }
  const response = doResult.value;

  const responseFields$ = {
    HttpMeta: { Response: response, Request: request$ },
  };

  const [result$] = await m$.match<
    operations.UpdateCompanyResponse,
    | errors.ErrorMessage
    | SDKError
    | SDKValidationError
    | UnexpectedClientError
    | InvalidRequestError
    | RequestAbortedError
    | RequestTimeoutError
    | ConnectionError
  >(
    m$.json(200, operations.UpdateCompanyResponse$inboundSchema, {
      key: "Company",
    }),
    m$.jsonErr(
      [401, 402, 403, 404, 429, 500, 503],
      errors.ErrorMessage$inboundSchema,
    ),
    m$.fail(["4XX", "5XX"]),
  )(response, request$, { extraFields: responseFields$ });
  if (!result$.ok) {
    return result$;
  }

  return result$;
}
