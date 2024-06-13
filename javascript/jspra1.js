// const http  =require('http');
// const fs  = require('fs');
// http.createServer((req,res)=>
// {
// res.writeHead(200,{'ontent-Type':'text/html'});
// console.log(req.url);
// res.end("hello");
// }).listen(8080);





const http  = require('http');
const fs  = require('fs');
const port  = 2000;
const hostname  = '127.0.0.1';
const file  = fs.readFileSync('chinu.html');
const server  = http.createServer((req,res)=>
{
res.writeHead(200,{'Content-Type':'text/html'});
res.end('hello');
console.log(req.url);
});
server.listen(port,hostname,()=>
{
    console.log(`server running at http://${hostname}:${port}`);
});