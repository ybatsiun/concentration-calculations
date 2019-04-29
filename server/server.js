"use strict"
const port = 3000;
const express = require('express');
const bodyParser = require('body-parser');
const app = express();
const { exec, spawn } = require('child_process');

app.listen(port, () => {
    console.log(`Started up at port ${port}`);
});
app.use(bodyParser.json());

app.post('/parseEquations', (req, res) => {
    const { equations } = req.body;

    exec(`python "${process.cwd()}/server/machineLearningModule/parseEquations.py" "${equations}"`, (err, stdout, stderr) => {
        if (err) {
            console.error(`exec error: ${err}`);
            res.status(500).send(err)
            return;
        };

        res.send(stdout);
    });

});

app.post('/calculateConstants', (req, res) => {
    const { equationData, config, experimentalData } = req.body;
    exec(`python "${process.cwd()}/machineLearningModule/main.py" "${experimentalData}" "${config}" "${equationData}"`,
        (err, stdout, stderr) => {
            if (err) {
                console.error(`exec error: ${stderr}`);
                res.status(500).send(stderr)
                return;
            };

            res.send(stdout);
        });
});