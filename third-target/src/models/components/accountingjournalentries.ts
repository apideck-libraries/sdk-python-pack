/*
 * Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT.
 */

import { AccountingJournalEntry, AccountingJournalEntry$ } from "./accountingjournalentry";
import { Links, Links$ } from "./links";
import * as z from "zod";

export type AccountingJournalEntries = {
    results?: Array<AccountingJournalEntry> | undefined;
    /**
     * Current page number.
     */
    pageNumber: number;
    /**
     * Number of items to return in results array.
     */
    pageSize: number;
    /**
     * Total number of items.
     */
    totalResults: number;
    links: Links;
};

/** @internal */
export namespace AccountingJournalEntries$ {
    export type Inbound = {
        results?: Array<AccountingJournalEntry$.Inbound> | undefined;
        pageNumber: number;
        pageSize: number;
        totalResults: number;
        _links: Links$.Inbound;
    };

    export const inboundSchema: z.ZodType<AccountingJournalEntries, z.ZodTypeDef, Inbound> = z
        .object({
            results: z.array(AccountingJournalEntry$.inboundSchema).optional(),
            pageNumber: z.number().int(),
            pageSize: z.number().int(),
            totalResults: z.number().int(),
            _links: Links$.inboundSchema,
        })
        .transform((v) => {
            return {
                ...(v.results === undefined ? null : { results: v.results }),
                pageNumber: v.pageNumber,
                pageSize: v.pageSize,
                totalResults: v.totalResults,
                links: v._links,
            };
        });

    export type Outbound = {
        results?: Array<AccountingJournalEntry$.Outbound> | undefined;
        pageNumber: number;
        pageSize: number;
        totalResults: number;
        _links: Links$.Outbound;
    };

    export const outboundSchema: z.ZodType<Outbound, z.ZodTypeDef, AccountingJournalEntries> = z
        .object({
            results: z.array(AccountingJournalEntry$.outboundSchema).optional(),
            pageNumber: z.number().int(),
            pageSize: z.number().int(),
            totalResults: z.number().int(),
            links: Links$.outboundSchema,
        })
        .transform((v) => {
            return {
                ...(v.results === undefined ? null : { results: v.results }),
                pageNumber: v.pageNumber,
                pageSize: v.pageSize,
                totalResults: v.totalResults,
                _links: v.links,
            };
        });
}
