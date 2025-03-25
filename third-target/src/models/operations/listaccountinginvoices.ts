/*
 * Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT.
 */

import * as components from "../components";
import * as z from "zod";

export type ListAccountingInvoicesRequest = {
    /**
     * Unique identifier for a company.
     */
    companyId: string;
    /**
     * Page number. [Read more](https://docs.codat.io/using-the-api/paging).
     */
    page?: number | undefined;
    /**
     * Number of records to return in a page. [Read more](https://docs.codat.io/using-the-api/paging).
     */
    pageSize?: number | undefined;
    /**
     * Codat query string. [Read more](https://docs.codat.io/using-the-api/querying).
     */
    query?: string | undefined;
    /**
     * Field to order results by. [Read more](https://docs.codat.io/using-the-api/ordering-results).
     */
    orderBy?: string | undefined;
};

export type ListAccountingInvoicesResponse = {
    httpMeta: components.HTTPMetadata;
    /**
     * Success
     */
    accountingInvoices?: components.AccountingInvoices | undefined;
};

/** @internal */
export namespace ListAccountingInvoicesRequest$ {
    export type Inbound = {
        companyId: string;
        page?: number | undefined;
        pageSize?: number | undefined;
        query?: string | undefined;
        orderBy?: string | undefined;
    };

    export const inboundSchema: z.ZodType<ListAccountingInvoicesRequest, z.ZodTypeDef, Inbound> = z
        .object({
            companyId: z.string(),
            page: z.number().int().default(1),
            pageSize: z.number().int().default(100),
            query: z.string().optional(),
            orderBy: z.string().optional(),
        })
        .transform((v) => {
            return {
                companyId: v.companyId,
                page: v.page,
                pageSize: v.pageSize,
                ...(v.query === undefined ? null : { query: v.query }),
                ...(v.orderBy === undefined ? null : { orderBy: v.orderBy }),
            };
        });

    export type Outbound = {
        companyId: string;
        page: number;
        pageSize: number;
        query?: string | undefined;
        orderBy?: string | undefined;
    };

    export const outboundSchema: z.ZodType<Outbound, z.ZodTypeDef, ListAccountingInvoicesRequest> =
        z
            .object({
                companyId: z.string(),
                page: z.number().int().default(1),
                pageSize: z.number().int().default(100),
                query: z.string().optional(),
                orderBy: z.string().optional(),
            })
            .transform((v) => {
                return {
                    companyId: v.companyId,
                    page: v.page,
                    pageSize: v.pageSize,
                    ...(v.query === undefined ? null : { query: v.query }),
                    ...(v.orderBy === undefined ? null : { orderBy: v.orderBy }),
                };
            });
}

/** @internal */
export namespace ListAccountingInvoicesResponse$ {
    export type Inbound = {
        HttpMeta: components.HTTPMetadata$.Inbound;
        AccountingInvoices?: components.AccountingInvoices$.Inbound | undefined;
    };

    export const inboundSchema: z.ZodType<ListAccountingInvoicesResponse, z.ZodTypeDef, Inbound> = z
        .object({
            HttpMeta: components.HTTPMetadata$.inboundSchema,
            AccountingInvoices: components.AccountingInvoices$.inboundSchema.optional(),
        })
        .transform((v) => {
            return {
                httpMeta: v.HttpMeta,
                ...(v.AccountingInvoices === undefined
                    ? null
                    : { accountingInvoices: v.AccountingInvoices }),
            };
        });

    export type Outbound = {
        HttpMeta: components.HTTPMetadata$.Outbound;
        AccountingInvoices?: components.AccountingInvoices$.Outbound | undefined;
    };

    export const outboundSchema: z.ZodType<Outbound, z.ZodTypeDef, ListAccountingInvoicesResponse> =
        z
            .object({
                httpMeta: components.HTTPMetadata$.outboundSchema,
                accountingInvoices: components.AccountingInvoices$.outboundSchema.optional(),
            })
            .transform((v) => {
                return {
                    HttpMeta: v.httpMeta,
                    ...(v.accountingInvoices === undefined
                        ? null
                        : { AccountingInvoices: v.accountingInvoices }),
                };
            });
}
