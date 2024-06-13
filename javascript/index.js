const http = require("http");
const fs  = require("fs");
const hostname  = "127.0.0.1";
const port   = 300;
const shop  = fs.readFileSync('chinu.html');
const server = http.createServer((req,res)=>
{
console.log(req.url);
res.statusCode = 2001;
res.setHeader('Content-Type','text/html');
res.end(shop);
});
server.listen(port,hostname,()=>
{
console.log(`server running at http://${hostname}:${port}/`);
});