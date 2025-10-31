fn fib(n: u32) -> u128 {
    match n {
        0 => 0,
        1 => 1,
        _ => {
            // iterative approach to avoid exponential recursion and stack overflow
            let mut a: u128 = 0;
            let mut b: u128 = 1;
            for _ in 2..=n {
                let tmp = a + b;
                a = b;
                b = tmp;
            }
            b
        }
    }
}

fn main() {
    println!("Fibonacci(100) = {}", fib(100));
}