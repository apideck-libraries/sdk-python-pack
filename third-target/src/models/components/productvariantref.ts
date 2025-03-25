/*
 * Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT.
 */

import * as z from "zod";

/**
 * Reference that links the line item to the specific version of product that has been ordered.
 */
export type ProductVariantRef = {
    /**
     * The unique identifier of the product variant being referenced.
     */
    id: string;
    /**
     * Name of the product variant being referenced.
     */
    name?: string | undefined;
};

/** @internal */
export namespace ProductVariantRef$ {
    export type Inbound = {
        id: string;
        name?: string | undefined;
    };

    export const inboundSchema: z.ZodType<ProductVariantRef, z.ZodTypeDef, Inbound> = z
        .object({
            id: z.string(),
            name: z.string().optional(),
        })
        .transform((v) => {
            return {
                id: v.id,
                ...(v.name === undefined ? null : { name: v.name }),
            };
        });

    export type Outbound = {
        id: string;
        name?: string | undefined;
    };

    export const outboundSchema: z.ZodType<Outbound, z.ZodTypeDef, ProductVariantRef> = z
        .object({
            id: z.string(),
            name: z.string().optional(),
        })
        .transform((v) => {
            return {
                id: v.id,
                ...(v.name === undefined ? null : { name: v.name }),
            };
        });
}
