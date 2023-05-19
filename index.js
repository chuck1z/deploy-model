const express = require('express');
const axios = require('axios');

const app = express();
app.use(express.json());

app.post('/', async (req, res) => {
    console.log(req.body)
  try {
    const data = {
      instances: [[parseFloat(req.body.sl), parseFloat(req.body.sw), parseFloat(req.body.pl), parseFloat(req.body.pw)]]
    };

    const response = await axios.post('https://deploy-modell-5tyme6tq4a-uc.a.run.app/v1/models/iris-classifier:predict', data);
    console.log(response.data.predictions[0][0])
    console.log(response.data.predictions[0][1])
    console.log(response.data.predictions[0][2])
    
    const arrayres = response.data.predictions[0]
    const indexres = arrayres.indexOf(Math.max(...arrayres))

    console.log(indexres)

    switch(indexres) {
        case 0:
            res.json("Iris-setosa");
          break;
        case 1:
            res.json("Iris-versicolor");
          break;
        case 2:
            res.json("Iris-virginica");
          break;
        default:
            res.json(response.data);
      }



  } catch (error) {
    res.status(500).json({ error: 'An error occurred' });
  }
});

app.listen(3000, () => {
  console.log('Server started on port 3000');
});
