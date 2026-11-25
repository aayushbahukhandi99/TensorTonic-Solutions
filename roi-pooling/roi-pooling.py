import math

def roi_pool(feature_map: list, rois: list, output_size: int) -> list:
    """
    Returns a list of pooled grids.
    """
    # Write code here
    grids = []

    H = len(feature_map)
    W = len(feature_map[0])
    
    for x1, y1, x2, y2 in rois:
        roi_h = y2 - y1
        roi_w = x2 - x1

        pooled = []

        for i in range(output_size):
            row = []
            
            hs = y1 + (i * roi_h) // output_size
            he = y1 + ((i+1)*roi_h) // output_size

            if he == hs:
                he = hs + 1

            for j in range(output_size):
                ws = x1 + (j*roi_w) // output_size
                we = x1 + ((j+1) * roi_w) // output_size

                if we == ws:
                    we = ws + 1

                values = []

                for r in range(hs, he):
                    for c in range(ws, we):
                        values.append(feature_map[r][c])

                row.append(max(values))


            pooled.append(row)

        grids.append(pooled)

    return grids
            
        