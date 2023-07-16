-- MySQl: Best band ever!
-- Script Query table user Old school band
select band_name, (IFNULL(split,2020)-formed) AS lifespan FROM metal_bands WHERE style LIKE "%Glam rock%" ORDER BY lifespan DESC;
