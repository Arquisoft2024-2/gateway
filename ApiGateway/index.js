const express = require('express');
const { createProxyMiddleware } = require('http-proxy-middleware');
const app = express();
const port = 3000;

app.use('/test1', createProxyMiddleware({
    target: 'http://127.0.0.1:3001',
    pathRewrite: {
        '^/test1': ''
    }
}))

app.use('/test1', createProxyMiddleware({
    target: 'http://127.0.0.1:3306',
    pathRewrite: {
        '^/test1': ''
    }
}))

app.use('/test1', createProxyMiddleware({
    target: 'http://127.0.0.1:3308',
    pathRewrite: {
        '^/test1': ''
    }
}))

app.listen(port, () => {
    console.log('el puerto de entrada es http://localhost:'+ port)
});