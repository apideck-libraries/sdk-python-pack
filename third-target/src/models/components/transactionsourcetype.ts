/*
 * Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT.
 */

import * as z from "zod";

/**
 * The type of source the transaction arose.
 */
export enum TransactionSourceType {
    Fee = "Fee",
    Order = "Order",
    Payment = "Payment",
    ServiceCharge = "ServiceCharge",
    Unknown = "Unknown",
}

/** @internal */
export const TransactionSourceType$ = z.nativeEnum(TransactionSourceType);
