/*
 * Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT.
 */

import * as components from "../components";
import * as z from "zod";

export type ListCommerceProductCategoriesRequest = {
    /**
     * Unique identifier for a company.
     */
    companyId: string;
    /**
     * Unique identifier for a connection.
     */
    connectionId: string;
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

export type ListCommerceProductCategoriesResponse = {
    httpMeta: components.HTTPMetadata;
    /**
     * OK
     */
    commerceProductCategories?: components.CommerceProductCategories | undefined;
};

/** @internal */
export namespace ListCommerceProductCategoriesRequest$ {
    export type Inbound = {
        companyId: string;
        connectionId: string;
        page?: number | undefined;
        pageSize?: number | undefined;
        query?: string | undefined;
        orderBy?: string | undefined;
    };

    export const inboundSchema: z.ZodType<
        ListCommerceProductCategoriesRequest,
        z.ZodTypeDef,
        Inbound
    > = z
        .object({
            companyId: z.string(),
            connectionId: z.string(),
            page: z.number().int().default(1),
            pageSize: z.number().int().default(100),
            query: z.string().optional(),
            orderBy: z.string().optional(),
        })
        .transform((v) => {
            return {
                companyId: v.companyId,
                connectionId: v.connectionId,
                page: v.page,
                pageSize: v.pageSize,
                ...(v.query === undefined ? null : { query: v.query }),
                ...(v.orderBy === undefined ? null : { orderBy: v.orderBy }),
            };
        });

    export type Outbound = {
        companyId: string;
        connectionId: string;
        page: number;
        pageSize: number;
        query?: string | undefined;
        orderBy?: string | undefined;
    };

    export const outboundSchema: z.ZodType<
        Outbound,
        z.ZodTypeDef,
        ListCommerceProductCategoriesRequest
    > = z
        .object({
            companyId: z.string(),
            connectionId: z.string(),
            page: z.number().int().default(1),
            pageSize: z.number().int().default(100),
            query: z.string().optional(),
            orderBy: z.string().optional(),
        })
        .transform((v) => {
            return {
                companyId: v.companyId,
                connectionId: v.connectionId,
                page: v.page,
                pageSize: v.pageSize,
                ...(v.query === undefined ? null : { query: v.query }),
                ...(v.orderBy === undefined ? null : { orderBy: v.orderBy }),
            };
        });
}

/** @internal */
export namespace ListCommerceProductCategoriesResponse$ {
    export type Inbound = {
        HttpMeta: components.HTTPMetadata$.Inbound;
        CommerceProductCategories?: components.CommerceProductCategories$.Inbound | undefined;
    };

    export const inboundSchema: z.ZodType<
        ListCommerceProductCategoriesResponse,
        z.ZodTypeDef,
        Inbound
    > = z
        .object({
            HttpMeta: components.HTTPMetadata$.inboundSchema,
            CommerceProductCategories:
                components.CommerceProductCategories$.inboundSchema.optional(),
        })
        .transform((v) => {
            return {
                httpMeta: v.HttpMeta,
                ...(v.CommerceProductCategories === undefined
                    ? null
                    : { commerceProductCategories: v.CommerceProductCategories }),
            };
        });

    export type Outbound = {
        HttpMeta: components.HTTPMetadata$.Outbound;
        CommerceProductCategories?: components.CommerceProductCategories$.Outbound | undefined;
    };

    export const outboundSchema: z.ZodType<
        Outbound,
        z.ZodTypeDef,
        ListCommerceProductCategoriesResponse
    > = z
        .object({
            httpMeta: components.HTTPMetadata$.outboundSchema,
            commerceProductCategories:
                components.CommerceProductCategories$.outboundSchema.optional(),
        })
        .transform((v) => {
            return {
                HttpMeta: v.httpMeta,
                ...(v.commerceProductCategories === undefined
                    ? null
                    : { CommerceProductCategories: v.commerceProductCategories }),
            };
        });
}
