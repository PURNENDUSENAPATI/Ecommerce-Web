const http  = require('http');
const fs = require('fs');
const hostname = '127.0.0.1';
const port  = 3000;  
const server = http.createServer((req,res)=>
{
console.log(req.url);
res.statusCode = 200;
res.setHeader('content-type','text/plain');
res.end('hi');

});
server.listen(hostname,port ,() =>
{
 console.log(`server running t http://${hostname}:${port}/`);
});
