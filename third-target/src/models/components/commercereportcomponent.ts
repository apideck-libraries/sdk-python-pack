/*
 * Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT.
 */

import { ReportComponentMeasure, ReportComponentMeasure$ } from "./reportcomponentmeasure";
import * as z from "zod";

export type CommerceReportComponent = {
    /**
     * The component's dimension.
     */
    dimension?: number | undefined;
    /**
     * The component's display name.
     */
    dimensionDisplayName?: string | undefined;
    /**
     * The component's item number.
     */
    item?: number | undefined;
    /**
     * The component's item display name.
     */
    itemDisplayName?: string | undefined;
    measures?: Array<ReportComponentMeasure> | undefined;
    components?: Array<CommerceReportComponent> | undefined;
};

/** @internal */
export namespace CommerceReportComponent$ {
    export type Inbound = {
        dimension?: number | undefined;
        dimensionDisplayName?: string | undefined;
        item?: number | undefined;
        itemDisplayName?: string | undefined;
        measures?: Array<ReportComponentMeasure$.Inbound> | undefined;
        components?: Array<CommerceReportComponent$.Inbound> | undefined;
    };

    export const inboundSchema: z.ZodType<CommerceReportComponent, z.ZodTypeDef, Inbound> = z
        .object({
            dimension: z.number().int().optional(),
            dimensionDisplayName: z.string().optional(),
            item: z.number().int().optional(),
            itemDisplayName: z.string().optional(),
            measures: z.array(ReportComponentMeasure$.inboundSchema).optional(),
            components: z.array(z.lazy(() => CommerceReportComponent$.inboundSchema)).optional(),
        })
        .transform((v) => {
            return {
                ...(v.dimension === undefined ? null : { dimension: v.dimension }),
                ...(v.dimensionDisplayName === undefined
                    ? null
                    : { dimensionDisplayName: v.dimensionDisplayName }),
                ...(v.item === undefined ? null : { item: v.item }),
                ...(v.itemDisplayName === undefined
                    ? null
                    : { itemDisplayName: v.itemDisplayName }),
                ...(v.measures === undefined ? null : { measures: v.measures }),
                ...(v.components === undefined ? null : { components: v.components }),
            };
        });

    export type Outbound = {
        dimension?: number | undefined;
        dimensionDisplayName?: string | undefined;
        item?: number | undefined;
        itemDisplayName?: string | undefined;
        measures?: Array<ReportComponentMeasure$.Outbound> | undefined;
        components?: Array<CommerceReportComponent$.Outbound> | undefined;
    };

    export const outboundSchema: z.ZodType<Outbound, z.ZodTypeDef, CommerceReportComponent> = z
        .object({
            dimension: z.number().int().optional(),
            dimensionDisplayName: z.string().optional(),
            item: z.number().int().optional(),
            itemDisplayName: z.string().optional(),
            measures: z.array(ReportComponentMeasure$.outboundSchema).optional(),
            components: z.array(z.lazy(() => CommerceReportComponent$.outboundSchema)).optional(),
        })
        .transform((v) => {
            return {
                ...(v.dimension === undefined ? null : { dimension: v.dimension }),
                ...(v.dimensionDisplayName === undefined
                    ? null
                    : { dimensionDisplayName: v.dimensionDisplayName }),
                ...(v.item === undefined ? null : { item: v.item }),
                ...(v.itemDisplayName === undefined
                    ? null
                    : { itemDisplayName: v.itemDisplayName }),
                ...(v.measures === undefined ? null : { measures: v.measures }),
                ...(v.components === undefined ? null : { components: v.components }),
            };
        });
}
