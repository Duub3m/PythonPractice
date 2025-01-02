const express = require('express');
const app = express();
const PORT = 8080;

app.use(express.json()); // Middleware to parse JSON requests

app.get('/tshirt', (req, res) => {
    res.status(200).send({
        tshirt: '👕',
        size: 'large'
    });
});

app.post('/tshirt/:id', (req, res) => { // Fixed route syntax
    const { id } = req.params;
    const { logo } = req.body;

    if (!logo) {
        return res.status(418).send({ message: 'We need a logo!' }); // Fixed "messsage" typo
    }

    res.send({
        tshirt: `👕 with your ${logo} and ID of ${id}`,
    });
});

app.listen(PORT, () => console.log(`Server is running on http://localhost:${PORT}`));
