fn fib(limit:u32)->u32{
    if n<=1{
    return n;
    }
    return fib(lim-2)+fib(lim-1);
}

fn main{
    println!("FIbonacci numbers {}",fib(100))
}