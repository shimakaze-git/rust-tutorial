fn main() {
    // Tupple
    let t = (2, 3.14, 0);
    let (a, b, c) = t;
    println!("a={}, b={}, c={}", a, b, c);

    let x = t.0;
    let y = t.1;
    let z = t.2;
    println!("x={}, y={}, z={}", x, y, z);

    // Array
    let a = [1, 2, 3, 4, 5];
    let x = a[0];
    let y = a[1];
    let z = a[2];
    println!("x={}, y={}, z={}", x, y, z);
}
