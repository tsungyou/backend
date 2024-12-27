const express = require("express");
const router = express.Router();
const { Client } = require("pg");

// Initialize a PostgreSQL client
const pgClient = new Client({
    user: 'postgres',
    host: 'localhost',
    database: 'tw',
    password: 'buddyrich134',
    port: 5432,
});

pgClient.connect()
    .then(() => console.log("Connected to PostgreSQL"))
    .catch((err) => console.error("Failed to connect to PostgreSQL:", err));

// Define the /strategy route
router.get("/price", async (req, res) => {
    try {
        const codes = req.query.codes;
        if(!codes) {return res.statrus(400).send("Missing 'codes'query parameter");}
        const codesArray = codes.split(",").map((code) => code.trim());
        console.log(1)
        const result = await pgClient.query(`
            SELECT da, code, cl, hi, lo, op, vol, vol_share
            FROM public.price where code = ANY ($1)
            ORDER BY da DESC
            LIMIT 100;
        `, [codesArray]);
        res.json(result.rows); // Send query results as JSON
    } catch (err) {
        console.error("Error querying strategy data:", err);
        res.status(500).send("Failed to retrieve strategy data");
    }
});

module.exports = router;
