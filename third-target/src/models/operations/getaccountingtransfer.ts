/*
 * Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT.
 */

import * as components from "../components";
import * as z from "zod";

export type GetAccountingTransferRequest = {
    /**
     * Unique identifier for a company.
     */
    companyId: string;
    /**
     * Unique identifier for a connection.
     */
    connectionId: string;
    /**
     * Unique identifier for a transfer.
     */
    transferId: string;
};

export type GetAccountingTransferResponse = {
    httpMeta: components.HTTPMetadata;
    /**
     * Success
     */
    accountingTransfer?: components.AccountingTransfer | null | undefined;
};

/** @internal */
export namespace GetAccountingTransferRequest$ {
    export type Inbound = {
        companyId: string;
        connectionId: string;
        transferId: string;
    };

    export const inboundSchema: z.ZodType<GetAccountingTransferRequest, z.ZodTypeDef, Inbound> = z
        .object({
            companyId: z.string(),
            connectionId: z.string(),
            transferId: z.string(),
        })
        .transform((v) => {
            return {
                companyId: v.companyId,
                connectionId: v.connectionId,
                transferId: v.transferId,
            };
        });

    export type Outbound = {
        companyId: string;
        connectionId: string;
        transferId: string;
    };

    export const outboundSchema: z.ZodType<Outbound, z.ZodTypeDef, GetAccountingTransferRequest> = z
        .object({
            companyId: z.string(),
            connectionId: z.string(),
            transferId: z.string(),
        })
        .transform((v) => {
            return {
                companyId: v.companyId,
                connectionId: v.connectionId,
                transferId: v.transferId,
            };
        });
}

/** @internal */
export namespace GetAccountingTransferResponse$ {
    export type Inbound = {
        HttpMeta: components.HTTPMetadata$.Inbound;
        AccountingTransfer?: components.AccountingTransfer$.Inbound | null | undefined;
    };

    export const inboundSchema: z.ZodType<GetAccountingTransferResponse, z.ZodTypeDef, Inbound> = z
        .object({
            HttpMeta: components.HTTPMetadata$.inboundSchema,
            AccountingTransfer: z.nullable(components.AccountingTransfer$.inboundSchema).optional(),
        })
        .transform((v) => {
            return {
                httpMeta: v.HttpMeta,
                ...(v.AccountingTransfer === undefined
                    ? null
                    : { accountingTransfer: v.AccountingTransfer }),
            };
        });

    export type Outbound = {
        HttpMeta: components.HTTPMetadata$.Outbound;
        AccountingTransfer?: components.AccountingTransfer$.Outbound | null | undefined;
    };

    export const outboundSchema: z.ZodType<Outbound, z.ZodTypeDef, GetAccountingTransferResponse> =
        z
            .object({
                httpMeta: components.HTTPMetadata$.outboundSchema,
                accountingTransfer: z
                    .nullable(components.AccountingTransfer$.outboundSchema)
                    .optional(),
            })
            .transform((v) => {
                return {
                    HttpMeta: v.httpMeta,
                    ...(v.accountingTransfer === undefined
                        ? null
                        : { AccountingTransfer: v.accountingTransfer }),
                };
            });
}
