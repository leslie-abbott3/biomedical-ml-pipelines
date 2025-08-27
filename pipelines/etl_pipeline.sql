
CREATE TABLE processed_data AS
SELECT 
    id,
    protein_id,
    ligand_id,
    binding_affinity,
    molecular_weight,
    polar_surface_area,
    hydrophobicity
FROM raw_data
WHERE binding_affinity IS NOT NULL;
