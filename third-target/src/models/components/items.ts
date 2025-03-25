/*
 * Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT.
 */

import * as z from "zod";

export type Items = {
    /**
     * Unique identifier for the group.
     */
    id?: string | undefined;
};

/** @internal */
export namespace Items$ {
    export type Inbound = {
        id?: string | undefined;
    };

    export const inboundSchema: z.ZodType<Items, z.ZodTypeDef, Inbound> = z
        .object({
            id: z.string().optional(),
        })
        .transform((v) => {
            return {
                ...(v.id === undefined ? null : { id: v.id }),
            };
        });

    export type Outbound = {
        id?: string | undefined;
    };

    export const outboundSchema: z.ZodType<Outbound, z.ZodTypeDef, Items> = z
        .object({
            id: z.string().optional(),
        })
        .transform((v) => {
            return {
                ...(v.id === undefined ? null : { id: v.id }),
            };
        });
}
