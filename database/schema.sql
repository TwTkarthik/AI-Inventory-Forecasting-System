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

    supplier_id UUID,

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

    deleted_at TIMESTAMP,

    CONSTRAINT fk_supplier
    FOREIGN KEY (supplier_id)
    REFERENCES suppliers(supplier_id)
    ON DELETE SET NULL

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

CREATE TABLE IF NOT EXISTS suppliers (

    supplier_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),

    supplier_name VARCHAR(255) NOT NULL,

    contact_person VARCHAR(255),

    email VARCHAR(255),

    phone VARCHAR(20),

    address TEXT,

    lead_time_days INTEGER DEFAULT 0,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ===========================================================
-- Table: Inventory
-- ===========================================================

CREATE TABLE IF NOT EXISTS inventory (
    inventory_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),

    product_id UUID NOT NULL,

    quantity_on_hand INTEGER NOT NULL DEFAULT 0,

    reserved_quantity INTEGER NOT NULL DEFAULT 0,

    reorder_level INTEGER NOT NULL DEFAULT 10,

    warehouse_location VARCHAR(100),

    last_stock_update TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_inventory_product
        FOREIGN KEY (product_id)
        REFERENCES products(product_id)
        ON DELETE CASCADE
);