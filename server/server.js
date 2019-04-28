"use strict"
const port = 3000;
const express = require('express');
const app = express();

app.listen(port, () => {
    console.log(`Started up at port ${port}`);
});

app.get('/', (req, res) => {
    res.send({
        welcomeMessage: "Hello!"
    });
});