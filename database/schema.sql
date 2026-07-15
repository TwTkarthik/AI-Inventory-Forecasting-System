-- ===========================================================
-- AI Inventory Forecasting & Smart Warehouse Management System
-- Database Schema - Version 1
-- Table: Products
-- ===========================================================

CREATE EXTENSION IF NOT EXISTS pgcrypto;

CREATE TABLE IF NOT EXISTS products (

    product_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),

    sku VARCHAR(100) NOT NULL UNIQUE,

    mpn VARCHAR(100),

    product_name VARCHAR(255) NOT NULL,

    brand VARCHAR(100),

    category VARCHAR(100),

    description TEXT,

    selling_price NUMERIC(10,2) NOT NULL CHECK (selling_price >= 0),

    cost_price NUMERIC(10,2) NOT NULL CHECK (cost_price >= 0),

    barcode VARCHAR(100) UNIQUE,

    unit VARCHAR(50) NOT NULL,

    lead_time_days INTEGER DEFAULT 0 CHECK (lead_time_days >= 0),

    weight NUMERIC(10,2),

    length NUMERIC(10,2),

    width NUMERIC(10,2),

    height NUMERIC(10,2),

    primary_image TEXT,

    status VARCHAR(20) NOT NULL DEFAULT 'ACTIVE'
        CHECK (status IN ('ACTIVE', 'INACTIVE', 'DISCONTINUED')),

    status_reason TEXT,

    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    created_by UUID,

    updated_by UUID,

    deleted_at TIMESTAMP

);

-- ===========================================================
-- Indexes
-- ===========================================================

CREATE INDEX IF NOT EXISTS idx_products_name
ON products(product_name);

CREATE INDEX IF NOT EXISTS idx_products_category
ON products(category);

CREATE INDEX IF NOT EXISTS idx_products_brand
ON products(brand);

CREATE INDEX IF NOT EXISTS idx_products_status
ON products(status);