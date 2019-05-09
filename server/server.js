"use strict"
const port = 3000;
const express = require('express');
const bodyParser = require('body-parser');
const app = express();
const { exec, spawn } = require('child_process');

app.options("/*", function (req, res, next) {
    setAccessHeaders(res);
    res.send(200);
});
app.use((req, res, next) => {
    setAccessHeaders(res);
    next();
});

app.listen(port, () => {
    console.log(`Started up at port ${port}`);
});
app.use(bodyParser.json());

app.post('/parseEquations', (req, res) => {
    const { equations } = req.body;

    exec(`python "${process.cwd()}/machineLearningModule/parseEquations.py" "${equations}"`, (err, stdout, stderr) => {
        if (err) {
            console.error(`exec error: ${err}`);
            res.status(500).send(err)
            return;
        };

        res.send(JSON.parse(stdout.replace(/'/g,'"')));
    });

});

function setAccessHeaders(res) {
    res.header('Access-Control-Allow-Origin', '*');
    res.header('Access-Control-Allow-Methods', '*');
    res.header('Access-Control-Allow-Headers', '*');
}

app.post('/calculateConstants', (req, res) => {
    let { equationData, config,experimentalData } = req.body;

    let equationData_s = '';
    equationData.forEach(element => {
        equationData_s = equationData_s + JSON.stringify(element) + ',';
    });
    equationData_s = '[' + equationData_s + ']';
    equationData_s = equationData_s.replace(/\"/g, "'");
    config = JSON.stringify(config).replace(/\"/g, "'");
    experimentalData = experimentalData.replace(/(\r\n|\n|\r)/gm,"");

    exec(`python "${process.cwd()}/machineLearningModule/main.py" "${experimentalData}" "${config}" "${equationData_s}"`,
        (err, stdout, stderr) => {
            if (err) {
                console.error(`exec error: ${stderr}`);
                res.status(500).send(stderr)
                return;
            };

            res.send(stdout);
        });
});