const express = require('express');
const tf = require('@tensorflow/tfjs-node');
const os = require('os');
const path = require('path');
require('dotenv').config()

const app = express(); // create a new Express app instance

const port = parseInt(process.env.PORT);

const loadModel = async () => {
  const model = await tf.loadLayersModel('file://' + path.join(__dirname, 'model/model.json'));
  return model;
}

let model;

loadModel().then(m => model = m);

function predict(sl, sw, pl, pw) {
  let resmessage = 'undefined';
  const temp = tf.tensor2d([[sl, sw, pl, pw]]);
  const result = model.predict(temp);
  const clas = result.argMax(1).dataSync()[0];

  if (clas === 0) {
    resmessage = 'Iris-setosa';
  } else if (clas === 1) {
    resmessage = 'Iris-versicolor';
  } else if (clas === 2) {
    resmessage = 'Iris-virginica';
  } else {
    resmessage = 'undefined';
  }

  return resmessage;
}

// middleware to parse JSON requests
app.use(express.json());

app.get('/', (req, res) => {
  res.send('hello world');
});

app.post('/', (req, res) => {
  const result = predict(req.body.sl, req.body.sw, req.body.pl, req.body.pw);
  res.json({ result });
});

app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});
