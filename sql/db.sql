CREATE TABLE plantdb_table_1 (
	ts timestamptz NOT NULL DEFAULT CURRENT_TIMESTAMP,
	moisture_value FLOAT4 NULL,
	temp_value FLOAT4 NULL,
	motion_value FLOAT4 NULL);