/* =========================================
   1. Total Orders & Sales by Year and Status
   ========================================= */
SELECT 
    YEAR_ID,
    STATUS,
    SUM(QUANTITYORDERED) AS total_units_sold,
    SUM(QUANTITYORDERED * PRICEEACH) AS total_sales
FROM sales_data_sample
GROUP BY YEAR_ID, STATUS
ORDER BY YEAR_ID, STATUS;


/* ===============================
   2. Total Orders & Sales by Year
   =============================== */
SELECT 
    YEAR_ID,
    SUM(QUANTITYORDERED) AS total_units_sold,
    SUM(QUANTITYORDERED * PRICEEACH) AS total_sales
FROM sales_data_sample
GROUP BY YEAR_ID
ORDER BY YEAR_ID;


/* ===============================================
   3. Total Orders & Sales by Product Line per Year
   =============================================== */
SELECT 
    YEAR_ID,
    PRODUCTLINE,
    SUM(QUANTITYORDERED) AS total_units_sold,
    SUM(QUANTITYORDERED * PRICEEACH) AS total_sales
FROM sales_data_sample
GROUP BY YEAR_ID, PRODUCTLINE
ORDER BY YEAR_ID, PRODUCTLINE;


/* ===========================================
   4. Total Orders & Sales by Country per Year
   =========================================== */
SELECT 
    YEAR_ID,
    COUNTRY,
    SUM(QUANTITYORDERED) AS total_units_sold,
    SUM(QUANTITYORDERED * PRICEEACH) AS total_sales
FROM sales_data_sample
GROUP BY YEAR_ID, COUNTRY
ORDER BY YEAR_ID, COUNTRY;


/* ===================================
   5. Top 10 Customers by Sales per Year
   =================================== */
SELECT 
    YEAR_ID,
    CUSTOMERNAME,
    SUM(QUANTITYORDERED) AS total_units_sold,
    SUM(QUANTITYORDERED * PRICEEACH) AS total_sales
FROM sales_data_sample
GROUP BY YEAR_ID, CUSTOMERNAME
ORDER BY total_sales DESC
LIMIT 10;


/* ==================================
   6. Monthly Sales Trend per Year
   ================================== */
SELECT 
    YEAR_ID,
    MONTH_ID,
    SUM(QUANTITYORDERED) AS total_units_sold,
    SUM(QUANTITYORDERED * PRICEEACH) AS total_sales
FROM sales_data_sample
GROUP BY YEAR_ID, MONTH_ID
ORDER BY YEAR_ID, MONTH_ID;


/* ==========================================
   7. Total Orders & Sales by Deal Size per Year
   ========================================== */
SELECT 
    YEAR_ID,
    DEALSIZE,
    SUM(QUANTITYORDERED) AS total_units_sold,
    SUM(QUANTITYORDERED * PRICEEACH) AS total_sales
FROM sales_data_sample
GROUP BY YEAR_ID, DEALSIZE
ORDER BY YEAR_ID, DEALSIZE;


/* ================================
   8. Top 10 Products by Sales
   ================================ */
SELECT 
    PRODUCTCODE,
    PRODUCTLINE,
    SUM(QUANTITYORDERED) AS total_units_sold,
    SUM(QUANTITYORDERED * PRICEEACH) AS total_sales
FROM sales_data_sample
GROUP BY PRODUCTCODE, PRODUCTLINE
ORDER BY total_sales DESC
LIMIT 10;
