/*
 * Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT.
 */

import * as components from "../components";
import * as z from "zod";

export type SetBankStatementUploadConfigurationRequest = {
    /**
     * Unique identifier for a company.
     */
    companyId: string;
    /**
     * Unique identifier for a connection.
     */
    connectionId: string;
    bankStatementUploadConfiguration?: components.BankStatementUploadConfiguration | undefined;
};

export type SetBankStatementUploadConfigurationResponse = {
    httpMeta: components.HTTPMetadata;
    /**
     * Success
     */
    bankStatementUploadConfiguration?: components.BankStatementUploadConfiguration | undefined;
};

/** @internal */
export namespace SetBankStatementUploadConfigurationRequest$ {
    export type Inbound = {
        companyId: string;
        connectionId: string;
        BankStatementUploadConfiguration?:
            | components.BankStatementUploadConfiguration$.Inbound
            | undefined;
    };

    export const inboundSchema: z.ZodType<
        SetBankStatementUploadConfigurationRequest,
        z.ZodTypeDef,
        Inbound
    > = z
        .object({
            companyId: z.string(),
            connectionId: z.string(),
            BankStatementUploadConfiguration:
                components.BankStatementUploadConfiguration$.inboundSchema.optional(),
        })
        .transform((v) => {
            return {
                companyId: v.companyId,
                connectionId: v.connectionId,
                ...(v.BankStatementUploadConfiguration === undefined
                    ? null
                    : { bankStatementUploadConfiguration: v.BankStatementUploadConfiguration }),
            };
        });

    export type Outbound = {
        companyId: string;
        connectionId: string;
        BankStatementUploadConfiguration?:
            | components.BankStatementUploadConfiguration$.Outbound
            | undefined;
    };

    export const outboundSchema: z.ZodType<
        Outbound,
        z.ZodTypeDef,
        SetBankStatementUploadConfigurationRequest
    > = z
        .object({
            companyId: z.string(),
            connectionId: z.string(),
            bankStatementUploadConfiguration:
                components.BankStatementUploadConfiguration$.outboundSchema.optional(),
        })
        .transform((v) => {
            return {
                companyId: v.companyId,
                connectionId: v.connectionId,
                ...(v.bankStatementUploadConfiguration === undefined
                    ? null
                    : { BankStatementUploadConfiguration: v.bankStatementUploadConfiguration }),
            };
        });
}

/** @internal */
export namespace SetBankStatementUploadConfigurationResponse$ {
    export type Inbound = {
        HttpMeta: components.HTTPMetadata$.Inbound;
        BankStatementUploadConfiguration?:
            | components.BankStatementUploadConfiguration$.Inbound
            | undefined;
    };

    export const inboundSchema: z.ZodType<
        SetBankStatementUploadConfigurationResponse,
        z.ZodTypeDef,
        Inbound
    > = z
        .object({
            HttpMeta: components.HTTPMetadata$.inboundSchema,
            BankStatementUploadConfiguration:
                components.BankStatementUploadConfiguration$.inboundSchema.optional(),
        })
        .transform((v) => {
            return {
                httpMeta: v.HttpMeta,
                ...(v.BankStatementUploadConfiguration === undefined
                    ? null
                    : { bankStatementUploadConfiguration: v.BankStatementUploadConfiguration }),
            };
        });

    export type Outbound = {
        HttpMeta: components.HTTPMetadata$.Outbound;
        BankStatementUploadConfiguration?:
            | components.BankStatementUploadConfiguration$.Outbound
            | undefined;
    };

    export const outboundSchema: z.ZodType<
        Outbound,
        z.ZodTypeDef,
        SetBankStatementUploadConfigurationResponse
    > = z
        .object({
            httpMeta: components.HTTPMetadata$.outboundSchema,
            bankStatementUploadConfiguration:
                components.BankStatementUploadConfiguration$.outboundSchema.optional(),
        })
        .transform((v) => {
            return {
                HttpMeta: v.httpMeta,
                ...(v.bankStatementUploadConfiguration === undefined
                    ? null
                    : { BankStatementUploadConfiguration: v.bankStatementUploadConfiguration }),
            };
        });
}
