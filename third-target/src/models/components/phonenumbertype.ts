/*
 * Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT.
 */

import * as z from "zod";

/**
 * The type of phone number
 */
export enum PhoneNumberType {
    Primary = "Primary",
    Landline = "Landline",
    Mobile = "Mobile",
    Fax = "Fax",
    Unknown = "Unknown",
}

/** @internal */
export const PhoneNumberType$ = z.nativeEnum(PhoneNumberType);
