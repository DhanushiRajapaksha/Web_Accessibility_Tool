const express = require('express');
const axios = require('axios');
const cors = require('cors');

const app = express();
const port = 3001;

app.use(cors());
app.use(express.json());

app.post('/api/fetch-source', async (req, res) => {
  const { url } = req.body;

  try {
    const response = await axios.get(url);
    const sourceCode = response.data;
    res.send({ sourceCode });
  } catch (error) {
    res.status(500).send({ error: 'Failed to fetch the webpage source code.' });
  }
});

app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
