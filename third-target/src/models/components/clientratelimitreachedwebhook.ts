/*
 * Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT.
 */

import {
    ClientRateLimitReachedWebhookData,
    ClientRateLimitReachedWebhookData$,
} from "./clientratelimitreachedwebhookdata";
import * as z from "zod";

/**
 * Webhook request body for a client that has reached their rate limit.
 */
export type ClientRateLimitReachedWebhook = {
    /**
     * Unique identifier for your client in Codat.
     */
    clientId?: string | undefined;
    /**
     * Name of your client in Codat.
     */
    clientName?: string | undefined;
    /**
     * Unique identifier for the rule.
     *
     * @deprecated field: This will be removed in a future release, please migrate away from it as soon as possible.
     */
    ruleId?: string | undefined;
    /**
     * The type of rule.
     */
    ruleType?: string | undefined;
    /**
     * Unique identifier of the webhook event.
     */
    alertId?: string | undefined;
    /**
     * A human-readable message about the webhook.
     */
    message?: string | undefined;
    data?: ClientRateLimitReachedWebhookData | undefined;
};

/** @internal */
export namespace ClientRateLimitReachedWebhook$ {
    export type Inbound = {
        ClientId?: string | undefined;
        ClientName?: string | undefined;
        RuleId?: string | undefined;
        RuleType?: string | undefined;
        AlertId?: string | undefined;
        Message?: string | undefined;
        Data?: ClientRateLimitReachedWebhookData$.Inbound | undefined;
    };

    export const inboundSchema: z.ZodType<ClientRateLimitReachedWebhook, z.ZodTypeDef, Inbound> = z
        .object({
            ClientId: z.string().optional(),
            ClientName: z.string().optional(),
            RuleId: z.string().optional(),
            RuleType: z.string().optional(),
            AlertId: z.string().optional(),
            Message: z.string().optional(),
            Data: ClientRateLimitReachedWebhookData$.inboundSchema.optional(),
        })
        .transform((v) => {
            return {
                ...(v.ClientId === undefined ? null : { clientId: v.ClientId }),
                ...(v.ClientName === undefined ? null : { clientName: v.ClientName }),
                ...(v.RuleId === undefined ? null : { ruleId: v.RuleId }),
                ...(v.RuleType === undefined ? null : { ruleType: v.RuleType }),
                ...(v.AlertId === undefined ? null : { alertId: v.AlertId }),
                ...(v.Message === undefined ? null : { message: v.Message }),
                ...(v.Data === undefined ? null : { data: v.Data }),
            };
        });

    export type Outbound = {
        ClientId?: string | undefined;
        ClientName?: string | undefined;
        RuleId?: string | undefined;
        RuleType?: string | undefined;
        AlertId?: string | undefined;
        Message?: string | undefined;
        Data?: ClientRateLimitReachedWebhookData$.Outbound | undefined;
    };

    export const outboundSchema: z.ZodType<Outbound, z.ZodTypeDef, ClientRateLimitReachedWebhook> =
        z
            .object({
                clientId: z.string().optional(),
                clientName: z.string().optional(),
                ruleId: z.string().optional(),
                ruleType: z.string().optional(),
                alertId: z.string().optional(),
                message: z.string().optional(),
                data: ClientRateLimitReachedWebhookData$.outboundSchema.optional(),
            })
            .transform((v) => {
                return {
                    ...(v.clientId === undefined ? null : { ClientId: v.clientId }),
                    ...(v.clientName === undefined ? null : { ClientName: v.clientName }),
                    ...(v.ruleId === undefined ? null : { RuleId: v.ruleId }),
                    ...(v.ruleType === undefined ? null : { RuleType: v.ruleType }),
                    ...(v.alertId === undefined ? null : { AlertId: v.alertId }),
                    ...(v.message === undefined ? null : { Message: v.message }),
                    ...(v.data === undefined ? null : { Data: v.data }),
                };
            });
}
