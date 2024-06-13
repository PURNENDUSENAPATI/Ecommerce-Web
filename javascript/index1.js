// const mod  = require("mod");
// console.log(average([3,4]))
// console.log('this is index1.js');

const express = require('express');
const ap  = exp();
const port  = 80;
ap.get((req,res)=>
{
    res.send("this is my first express app");
});
ap.listen(port,()=>
{
console.log(`the port is ${port}`);
});